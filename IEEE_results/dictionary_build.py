from pathlib import Path
import numpy as np
import pandas as pd
import rainflow
from scipy.signal import lfilter
import json
from scipy.signal import butter, sosfiltfilt
from scipy.signal import butter, sosfiltfilt, bilinear

base_dir_load = r"E:\IEEE_GM_2027\Dataset\Data_for_simulation"
dictionary_master = {}


def building(files_load, sims_dir, results_dir, spikes=None):

    ###############################
    # Load
    ###############################

    def load_characteristics(p, dt=0.02, hyst=0.1, min_freq=1/300):
        """Basic load characteristics of one power profile p [W]. Swing over the whole period, no averaging."""
        p = np.asarray(p, dtype=float)
        n = len(p)
        duration_h = n * dt / 3600

        p05, p95 = np.percentile(p, [5, 95])
        swing = p95 - p05
        mid = p05 + 0.5 * swing                                   # high-load threshold

        # load transitions with hysteresis (±10 % of swing)
        hi, lo = mid + hyst * swing, mid - hyst * swing
        state = np.where(p > hi, 1, np.where(p < lo, 0, -1))
        s = state[state >= 0]
        transitions = int(np.count_nonzero(np.diff(s))) if len(s) > 1 else 0

        # dominant fluctuation period (strongest FFT component, period <= 300 s)
        spec = np.abs(np.fft.rfft(p - p.mean())) ** 2
        freq = np.fft.rfftfreq(n, dt)
        mask = freq >= min_freq
        f_dom = freq[mask][np.argmax(spec[mask])] if (mask.any() and swing > 0) else np.nan

        return {
            "P_mean_MW": p.mean() / 1e6,
            "P_max_MW": p.max() / 1e6,
            "P_min_MW": p.min() / 1e6,
            "Energy_MWh": p.sum() * dt / 3.6e9,
            "Peak_to_mean": p.max() / p.mean(),
            "Swing_p95_p05_MW": swing / 1e6,
            "Time_at_high_load_pct": 100 * np.mean(p > mid),
            "Dominant_period_s": 1 / f_dom if np.isfinite(f_dom) and f_dom > 0 else np.nan,
            "Transitions_per_h": transitions / duration_h,
            "Ramp_p99_MW_per_s": np.percentile(np.abs(np.diff(p)) / dt, 99) / 1e6,
        }

    def swing_by_period(p, dt=0.02, periods_s=(1, 5, 10, 60), block_s=900.0,
                        stats=("max", "mean", "median")):
        """
        Swing p95-p05 in consecutive windows of T [s] within each 15-min block, from raw 20 ms data.
        For each block: statistic (max / mean / median) over its windows of
          - the swing [MW],
          - the swing weighted by the energy of the same window [MW * MJ], and
          - the swing weighted by the RMS power of the same window [MW * MW].
        The worst block of the profile is returned.
        """
        p = np.asarray(p, dtype=float)
        kb = int(round(block_s / dt))
        nb = len(p) // kb
        blocks = [p[i * kb:(i + 1) * kb] for i in range(nb)] if nb >= 1 else [p]

        agg = {"max": np.max, "mean": np.mean, "median": np.median}
        out = {}
        for T in periods_s:
            k = int(round(T / dt))
            for st in stats:
                key = f"Swing_period{T:g}s_{st}_MW"
                vals, vals_e, vals_r = [], [], []
                for b in blocks:
                    m = len(b) // k
                    if m < 1:
                        continue
                    w = b[: m * k].reshape(m, k)
                    s = (np.percentile(w, 95, axis=1) - np.percentile(w, 5, axis=1)) / 1e6  # swing per window [MW]
                    e = w.sum(axis=1) * dt / 1e6  # energy per window [MJ]
                    r = np.sqrt(np.mean(w ** 2, axis=1)) / 1e6  # RMS power per window [MW]
                    vals.append(agg[st](s))
                    vals_e.append(agg[st](s * e))
                    vals_r.append(agg[st](s * r))
                out[key] = max(vals) if vals else np.nan
                out[f"{key}_x_E_MJ"] = max(vals_e) if vals_e else np.nan
                out[f"{key}_x_Prms_MW"] = max(vals_r) if vals_r else np.nan
        return out

    def _flicker_pst(d, dt=0.02, window_s=600.0, settle_s=20.0):
        """
        Short-term flicker severity Pst (IEC 61000-4-15, 230 V lamp) from a relative voltage
        fluctuation d(t) = dV/V sampled at dt. Works on the fluctuation envelope, so the
        demodulator is skipped; the gain is calibrated so that 8.8 Hz sinusoidal
        modulation of 0.25 % peak-to-peak gives Pinst = 1. Returns the largest Pst of all 10-min windows.
        """
        fs = 1.0 / dt
        # block 3: 0.05 Hz high-pass + lamp-eye weighting filter
        b_hp, a_hp = butter(1, 0.05, btype="highpass", fs=fs)
        K, lam = 1.74802, 2 * np.pi * 4.05981
        w1, w2, w3, w4 = 2 * np.pi * np.array([9.15494, 2.27979, 1.22535, 21.9])
        num = K * w1 * np.polymul([1.0, 0.0], [1.0 / w2, 1.0])
        den = np.polymul([1.0, 2 * lam, w1 ** 2], np.polymul([1.0 / w3, 1.0], [1.0 / w4, 1.0]))
        b_w, a_w = bilinear(num, den, fs)
        # block 4: squaring + first-order low-pass (300 ms)
        a_lp = np.exp(-dt / 0.3)

        def chain(x):
            y = lfilter(b_w, a_w, lfilter(b_hp, a_hp, x))
            return lfilter([1 - a_lp], [1, -a_lp], y ** 2)

        # calibration: 8.8 Hz, 0.25 % peak-to-peak -> Pinst = 1
        t = np.arange(int(round(60 / dt))) * dt
        ref = chain(0.5 * 0.0025 * np.sin(2 * np.pi * 8.8 * t))
        g = 1.0 / ref[int(round(settle_s / dt)):].mean()

        pinst = g * chain(d)[int(round(settle_s / dt)):]      # drop filter start-up

        # block 5: statistical evaluation per 10-min window
        kw = int(round(window_s / dt))
        pst = []
        for i in range(len(pinst) // kw):
            w = pinst[i * kw:(i + 1) * kw]
            P = lambda q: np.percentile(w, 100 - q)          # level exceeded q % of the time
            P1s = (P(0.7) + P(1) + P(1.5)) / 3
            P3s = (P(2.2) + P(3) + P(4)) / 3
            P10s = (P(6) + P(8) + P(10) + P(13) + P(17)) / 5
            P50s = (P(30) + P(50) + P(80)) / 3
            pst.append(np.sqrt(0.0314 * P(0.1) + 0.0525 * P1s + 0.0657 * P3s + 0.28 * P10s + 0.08 * P50s))
        return max(pst) if pst else np.nan

    def grid_operator_metrics(p, dt=0.02, P_rated=2e6, ercot_window_s=5.0, ercot_thr_pct=25.0, lipa_band_Hz=(5.0, 24.0),
                              lipa_window_s=10.0, soco_bands_Hz=((0.1, 0.5), (0.5, 0.8), (0.8, 2.0)),
                              soco_window_s=60.0, ramp_window_s=60.0, avg_s=(4.0, 300.0), scr=20.0):
        """
        Load metrics in the format of existing grid-operator rules, from a power profile p [W] at dt [s].

        ERCOT : number of repetitive changes above a threshold within a sliding 5 s window [1/h].
                The rule uses 10 MW for facility-level loads; here the threshold is a share of the
                converter rating (ercot_thr_pct), because the absolute value does not scale to 2 MW.
        LIPA  : largest peak-to-peak amplitude of the 5-55 Hz band within a rolling 10 s window [MW].
                At 20 ms sampling only frequencies below 25 Hz are resolvable -> band 5-24 Hz.
        Ramp  : largest change between consecutive 1-min average powers [MW/min] (ramp-rate limits).
        SCADA / settlement : swing p95-p05 after averaging to 4 s and 5 min [MW].
        SoCo  : largest peak-to-peak amplitude in the 0.1-0.5, 0.5-0.8 and 0.8-2 Hz bands within a
            rolling 60 s window [MW] (Southern Company inter-area, sub-regional and local bands).
        """
        p = np.asarray(p, dtype=float)
        n = len(p)
        duration_h = n * dt / 3600
        out = {}

        # ---- ERCOT: repetitive changes above threshold within a sliding window ----
        s = pd.Series(p)
        k = max(int(round(ercot_window_s / dt)) + 1, 2)
        change = (s.rolling(k).max() - s.rolling(k).min()).to_numpy()
        above = np.nan_to_num(change) > ercot_thr_pct / 100 * P_rated
        events = np.count_nonzero(np.diff(above.astype(int)) == 1) + int(above[0])  # rising edges = separate events
        out[f"ERCOT_changes_gt{ercot_thr_pct:g}pct_in_{ercot_window_s:g}s_per_h"] = events / duration_h

        # ---- LIPA: band-limited oscillation amplitude in a rolling window ----
        f_nyq = 0.5 / dt
        lo, hi = lipa_band_Hz[0], min(lipa_band_Hz[1], 0.95 * f_nyq)
        sos = butter(4, [lo, hi], btype="bandpass", fs=1 / dt, output="sos")
        pb = pd.Series(sosfiltfilt(sos, p - p.mean()))
        kw = int(round(lipa_window_s / dt))
        amp = (pb.rolling(kw).max() - pb.rolling(kw).min()).to_numpy()
        out[f"LIPA_band_{lo:g}_{hi:g}Hz_amp_{lipa_window_s:g}s_MW"] = np.nanmax(amp) / 1e6

        # ---- Ramp rate in MW/min from 1-min averages ----
        kr = int(round(ramp_window_s / dt))
        m = n // kr
        if m >= 2:
            pr = p[: m * kr].reshape(m, kr).mean(axis=1)
            out["Ramp_max_MW_per_min"] = np.abs(np.diff(pr)).max() / 1e6 * (60.0 / ramp_window_s)
            out["Variability_1min_std_MW"] = np.std(np.diff(pr)) / 1e6      # regulation / balancing view
        else:
            out["Ramp_max_MW_per_min"] = np.nan
            out["Variability_1min_std_MW"] = np.nan

        # ---- SCADA (4 s) and settlement (5 min) resolution ----
        for a_s in avg_s:
            ka = int(round(a_s / dt))
            ma = n // ka
            if ma < 2:
                out[f"Swing_avg_{a_s:g}s_MW"] = np.nan
                continue
            pa = p[: ma * ka].reshape(ma, ka).mean(axis=1)
            q05, q95 = np.percentile(pa, [5, 95])
            out[f"Swing_avg_{a_s:g}s_MW"] = (q95 - q05) / 1e6

        # ---- Southern Company: oscillation amplitude per band in a rolling window ----
        # Absolute amplitude [MW] instead of variance share, so the metric keeps the size
        # of the oscillation. Window long enough for several periods of the lowest band (0.1 Hz -> 10 s).
        ks = int(round(soco_window_s / dt))
        for lo_b, hi_b in soco_bands_Hz:
            key = f"SoCo_band_{lo_b:g}_{hi_b:g}Hz_amp_{soco_window_s:g}s_MW"
            sos_b = butter(4, [lo_b, hi_b], btype="bandpass", fs=1 / dt, output="sos")
            pb_b = sosfiltfilt(sos_b, p - p.mean())
            edge = int(round(3.0 / lo_b / dt))  # discard ~3 periods of the lowest frequency at each end
            pb_b = pb_b[edge:-edge] if n > 2 * edge + ks else np.array([])
            if len(pb_b) < ks:
                out[key] = np.nan  # profile too short for this band and window
                continue
            pb_b = pd.Series(pb_b)
            amp_b = (pb_b.rolling(ks).max() - pb_b.rolling(ks).min()).to_numpy()
            out[key] = np.nanmax(amp_b) / 1e6

        # ---- Flicker Pst (IEC 61000-4-15 / IEEE 1453) ----
        # dV/V ~ dP / S_sc. Pst is linear in dV/V, so the ranking does not depend on the assumed SCR.
        d = (p - p.mean()) / (scr * P_rated)
        out[f"Flicker_Pst_max_SCR{scr:g}"] = _flicker_pst(d, dt=dt)

        # ---- Metering / billing: 15-min peak demand and load factor ----
        k15 = int(round(900.0 / dt))
        m15 = n // k15
        if m15 >= 1:
            p15 = p[: m15 * k15].reshape(m15, k15).mean(axis=1)
            out["Peak_demand_15min_MW"] = p15.max() / 1e6
            out["Load_factor_15min"] = p.mean() / p15.max()
        else:
            out["Peak_demand_15min_MW"] = np.nan
            out["Load_factor_15min"] = np.nan

        return out

    def _run_lengths(state, dt):
        """Durations [s] of consecutive runs of 1 (high) and 0 (low) in a 0/1 state array."""
        edges = np.flatnonzero(np.diff(state)) + 1
        starts = np.r_[0, edges]
        lengths = np.diff(np.r_[starts, len(state)]) * dt
        vals = state[starts]
        # drop first and last run: they are cut by the window and not complete
        return lengths[1:-1][vals[1:-1] == 1], lengths[1:-1][vals[1:-1] == 0], starts[vals == 1] * dt

    def load_characteristics_extra(p, dt=0.02, P_rated=2e6, hyst=0.1, taus=(0.26, 3.31, 159.0), windows_s=(0.1, 1.0, 5.0, 60.0), avg_s=(1.0, 60.0, 900.0), bands_Hz=((0, 0.017), (0.017, 0.1), (0.1, 0.5), (0.5, 0.8), (0.8, 2.0), (2.0, 25.0)), dP_exp=17.7, block_s=900.0):
        """
        Additional load characteristics of one power profile p [W], sampled at dt [s].
        Complements load_characteristics(): same hysteresis thresholds, more views on the shape.
        """
        p = np.asarray(p, dtype=float)
        n = len(p)
        duration_h = n * dt / 3600
        out = {}

        # 1) Two-level description: plateau levels and step height
        p05, p95 = np.percentile(p, [5, 95])
        swing = p95 - p05
        mid = p05 + 0.5 * swing
        hi, lo = mid + hyst * swing, mid - hyst * swing

        P_high = np.median(p[p > hi]) if np.any(p > hi) else np.nan
        P_low = np.median(p[p < lo]) if np.any(p < lo) else np.nan
        out["P_high_level_MW"] = P_high / 1e6
        out["P_low_level_MW"] = P_low / 1e6
        out["Step_height_MW"] = (P_high - P_low) / 1e6
        out["Step_height_pct_rating"] = 100 * (P_high - P_low) / P_rated
        out["P_p999_MW"] = np.percentile(p, 99.9) / 1e6              # robust peak

        # 2) Dwell times: how long the load stays high / low per burst
        state = np.where(p > hi, 1, np.where(p < lo, 0, -1))
        state = pd.Series(state).replace(-1, np.nan).ffill().bfill().to_numpy()   # hysteresis: keep last state
        high_d, low_d, burst_starts = _run_lengths(state.astype(int), dt)

        out["Dwell_high_mean_s"] = high_d.mean() if len(high_d) else np.nan
        out["Dwell_high_p95_s"] = np.percentile(high_d, 95) if len(high_d) else np.nan
        out["Dwell_low_mean_s"] = low_d.mean() if len(low_d) else np.nan
        out["Dwell_low_p95_s"] = np.percentile(low_d, 95) if len(low_d) else np.nan
        out["Bursts_per_h"] = len(high_d) / duration_h
        period = np.diff(burst_starts)
        out["Burst_period_mean_s"] = period.mean() if len(period) else np.nan
        out["Burst_period_CV"] = period.std() / period.mean() if len(period) > 1 else np.nan   # 0 = perfectly regular

        # 3) Rainflow on the power profile (low-pass filtered with the fastest tau against 20 ms noise)
        a = np.exp(-dt / taus[0])
        p_rf = lfilter([1 - a], [1, -a], p, zi=[a * p[0]])[0]
        cyc = np.array([(r, c) for r, _, c, _, _ in rainflow.extract_cycles(p_rf)])
        dP, cnt = (cyc[:, 0], cyc[:, 1]) if len(cyc) else (np.empty(0), np.empty(0))
        x = dP / P_rated
        out["Power_cycles_ge_10pct_per_h"] = cnt[x >= 0.10].sum() / duration_h
        out["Power_cycles_ge_30pct_per_h"] = cnt[x >= 0.30].sum() / duration_h
        out["Power_cycles_ge_50pct_per_h"] = cnt[x >= 0.50].sum() / duration_h
        out["Power_cycle_dP_max_MW"] = dP.max() / 1e6 if len(dP) else np.nan
        out["Damage_proxy_per_h"] = np.sum(cnt * x ** dP_exp) / duration_h        # sum n * (dP/P_rated)^k

        # 4) Thermally filtered swing: swing seen through a first-order low-pass
        for tau in taus:
            a = np.exp(-dt / tau)
            pf = lfilter([1 - a], [1, -a], p, zi=[a * p[0]])[0]
            skip = min(int(5 * tau / dt), n // 2)                                  # ignore filter start-up
            q05, q95 = np.percentile(pf[skip:], [5, 95])
            out[f"Swing_filtered_tau{tau:g}s_MW"] = (q95 - q05) / 1e6

        # 5) Moving-window power change (AESO: 100 ms, ATC: 5 s)
        s = pd.Series(p)
        for w in windows_s:
            k = max(int(round(w / dt)) + 1, 2)
            rng = (s.rolling(k).max() - s.rolling(k).min()).to_numpy()
            out[f"Max_change_in_{w:g}s_MW"] = np.nanmax(rng) / 1e6

        # 6) Resolution: what survives averaging (1 s, 1 min, 15 min metering)
        for a_s in avg_s:
            k = int(round(a_s / dt))
            m = n // k
            if m < 2:
                out[f"Swing_avg_{a_s:g}s_MW"] = np.nan
                continue
            pa = p[: m * k].reshape(m, k).mean(axis=1)
            q05, q95 = np.percentile(pa, [5, 95])
            out[f"Swing_avg_{a_s:g}s_MW"] = (q95 - q05) / 1e6

        # 7) Spectral content in bands (share of fluctuation variance)
        spec = np.abs(np.fft.rfft(p - p.mean())) ** 2
        freq = np.fft.rfftfreq(n, dt)
        total = spec[1:].sum()
        for f_lo, f_hi in bands_Hz:
            sel = (freq > f_lo) & (freq <= f_hi)
            out[f"Var_share_{f_lo:g}_{f_hi:g}Hz_pct"] = 100 * spec[sel].sum() / total if total > 0 else np.nan

        # 8) Artefacts of tiling 15-min blocks to longer profiles
        kb = int(round(block_s / dt))
        seams = np.arange(kb, n, kb)
        out["Seam_jump_max_MW"] = np.abs(p[seams] - p[seams - 1]).max() / 1e6 if len(seams) else np.nan
        k60 = int(round(60 / dt))
        out["Startup_60s_mean_minus_block_mean_MW"] = (p[:k60].mean() - p[:min(kb, n)].mean()) / 1e6

        # 9) Loss-weighted level and thermally relevant peak level
        out["P_rms_MW"] = np.sqrt(np.mean(p ** 2)) / 1e6
        for w_s in (60.0, 180.0, 300.0):
            kw = int(round(w_s / dt))
            if n >= kw:
                out[f"P_max_avg_{w_s:g}s_MW"] = pd.Series(p).rolling(kw).mean().max() / 1e6
            else:
                out[f"P_max_avg_{w_s:g}s_MW"] = np.nan

        return out

    def add_spikes(p, dt=0.02, rate_per_h=60, dur_s=0.04, amp_frac=0.25, P_rated=2e6, seed=0):
        """Adds short positive spikes (amp_frac of rating, dur_s long) at random times to one profile p [W]."""
        rng = np.random.default_rng(seed)
        p = np.asarray(p, dtype=float).copy()
        n, k = len(p), max(int(round(dur_s / dt)), 1)
        n_spikes = int(rate_per_h * n * dt / 3600)
        for i in rng.integers(0, n - k, n_spikes):
            p[i:i + k] += amp_frac * P_rated
        return np.minimum(p, P_rated)  # never above converter rating

    def build_load_characteristics(base_dir, files, until_s, dt=0.02, P_rated=2e6, spikes=None):
        """Returns {scenario_name: {load characteristics}}. spikes = None or dict of add_spikes settings."""
        Load_characteristics = {}
        for chip, file in files.items():
            df = pd.read_parquet(Path(base_dir) / chip / "Dataframes" / file)
            df = df[df["time_s"] < until_s]

            for j, col in enumerate(df.columns.drop("time_s")):
                p = df[col].to_numpy()
                if spikes is not None:
                    p = add_spikes(p, dt=dt, P_rated=P_rated, seed=j, **spikes)  # own seed per profile

                Load_characteristics[col] = {"chip": chip, "duration_s": len(df) * dt}
                Load_characteristics[col].update(load_characteristics(p, dt=dt))
                Load_characteristics[col].update(load_characteristics_extra(p, dt=dt, P_rated=P_rated))
                Load_characteristics[col].update(swing_by_period(p, dt=dt))
                Load_characteristics[col].update(grid_operator_metrics(p, dt=dt, P_rated=P_rated))

        return Load_characteristics

    dictionary_master["Load_characteristics"] = build_load_characteristics(base_dir_load, files_load, until_s=3600,spikes=spikes)

    ###############################
    # Electrical
    ###############################

    def build_electrical_characteristics(results_dir, dt=0.001, input_step=0.02):
        """Returns {scenario_name: {electrical characteristics}} of the simulated IGBT-diode pair."""
        results_dir = Path(results_dir)
        spp = int(round(input_step / dt))                      # samples per 20 ms step
        cols = ["P_I", "P_D", "is_I", "is_D", "P_sw_I", "P_sw_D", "P_con_I", "P_con_D"]

        Electrical_characteristics = {}

        for sim in sorted(p for p in results_dir.iterdir() if p.is_dir()):
            loss_dir = sim / "df_electrical_loss"
            elec_file = sim / "df_electrical" / "df.parquet"
            if not loss_dir.exists() or not elec_file.exists():
                continue

            files = sorted(loss_dir.glob("df_*.parquet"), key=lambda f: int(f.stem.split("_")[1]))
            df = pd.concat([pd.read_parquet(f, columns=cols) for f in files], ignore_index=True)
            P = pd.read_parquet(elec_file, columns=["P"])["P"].to_numpy()

            n = len(df) // spp * spp                           # whole 20 ms steps only
            step_avg = lambda x: x[:n].reshape(-1, spp).mean(axis=1)

            P_I, P_D = df["P_I"].to_numpy(), df["P_D"].to_numpy()
            is_I, is_D = df["is_I"].to_numpy(), df["is_D"].to_numpy()
            P_I_step, P_D_step = step_avg(P_I), step_avg(P_D)

            P_I_mean, P_D_mean = P_I.mean(), P_D.mean()
            P_sw_total = df["P_sw_I"].mean() + df["P_sw_D"].mean()

            Electrical_characteristics[sim.name] = {
                # device currents
                "I_IGBT_rms_A": np.sqrt(np.mean(is_I ** 2)),
                "I_IGBT_peak_A": np.abs(is_I).max(),
                "I_Diode_rms_A": np.sqrt(np.mean(is_D ** 2)),
                "I_Diode_peak_A": np.abs(is_D).max(),
                # losses per device (20 ms averages)
                "P_loss_IGBT_mean_W": P_I_mean,
                "P_loss_IGBT_max_W": P_I_step.max(),
                "P_loss_IGBT_swing_W": np.percentile(P_I_step, 95) - np.percentile(P_I_step, 5),
                "P_loss_Diode_mean_W": P_D_mean,
                "P_loss_Diode_max_W": P_D_step.max(),
                "P_loss_Diode_swing_W": np.percentile(P_D_step, 95) - np.percentile(P_D_step, 5),
                # composition
                "Switching_share_pct": 100 * P_sw_total / (P_I_mean + P_D_mean),
                "Diode_share_pct": 100 * P_D_mean / (P_I_mean + P_D_mean),
                # losses of the IGBT-diode pair relative to load power
                "Loss_ratio_pct": 100 * (P_I_mean + P_D_mean) / P.mean(),
            }

            del df, P, P_I, P_D, is_I, is_D, P_I_step, P_D_step

        return Electrical_characteristics

    dictionary_master["Electrical_characteristics"] = build_electrical_characteristics(sims_dir)

    ###############################
    # Thermal
    ###############################

    def _weighted_percentile(values, weights, q):
        """Percentile q (0–100) of values with weights (e.g. rainflow counts 0.5 / 1)."""
        if len(values) == 0:
            return np.nan
        order = np.argsort(values)
        v, w = values[order], weights[order]
        cum = np.cumsum(w) / w.sum()
        return v[np.searchsorted(cum, q / 100)]

    def _read_chunks(folder, cols):
        """Reads df_1.parquet, df_2.parquet, ... (ignores df_IGBT_final / df_Diode_final)."""
        files = [f for f in folder.glob("df_*.parquet") if f.stem.split("_")[1].isdigit()]
        files = sorted(files, key=lambda f: int(f.stem.split("_")[1]))
        return pd.concat([pd.read_parquet(f, columns=cols) for f in files], ignore_index=True)

    def _burst_cycle_statistics(dT, Tm, t_cyc, cnt, prefix, duration_h, dT_min=5.0, t_split=0.1, k_eq=15.0):
        """
        Statistics of burst cycles: load cycles (duration >= t_split) with dT >= dT_min,
        without the heat-up half cycle from ambient (the largest half cycle).
        k_eq: exponent for the damage-equivalent dT (Nf ~ dT^-15 in the relevant range).
        """
        burst = (t_cyc >= t_split) & (dT >= dT_min)

        half = np.flatnonzero(cnt == 0.5)                       # remove heat-up: largest half cycle
        if len(half):
            burst[half[np.argmax(dT[half])]] = False

        d, w, T, t = dT[burst], cnt[burst], Tm[burst], t_cyc[burst]
        if w.sum() == 0:
            keys = ["cycles_per_h", "dT_mean_K", "dT_median_K", "dT_p95_K", "dT_max_K",
                    "dT_eq_K", "Tmean_C", "duration_mean_s"]
            return {f"{prefix}_burst_{k}": (0.0 if k == "cycles_per_h" else np.nan) for k in keys}

        return {
            f"{prefix}_burst_cycles_per_h": w.sum() / duration_h,
            f"{prefix}_burst_dT_mean_K": np.sum(d * w) / w.sum(),
            f"{prefix}_burst_dT_median_K": _weighted_percentile(d, w, 50),
            f"{prefix}_burst_dT_p95_K": _weighted_percentile(d, w, 95),
            f"{prefix}_burst_dT_max_K": d.max(),
            f"{prefix}_burst_dT_eq_K": (np.sum(w * d ** k_eq) / w.sum()) ** (1 / k_eq),   # damage-equivalent dT
            f"{prefix}_burst_Tmean_C": np.sum(T * w) / w.sum(),
            f"{prefix}_burst_duration_mean_s": np.sum(t * w) / w.sum(),
        }

    def _cycle_statistics(df, dev, prefix, duration_h, t_split=0.1):
        """
        Thermal cycle statistics from rainflow results of one device.
        Cycles shorter than t_split [s] are grid cycles (50 Hz ripple),
        longer ones are load cycles (caused by load changes).
        Burst cycles: load cycles with dT >= 5 K, heat-up half cycle removed.
        """
        dT = df[f"deltaT_{dev}"].to_numpy()
        Tm = df[f"Tmean_{dev}"].to_numpy() - 273.15
        t_cyc = df[f"thermal_cycle_period_{dev}"].to_numpy()
        cnt = df[f"count_{dev}"].to_numpy()

        wmean = lambda x, w: np.sum(x * w) / w.sum() if w.sum() > 0 else np.nan
        band = lambda lo, hi: cnt[(dT >= lo) & (dT < hi)].sum() / duration_h

        load = t_cyc >= t_split
        grid = ~load

        stats = {
            # all cycles
            f"{prefix}_cycles_per_h": cnt.sum() / duration_h,
            f"{prefix}_dT_max_K": dT.max() if len(dT) else np.nan,
            f"{prefix}_dT_mean_K": wmean(dT, cnt),
            f"{prefix}_dT_p95_K": _weighted_percentile(dT, cnt, 95),
            f"{prefix}_cycles_dT_lt5_per_h": band(0, 5),
            f"{prefix}_cycles_dT_5_10_per_h": band(5, 10),
            f"{prefix}_cycles_dT_10_20_per_h": band(10, 20),
            f"{prefix}_cycles_dT_ge20_per_h": band(20, np.inf),
            f"{prefix}_cycle_Tmean_C": wmean(Tm, cnt),
            f"{prefix}_cycle_duration_mean_s": wmean(t_cyc, cnt),
            f"{prefix}_cycle_duration_p95_s": _weighted_percentile(t_cyc, cnt, 95),

            # grid cycles (50 Hz ripple, duration < t_split)
            f"{prefix}_grid_cycles_per_h": cnt[grid].sum() / duration_h,
            f"{prefix}_grid_cycle_dT_mean_K": wmean(dT[grid], cnt[grid]),
            f"{prefix}_grid_cycle_dT_max_K": dT[grid].max() if grid.any() else np.nan,

            # load cycles (caused by load changes, duration >= t_split)
            f"{prefix}_load_cycles_per_h": cnt[load].sum() / duration_h,
            f"{prefix}_load_cycle_dT_mean_K": wmean(dT[load], cnt[load]),
            f"{prefix}_load_cycle_dT_max_K": dT[load].max() if load.any() else np.nan,
            f"{prefix}_load_cycle_Tmean_C": wmean(Tm[load], cnt[load]),
            f"{prefix}_load_cycle_duration_mean_s": wmean(t_cyc[load], cnt[load]),
        }

        # burst cycles (load cycles >= 5 K, heat-up removed)
        stats.update(_burst_cycle_statistics(dT, Tm, t_cyc, cnt, prefix, duration_h, t_split=t_split))
        return stats


    def build_thermal_characteristics(results_dir, warmup_s=0.0, dt=0.001):
        """Returns {scenario_name: {thermal response + thermal cycle statistics}}."""
        results_dir = Path(results_dir)
        swing = lambda x: np.percentile(x, 95) - np.percentile(x, 5)

        Thermal_characteristics = {}

        for sim in sorted(p for p in results_dir.iterdir() if p.is_dir()):
            thermal_dir = sim / "df_thermal"
            igbt_dir = sim / "df_lifetime_IGBT"
            diode_dir = sim / "df_lifetime_Diode"
            if not (thermal_dir.exists() and igbt_dir.exists() and diode_dir.exists()):
                continue

            # ---- 3. thermal response ----
            df = _read_chunks(thermal_dir, ["time", "Tj_igbt", "Tj_diode", "T_case"])
            duration_h = (df["time"].iloc[-1] - df["time"].iloc[0] + dt) / 3600
            df = df[df["time"] >= warmup_s]                     # optionally skip heat-up from ambient

            Tj_I = df["Tj_igbt"].to_numpy() - 273.15
            Tj_D = df["Tj_diode"].to_numpy() - 273.15
            T_c = df["T_case"].to_numpy() - 273.15

            result = {
                "Tj_IGBT_mean_C": Tj_I.mean(),
                "Tj_IGBT_max_C": Tj_I.max(),
                "Tj_IGBT_min_C": Tj_I.min(),
                "Tj_IGBT_swing_K": swing(Tj_I),
                "Tj_Diode_mean_C": Tj_D.mean(),
                "Tj_Diode_max_C": Tj_D.max(),
                "Tj_Diode_min_C": Tj_D.min(),
                "Tj_Diode_swing_K": swing(Tj_D),
                "T_case_mean_C": T_c.mean(),
                "T_case_swing_K": swing(T_c),
            }
            del df, Tj_I, Tj_D, T_c

            # ---- 4. thermal cycle statistics ----
            df_I = _read_chunks(igbt_dir, ["deltaT_igbt", "Tmean_igbt", "thermal_cycle_period_igbt", "count_igbt"])
            df_D = _read_chunks(diode_dir, ["deltaT_diode", "Tmean_diode", "thermal_cycle_period_diode", "count_diode"])

            result.update(_cycle_statistics(df_I, "igbt", "IGBT", duration_h))
            result.update(_cycle_statistics(df_D, "diode", "Diode", duration_h))
            del df_I, df_D

            Thermal_characteristics[sim.name] = result

        return Thermal_characteristics

    dictionary_master["Thermal_characteristics"] = build_thermal_characteristics(sims_dir)

    ###############################
    # Lifetime
    ###############################

    def _nf_eq(Nf, cnt):
        """Equivalent number of mission repetitions to failure (Miner's rule), same as miners_rule."""
        mask = (Nf > 0) & np.isfinite(Nf) & np.isfinite(cnt)
        D = np.sum(cnt[mask] / Nf[mask])
        return np.inf if D == 0 else 1.0 / D

    def _nf_results(df, dev, prefix, dT_split=10.0, t_split=0.1):
        """Nf results of one device from rainflow + LESIT results."""
        dT = df[f"deltaT_{dev}"].to_numpy()
        t_cyc = df[f"thermal_cycle_period_{dev}"].to_numpy()
        cnt = df[f"count_{dev}"].to_numpy()
        Nf = df[f"Nf_{dev}"].to_numpy()

        large = dT >= dT_split
        load = t_cyc >= t_split

        valid = (Nf > 0) & np.isfinite(Nf)
        worst = np.argmin(np.where(valid, Nf, np.inf)) if valid.any() else None

        return {
            f"{prefix}_Nf_eq": _nf_eq(Nf, cnt),
            f"{prefix}_Nf_eq_dT_ge10": _nf_eq(Nf[large], cnt[large]),
            f"{prefix}_Nf_eq_dT_lt10": _nf_eq(Nf[~large], cnt[~large]),
            f"{prefix}_Nf_eq_load_cycles": _nf_eq(Nf[load], cnt[load]),
            f"{prefix}_Nf_eq_grid_cycles": _nf_eq(Nf[~load], cnt[~load]),
            f"{prefix}_Nf_worst_cycle": Nf[worst] if worst is not None else np.nan,
            f"{prefix}_worst_cycle_dT_K": dT[worst] if worst is not None else np.nan,
            f"{prefix}_worst_cycle_Tmean_C": df[f"Tmean_{dev}"].to_numpy()[worst] - 273.15 if worst is not None else np.nan,
        }

    def build_nf_results(results_dir, input_step=0.02):
        """Returns {scenario_name: {Nf results and lifetimes in years}} for IGBT and diode."""
        results_dir = Path(results_dir)
        Nf_results = {}

        for sim in sorted(p for p in results_dir.iterdir() if p.is_dir()):
            igbt_dir = sim / "df_lifetime_IGBT"
            diode_dir = sim / "df_lifetime_Diode"
            elec_file = sim / "df_electrical" / "df.parquet"
            if not (igbt_dir.exists() and diode_dir.exists() and elec_file.exists()):
                continue

            # mission duration: one row per input step, as len(Is) * input_step in miners_rule
            mission_s = len(pd.read_parquet(elec_file, columns=["P"])) * input_step

            cols_I = ["deltaT_igbt", "Tmean_igbt", "thermal_cycle_period_igbt", "count_igbt", "Nf_igbt"]
            cols_D = ["deltaT_diode", "Tmean_diode", "thermal_cycle_period_diode", "count_diode", "Nf_diode"]
            df_I = _read_chunks(igbt_dir, cols_I)
            df_D = _read_chunks(diode_dir, cols_D)

            result = {"Mission_duration_s": mission_s}
            result.update(_nf_results(df_I, "igbt", "IGBT", mission_s))
            result.update(_nf_results(df_D, "diode", "Diode", mission_s))
            result["Limiting_device"] = "IGBT" if result["IGBT_Nf_eq"] <= result["Diode_Nf_eq"] else "Diode"

            # ---- lifetime as saved by mother_function (first row of the final files) ----
            final_I = pd.read_parquet(igbt_dir / "df_IGBT_final.parquet", columns=["lifetime_years_igbt_actual"]).iloc[0]
            final_D = pd.read_parquet(diode_dir / "df_Diode_final.parquet", columns=["lifetime_years_diode_actual"]).iloc[0]
            result["IGBT_lifetime_years_actual"] = float(final_I["lifetime_years_igbt_actual"])
            result["Diode_lifetime_years_actual"] = float(final_D["lifetime_years_diode_actual"])

            Nf_results[sim.name] = result
            del df_I, df_D

        return Nf_results

    dictionary_master["Nf_results"] = build_nf_results(sims_dir)

    ###############################
    # Dictionary Save
    ###############################

    def save_dictionary_master(dictionary_master, results_dir):
        results_dir = Path(results_dir)

        # ---- 1) JSON: the dictionary as it is ----
        def to_python(x):
            if isinstance(x, dict):
                return {k: to_python(v) for k, v in x.items()}
            if isinstance(x, (np.floating, float)):
                return None if not np.isfinite(x) else float(x)      # inf / nan -> null
            if isinstance(x, np.integer):
                return int(x)
            return x

        with open(results_dir / "dictionary_master.json", "w") as f:
            json.dump(to_python(dictionary_master), f, indent=2)

        # ---- 2) Excel: one sheet per section + one sheet with everything ----
        sections = {name: pd.DataFrame.from_dict(d, orient="index") for name, d in dictionary_master.items()}
        all_results = pd.concat(sections.values(), axis=1)
        all_results.index.name = "scenario"

        with pd.ExcelWriter(results_dir / "results_overview.xlsx") as writer:
            all_results.to_excel(writer, sheet_name="All_results")
            for name, df in sections.items():
                df.index.name = "scenario"
                df.to_excel(writer, sheet_name=name[:31])            # Excel sheet names max 31 chars

        return all_results

    all_results = save_dictionary_master(dictionary_master, results_dir)


files_load = {"H_100": "df_H_100_2MW.parquet", "B_200": "df_B_200_2MW.parquet"}
sims_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW\Dataframes"
results_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"
building(files_load, sims_dir, results_dir)

files_load = {"H_100": "df_H_100_norm.parquet", "B_200": "df_B_200_norm.parquet"}
sims_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm\Dataframes"
results_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm"
building(files_load, sims_dir, results_dir)

