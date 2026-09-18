
from pathlib import Path
import numpy as np
import pandas as pd

import json

base_dir_load = r"E:\IEEE_GM_2027\Dataset\Data_for_simulation"
files_load = {"H_100": "df_H_100_2MW.parquet", "B_200": "df_B_200_2MW.parquet"}
#files_load = {"H_100": "df_H_100_norm.parquet", "B_200": "df_B_200_norm.parquet"}
results_dir = r"E:\IEEE_GM_2027\IEEE_results\Results\2MW\Dataframes"
dictionary_master = {}

###############################
# Load
###############################

def load_characteristics(p, dt=0.02, hyst=0.1, min_freq=1/300):
    """Returns the load characteristics of one power profile p [W] as a dictionary."""
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

def build_load_characteristics(base_dir, files, until_s, dt=0.02):
    """Returns {scenario_name: {load characteristics}} for all chips and profiles."""
    Load_characteristics = {}
    for chip, file in files.items():
        df = pd.read_parquet(Path(base_dir) / chip / "Dataframes" / file)
        df = df[df["time_s"] < until_s]

        for col in df.columns.drop("time_s"):
            Load_characteristics[col] = {"chip": chip, "duration_s": len(df) * dt}
            Load_characteristics[col].update(load_characteristics(df[col].to_numpy(), dt=dt))

    return Load_characteristics

dictionary_master["Load_characteristics"] = build_load_characteristics(base_dir_load, files_load, until_s=3600)

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

dictionary_master["Electrical_characteristics"] = build_electrical_characteristics(results_dir)

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

def _cycle_statistics(df, dev, prefix, duration_h, t_split=0.1):
    """
    Thermal cycle statistics from rainflow results of one device.
    Cycles shorter than t_split [s] are grid cycles (50 Hz ripple),
    longer ones are load cycles (caused by load changes).
    """
    dT = df[f"deltaT_{dev}"].to_numpy()
    Tm = df[f"Tmean_{dev}"].to_numpy() - 273.15
    t_cyc = df[f"thermal_cycle_period_{dev}"].to_numpy()
    cnt = df[f"count_{dev}"].to_numpy()

    wmean = lambda x, w: np.sum(x * w) / w.sum() if w.sum() > 0 else np.nan
    band = lambda lo, hi: cnt[(dT >= lo) & (dT < hi)].sum() / duration_h

    load = t_cyc >= t_split
    grid = ~load

    return {
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

dictionary_master["Thermal_characteristics"] = build_thermal_characteristics(results_dir)

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

def build_nf_results(results_dir):
    """Returns {scenario_name: {Nf results}} for IGBT and diode."""
    results_dir = Path(results_dir)
    Nf_results = {}

    for sim in sorted(p for p in results_dir.iterdir() if p.is_dir()):
        igbt_dir = sim / "df_lifetime_IGBT"
        diode_dir = sim / "df_lifetime_Diode"
        if not (igbt_dir.exists() and diode_dir.exists()):
            continue

        cols_I = ["deltaT_igbt", "Tmean_igbt", "thermal_cycle_period_igbt", "count_igbt", "Nf_igbt"]
        cols_D = ["deltaT_diode", "Tmean_diode", "thermal_cycle_period_diode", "count_diode", "Nf_diode"]
        df_I = _read_chunks(igbt_dir, cols_I)
        df_D = _read_chunks(diode_dir, cols_D)

        result = {}
        result.update(_nf_results(df_I, "igbt", "IGBT"))
        result.update(_nf_results(df_D, "diode", "Diode"))
        result["Limiting_device"] = "IGBT" if result["IGBT_Nf_eq"] <= result["Diode_Nf_eq"] else "Diode"

        Nf_results[sim.name] = result
        del df_I, df_D

    return Nf_results

dictionary_master["Nf_results"] = build_nf_results(results_dir)

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

