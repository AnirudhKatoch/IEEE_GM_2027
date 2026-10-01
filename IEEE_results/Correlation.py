from matplotlib.colors import TwoSlopeNorm
import matplotlib.pyplot as plt
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy.signal import lfilter
from scipy.stats import spearmanr, kendalltau, skew, kurtosis

plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15, "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

SECTIONS = ("Load_characteristics", "Electrical_characteristics", "Thermal_characteristics")

###############################################
# Target factors
###############################################

def workload_damage(v, dev="IGBT"):
    """Workload-only damage per mission: heat-up half cycle removed (Eq. 8)."""
    nf, nw = v.get(f"{dev}_Nf_eq"), v.get(f"{dev}_Nf_worst_cycle")
    if not (nf and nw):
        return np.nan
    D = 1 / nf - 0.50 / nw
    return D if D > 0 else np.nan

def workload_damage_per_1e9h(v, dev="IGBT"):
    """Workload-only damage per 10^9 operating hours (scale of FIT figures), heat-up removed."""
    D = workload_damage(v, dev)                     # damage of one mission [-]
    mission_s = v.get("Mission_duration_s")
    if not np.isfinite(D) or not mission_s:
        return np.nan
    return D * (3600.0 / mission_s) * 1e9           # per hour -> per 10^9 hours

def inverter_lifetime(v, dev="IGBT", n_start_per_year=0.0):
    """
    Inverter lifetime in years from the workload-only damage (heat-up removed).

    D_wl             : damage of one simulated mission (e.g. 1 h), from workload_damage()
    n_start_per_year : start-stops per year (cold start -> operating temp. -> cold),
                       each counted as one full heat-up cycle (1/Nf_hu).
                       0 = converter runs continuously, never cools down.

    D_year = D_wl * missions_per_year + n_start_per_year / Nf_hu
    L      = 1 / D_year
    """
    D_wl = workload_damage(v, dev)
    mission_s = v.get("Mission_duration_s")
    if not np.isfinite(D_wl) or not mission_s:
        return np.nan

    missions_per_year = 365 * 24 * 3600 / mission_s
    D_year = D_wl * missions_per_year

    if n_start_per_year > 0:
        nw = v.get(f"{dev}_Nf_worst_cycle")          # heat-up cycle (worst cycle)
        if nw:
            D_year += n_start_per_year / nw

    return 1.0 / D_year if D_year > 0 else np.nan

def normal_damage(v, dev="IGBT"):
    """Total damage per mission: Miner's rule over all cycles, heat-up included."""
    nf = v.get(f"{dev}_Nf_eq")
    if not nf:
        return np.nan
    return 1 / nf

def load_pooled(sets, chips, target="workload_damage", dedup_cols=("P_mean_MW", "P_max_MW", "Swing_p95_p05_MW")):
    """
    Reads all sets, selects every scenario of the given chips, removes duplicate runs
    within each set and chip, and pools everything into one table per section.

    target = "workload_damage" : IGBT workload-only damage (heat-up removed, Eq. 8),
                                 relative to the least damaging pooled scenario (= 1)
    target = any key of Nf_results, e.g. "IGBT_Nf_eq" or "IGBT_lifetime_years_actual"
    """
    pooled = {s: [] for s in SECTIONS}
    y_parts = []

    for set_name, folder in sets.items():
        with open(Path(folder) / "dictionary_master.json", "r") as f:
            dm = json.load(f)

        load = pd.DataFrame.from_dict(dm["Load_characteristics"], orient="index")

        for chip in chips:
            keep = [s for s in load.index if f"_{chip}_" in s and s in dm["Nf_results"]]
            if not keep:
                print(f"[{set_name} | {chip}] no scenarios found")
                continue

            dup = load.loc[keep][list(dedup_cols)].round(6).duplicated()
            keep = list(dup[~dup].index)
            print(f"[{set_name} | {chip}] {len(keep)} unique | removed as duplicates: {list(dup[dup].index)}")

            label = lambda s: f"{set_name} | {s}"

            # ---- target ----
            #if target == "workload_damage":
            #    vals = {label(s): workload_damage(dm["Nf_results"][s]) for s in keep}   # heat-up removed
            #else:
            #    vals = {label(s): dm["Nf_results"][s].get(target) for s in keep}        # any Nf_results key


            if target == "workload_damage":
                vals = {label(s): workload_damage(dm["Nf_results"][s]) for s in keep}
            elif target == "inverter_lifetime":
                vals = {label(s): inverter_lifetime(dm["Nf_results"][s]) for s in keep}
            elif target == "normal_damage":
                vals = {label(s): normal_damage(dm["Nf_results"][s]) for s in keep}
            elif target == "workload_damage_per_1e9h":
                vals = {label(s): workload_damage_per_1e9h(dm["Nf_results"][s]) for s in keep}
            else:
                vals = {label(s): dm["Nf_results"][s].get(target) for s in keep}

            y_parts.append(pd.Series(vals, dtype=float))

            for section in SECTIONS:
                df = pd.DataFrame.from_dict(dm[section], orient="index").reindex(keep)
                df.index = [label(s) for s in df.index]
                pooled[section].append(df)

    y = pd.concat(y_parts).replace([np.inf, -np.inf], np.nan)
    if target == "workload_damage":
        y = y / y.min()                                           # damage ratio: least damaging = 1
    tables = {s: pd.concat(parts) for s, parts in pooled.items()}
    print(f"\nTarget: {target} | {len(y)} scenarios pooled")
    return tables, y

def rank_characteristics(tables, y, top=15, exclude=("Diode",), save_path=None):
    """Spearman rho and Kendall tau of every characteristic with y, per section. Prints the top N."""
    results = {}
    for section, df in tables.items():
        rows = []
        for c in df.columns:
            if any(e in c for e in exclude):
                continue
            x = pd.to_numeric(df[c], errors="coerce").replace([np.inf, -np.inf], np.nan)
            m = x.notna() & y.notna()
            if m.sum() < 4 or x[m].round(9).nunique() < 2:           # too few points or constant
                continue
            rho, p_rho = spearmanr(x[m], y[m])
            tau, p_tau = kendalltau(x[m], y[m])
            p = max(p_rho, p_tau)                                     # significant only if both agree
            rows.append({"characteristic": c, "n": int(m.sum()),
                         "spearman_rho": rho, "p_spearman": p_rho,
                         "kendall_tau": tau, "p_kendall": p_tau,
                         "significant": "p<0.01" if p < 0.01 else ("p<0.05" if p < 0.05 else "-")})

        out = pd.DataFrame(rows)
        out["consensus_rank"] = (out["spearman_rho"].abs().rank(ascending=False)
                                 + out["kendall_tau"].abs().rank(ascending=False)) / 2
        out = out.sort_values("consensus_rank").reset_index(drop=True)
        out.index += 1
        out.index.name = "rank"
        results[section] = out

        print(f"\n===== {section}: top {top} of {len(out)} =====")
        print(out.head(top)[["characteristic", "n", "spearman_rho", "kendall_tau", "significant"]]
              .round(3).to_string())

    if save_path is not None:
        combined = pd.concat({s.replace("_characteristics", ""): out for s, out in results.items()},
                             names=["stage", "rank"]).reset_index()
        with pd.ExcelWriter(save_path) as writer:
            combined.round(4).to_excel(writer, sheet_name="All", index=False)  # all stages in one sheet
            for section, out in results.items():
                out.round(4).to_excel(writer, sheet_name=section[:31])  # plus one sheet per stage
    return results

##########################
# For running
##########################

GRID_COLS = [
    "Max_change_in_5s_MW",                  # ERCOT / MISO / ATC
    "Max_change_in_0.1s_MW",                # AESO draft
    "Swing_avg_4s_MW",                      # SCADA
    "Swing_avg_60s_MW",                     # 1-min resolution
    "Swing_avg_300s_MW",                    # 5-min dispatch
    "Ramp_max_MW_per_min",                  # AESO / MISO / ATC ramp limits
    "ERCOT_changes_gt25pct_in_5s_per_h",    # ERCOT repetition
    "LIPA_band_5_23.75Hz_amp_10s_MW",       # LIPA
    "SoCo_band_0.1_0.5Hz_amp_60s_MW",       # Southern Company
    "SoCo_band_0.5_0.8Hz_amp_60s_MW",
    "SoCo_band_0.8_2Hz_amp_60s_MW",
    "Flicker_Pst_max_SCR20",  # IEC 61000-4-15 / IEEE 1453
    "Peak_demand_15min_MW",  # metering / demand charge
    "Load_factor_15min",  # metering
    "Variability_1min_std_MW",  # balancing / regulation
]
SKIP_PREFIXES = ("chip", "duration_s", "Seam_jump", "Startup_", "Var_share_")   # metadata, artefacts, old shares
ELEC_COLS  = ["P_loss_IGBT_swing_W", "I_IGBT_rms_A", "P_loss_IGBT_mean_W"]
THERM_COLS = ["IGBT_burst_dT_eq_K", "IGBT_burst_Tmean_C", "IGBT_burst_duration_mean_s"]

def build_sections(tables):
    load = tables["Load_characteristics"]
    grid = [c for c in GRID_COLS if c in load.columns]
    proposed = [c for c in load.columns
                if c not in grid and not c.startswith(SKIP_PREFIXES)]

    return {
        "Proposed_metrics":           load[proposed],
        "Grid_operator_metrics":      load[grid],
        "Electrical_characteristics": tables["Electrical_characteristics"][ELEC_COLS],
        "Thermal_characteristics":    tables["Thermal_characteristics"][THERM_COLS],
    }

chips = ("B200", "H100")
sets = {"norm": r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm",
        "2MW":  r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"}


save_dir = Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2\Correlations")
save_dir.mkdir(parents=True, exist_ok=True)

target = "normal_damage"   # or "workload_damage", "inverter_lifetime", "IGBT_Nf_eq", "IGBT_lifetime_years_actual"

tables, y = load_pooled(sets, chips, target=target)

results = rank_characteristics(build_sections(tables), y, top=100, exclude=(),
                               save_path=save_dir / f"ranking_{target}_pooled_{'_'.join(chips)}.xlsx")

# ---- save the printed rankings as one CSV ----
csv_path = save_dir / f"ranking_{target}_pooled_{'_'.join(chips)}.csv"
pd.concat(results, names=["section"]).to_csv(csv_path, sep=";")


"""
Search for the pure LOAD property that best ranks the normal (total) Miner damage.

Input  : active-power profiles, first 15 min at 20 ms (45 000 samples), taken from the simulation parquet files
Target : normal damage per mission = 1 / IGBT_Nf_eq (all cycles, heat-up included), from dictionary_master.json
Output : ranking of every load metric (pooled, per set, per chip) printed and saved as CSV + Excel

Only the power signal is used - no converter, loss or temperature data.
Rank correlations (Spearman rho, Kendall tau) are used, so units and scaling do not matter.
"""


# =====================================================================================================
# Settings
# =====================================================================================================

DATA = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")

RESULTS = {  # set -> folder that contains dictionary_master.json
    "norm": Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm"),
    "2MW":  Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"),
}

FILES = {  # set -> {chip: parquet file relative to DATA}
    "norm": {"H100": "H_100/Dataframes/df_H_100_norm.parquet", "B200": "B_200/Dataframes/df_B_200_norm.parquet"},
    "2MW":  {"H100": "H_100/Dataframes/df_H_100_2MW.parquet",  "B200": "B_200/Dataframes/df_B_200_2MW.parquet"},
}

CHIPS = ("B200", "H100")                       # remove one to analyse a single chip
OUT_DIR = Path(r"E:\IEEE_GM_2027\IEEE_results\Figures")

DT = 0.02                                      # [s] profile resolution
WINDOW_S = 900.0                               # [s] length of the profile used (15 min)
P_RATED_MW = 2.0                               # [MW] converter rating, only for %-of-rating thresholds

# default runs that appear in several sweeps (identical profiles) -> keep only one copy
DUPLICATES = ("ImageSize_32", "ModelSize_128", "Deepspeedds_z3", "Lamma_8B", "SeqLength_2048")


# =====================================================================================================
# Target
# =====================================================================================================

def normal_damage(v, dev="IGBT"):
    """Total damage per mission: Miner's rule over all cycles, heat-up included."""
    nf = v.get(f"{dev}_Nf_eq")
    return 1.0 / nf if nf else np.nan


# =====================================================================================================
# Load metrics (pure power-signal properties)
# =====================================================================================================

def load_metrics(p, dt=DT, P_rated=P_RATED_MW):
    """All candidate load properties of one power profile p [MW]."""
    p = np.asarray(p, dtype=float)
    n = len(p)
    s, s2 = pd.Series(p), pd.Series(p ** 2)
    mean, std = p.mean(), p.std()
    rms = np.sqrt(np.mean(p ** 2))
    out = {}

    # ---- A) level ----
    out["A_mean"] = mean
    out["A_median"] = np.median(p)
    out["A_min"] = p.min()
    out["A_max"] = p.max()
    out["A_energy_MWh"] = p.sum() * dt / 3600

    # ---- B) power means of order k (k=1 mean, k=2 RMS, k->inf max) ----
    for k in (0.5, 1.5, 2, 2.5, 3, 4, 6, 8):
        out[f"B_power_mean_k{k:g}"] = np.mean(p ** k) ** (1 / k)

    # ---- C) moments and level + fluctuation combinations (RMS^2 = mean^2 + var) ----
    out["C_std"] = std
    out["C_cv"] = std / mean
    out["C_skewness"] = skew(p)
    out["C_kurtosis"] = kurtosis(p)
    for lam in (0.25, 0.5, 2, 4, 8):
        out[f"C_sqrt(mean^2+{lam:g}var)"] = np.sqrt(mean ** 2 + lam * std ** 2)
    for c in (0.5, 1, 2, 3):
        out[f"C_mean+{c:g}std"] = mean + c * std

    # ---- D) percentiles and load duration curve ----
    for q in (50, 75, 90, 95, 99, 99.9):
        out[f"D_P{q:g}"] = np.percentile(p, q)
    for thr in (0.25, 0.4, 0.5, 0.6, 0.75):
        x = thr * P_rated
        out[f"D_time_above_{thr * 100:g}pct_rating"] = 100 * np.mean(p > x)
        out[f"D_energy_above_{thr * 100:g}pct_rating_MWh"] = np.sum(np.clip(p - x, 0, None)) * dt / 3600

    # ---- E) tails: mean of the highest x % of samples, upper semi-deviation ----
    ps = np.sort(p)[::-1]
    for frac in (0.01, 0.05, 0.10, 0.25, 0.50):
        out[f"E_mean_of_top_{frac * 100:g}pct"] = ps[:max(1, int(frac * n))].mean()
    usd = np.sqrt(np.mean(np.clip(p - mean, 0, None) ** 2))
    out["E_upper_semi_std"] = usd
    out["E_mean+upper_semi_std"] = mean + usd

    # ---- F) sliding windows: highest average and highest RMS over window w ----
    for w in (0.1, 1, 5, 10, 30, 60, 120, 180, 300, 600):
        k = max(int(round(w / dt)), 1)
        ma = s.rolling(k).mean()
        mr = np.sqrt(s2.rolling(k).mean())
        out[f"F_max_avg_{w:g}s"] = ma.max()
        out[f"F_max_rms_{w:g}s"] = mr.max()
        out[f"F_p95_rms_{w:g}s"] = mr.quantile(0.95)

    # ---- G) sustained peak: highest level held for at least w seconds ----
    for w in (0.2, 1, 5, 30, 60, 180):
        k = max(int(round(w / dt)), 1)
        out[f"G_sustained_peak_{w:g}s"] = s.rolling(k).min().max()

    # ---- H) exponential memory (first-order filter, starts at zero), peak of p and of p^2 ----
    for tau in (1, 3, 10, 30, 60, 180, 300):
        a = np.exp(-dt / tau)
        out[f"H_exp_peak_tau{tau:g}s"] = lfilter([1 - a], [1, -a], p).max()
        out[f"H_exp_rms_peak_tau{tau:g}s"] = np.sqrt(lfilter([1 - a], [1, -a], p ** 2).max())

    # ---- I) swings and changes ----
    p05, p95 = np.percentile(p, [5, 95])
    out["I_swing_p95_p05"] = p95 - p05
    out["I_max_minus_min"] = p.max() - p.min()
    for w in (0.1, 1, 5, 60):
        k = max(int(round(w / dt)) + 1, 2)
        out[f"I_max_change_{w:g}s"] = (s.rolling(k).max() - s.rolling(k).min()).max()
    k = int(round(1 / dt)); m = n // k
    wnd = p[: m * k].reshape(m, k)
    sw = np.percentile(wnd, 95, axis=1) - np.percentile(wnd, 5, axis=1)
    out["I_swing1s_max"] = sw.max()
    out["I_swing1s_mean"] = sw.mean()
    out["I_swing1s_max_x_rms"] = (sw * np.sqrt((wnd ** 2).mean(axis=1))).max()

    # ---- J) combinations of level and shape ----
    out["J_rms_x_(1+cv)"] = rms * (1 + std / mean)
    out["J_mean_x_max"] = mean * p.max()
    out["J_rms_x_max"] = rms * p.max()
    out["J_rms_x_swing"] = rms * (p95 - p05)
    out["J_rms+0.5swing"] = rms + 0.5 * (p95 - p05)
    out["J_rms_x_P95"] = rms * p95

    # ---- K) timing (expected to be irrelevant, kept as reference) ----
    mid = p05 + 0.5 * (p95 - p05)
    high = (p > mid).astype(int)
    out["K_duty_above_mid_pct"] = 100 * high.mean()
    out["K_transitions_per_h"] = np.count_nonzero(np.diff(high)) / (n * dt / 3600)
    out["K_peak_to_mean"] = p.max() / mean
    out["K_ramp_p99_MW_per_s"] = np.percentile(np.abs(np.diff(p)) / dt, 99)

    return out


# =====================================================================================================
# Ranking
# =====================================================================================================

def rank_metrics(X, y, meta):
    """Spearman rho and Kendall tau of every metric with y: pooled, per set and per chip."""
    subsets = {f"{col}={v}": meta[col] == v for col in ("set", "chip") for v in meta[col].unique()}
    rows = []
    for c in X.columns:
        x = pd.to_numeric(X[c], errors="coerce").replace([np.inf, -np.inf], np.nan)
        m = x.notna() & y.notna()
        if m.sum() < 5 or x[m].round(12).nunique() < 2:
            continue
        r = {"family": c.split("_")[0], "metric": c, "n": int(m.sum()),
             "rho": spearmanr(x[m], y[m])[0], "tau": kendalltau(x[m], y[m])[0]}
        for name, sel in subsets.items():
            mm = m & sel
            if mm.sum() >= 5 and x[mm].round(12).nunique() > 1:
                r[f"tau[{name}]"] = kendalltau(x[mm], y[mm])[0]
        sub_taus = [v for k, v in r.items() if k.startswith("tau[")]
        r["tau_worst_subset"] = min(sub_taus) if sub_taus else np.nan     # robustness: weakest subset
        rows.append(r)
    out = pd.DataFrame(rows).sort_values(["tau", "rho"], ascending=False).reset_index(drop=True)
    out.index += 1
    out.index.name = "rank"
    return out


# =====================================================================================================
# Run
# =====================================================================================================

if __name__ == "__main__":
    n_keep = int(round(WINDOW_S / DT))
    X_rows, y_vals, meta = {}, {}, {}

    for set_name, chip_files in FILES.items():
        with open(RESULTS[set_name] / "dictionary_master.json") as f:
            nf = json.load(f)["Nf_results"]

        for chip, fpath in chip_files.items():
            if chip not in CHIPS:
                continue
            df = pd.read_parquet(DATA / fpath).iloc[:n_keep]             # first 15 min
            used = 0
            for col in df.columns.drop("time_s"):
                if col.endswith(DUPLICATES) or col not in nf:
                    continue
                lbl = f"{set_name} | {col}"
                X_rows[lbl] = load_metrics(df[col].to_numpy() / 1e6)
                y_vals[lbl] = normal_damage(nf[col])
                meta[lbl] = {"set": set_name, "chip": chip}
                used += 1
            print(f"[{set_name} | {chip}] {used} scenarios, {len(df)} samples = {len(df) * DT:.0f} s")
            del df

    X = pd.DataFrame.from_dict(X_rows, orient="index")
    y = pd.Series(y_vals, dtype=float)
    M = pd.DataFrame.from_dict(meta, orient="index")
    print(f"\n{len(y)} scenarios | {X.shape[1]} load metrics | target: normal damage (1 / IGBT_Nf_eq)\n")

    res = rank_metrics(X, y, M)

    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 20)
    print("===== Top 40 (sorted by pooled Kendall tau) =====")
    print(res.head(40).round(3).to_string())

    print("\n===== Best metric per family =====")
    print(res.groupby("family", sort=False).head(1).round(3).to_string())

    print("\n===== Reference: RMS power (k = 2) =====")
    print(res[res["metric"] == "B_power_mean_k2"].round(3).to_string())

    CORR_DIR = Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2\Correlations")
    CORR_DIR.mkdir(parents=True, exist_ok=True)
    res.to_csv(CORR_DIR / "load_metric_search_normal_damage.csv", sep=";")
    with pd.ExcelWriter(CORR_DIR / "load_metric_search_normal_damage.xlsx") as writer:
        res.round(4).to_excel(writer, sheet_name="ranking")
        X.assign(normal_damage=y).join(M).to_excel(writer, sheet_name="metric_values")
    print(f"\nSaved to {CORR_DIR}")


def downsample(p, dt_in, dt_out, method="mean"):
    """Profile at resolution dt_out: 'mean' = block average (like a meter), 'sample' = every k-th value."""
    k = int(round(dt_out / dt_in))
    if k <= 1:
        return p
    n = len(p) // k * k
    return p[:n].reshape(-1, k).mean(axis=1) if method == "mean" else p[:n:k]

def resolution_study(resolutions_s=(0.02, 0.1, 0.2, 0.5, 1, 2, 5, 10, 30, 60),lam=0.5, method="mean", save_name="resolution_study_effective_level"):
    """
    Kendall tau / Spearman rho of the effective level sqrt(mean^2 + lam*var) with the normal damage,
    computed from profiles down-sampled to each resolution. Mean and RMS power shown as references.
    """
    n_keep = int(round(WINDOW_S / DT))
    profiles, y, meta = {}, {}, {}
    for set_name, chip_files in FILES.items():
        with open(RESULTS[set_name] / "dictionary_master.json") as f:
            nf = json.load(f)["Nf_results"]
        for chip, fpath in chip_files.items():
            if chip not in CHIPS:
                continue
            df = pd.read_parquet(DATA / fpath).iloc[:n_keep]
            for col in df.columns.drop("time_s"):
                if col.endswith(DUPLICATES) or col not in nf:
                    continue
                lbl = f"{set_name} | {col}"
                profiles[lbl] = df[col].to_numpy() / 1e6
                y[lbl] = normal_damage(nf[col])
                meta[lbl] = set_name
            del df
    y = pd.Series(y)
    sets = pd.Series(meta)

    metrics = {
        f"Effective level (λ={lam:g})": lambda p: np.sqrt(p.mean() ** 2 + lam * p.var()),
        "RMS power":                     lambda p: np.sqrt(np.mean(p ** 2)),
        "Mean power":                    lambda p: p.mean(),
    }

    rows = []
    for res in resolutions_s:
        for name, f in metrics.items():
            x = pd.Series({k: f(downsample(p, DT, res, method)) for k, p in profiles.items()})
            r = {"resolution_s": res, "metric": name,
                 "rho": spearmanr(x, y)[0], "tau": kendalltau(x, y)[0]}
            for s in sets.unique():                                   # per set (2MW / norm)
                m = sets == s
                r[f"tau[{s}]"] = kendalltau(x[m], y[m])[0] if x[m].round(12).nunique() > 1 else np.nan
            rows.append(r)
    out = pd.DataFrame(rows)

    pd.set_option("display.width", 200)
    print(out.round(3).to_string(index=False))

    # ---- plot: tau vs resolution ----
    fig, ax = plt.subplots(figsize=(6.4, 4.8 * 0.75))
    for (name, g), mk in zip(out.groupby("metric", sort=False), ("o", "s", "^")):
        ax.plot(g["resolution_s"], g["tau"], marker=mk, lw=1.5, label=name)
    ax.set_xscale("log")
    ax.set_xlabel("Data resolution (s)")
    ax.set_ylabel("Kendall τ with damage (–)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / f"{save_name}.png", dpi=600, bbox_inches="tight")
    plt.close(fig)
    return out

#res_table = resolution_study()



#########################################################################################################################
#Plotting Heat map
#########################################################################################################################

CORR_DIR = Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2\Correlations")
FIG_DIR = Path(r"E:\IEEE_GM_2027\IEEE_results\Figures")

PROPOSED = "C_sqrt(mean^2+0.5var)"

# block label (right side, None = no label) -> (source, rows to take: None = all)
# source "search" = load_metric_search CSV (P_eff, RMS, mean), otherwise a section of the ranking CSV
BLOCKS = [
    (None,           ("search", [PROPOSED])),
    ("Reference",  ("search", ["B_power_mean_k2", "A_mean"])),      # optional: RMS and mean power
    ("Grid metrics", ("Grid_operator_metrics", None)),
    #("Thermal",      ("Thermal_characteristics", None)),
]

LABELS = {
    # proposed and references
    "C_sqrt(mean^2+0.5var)":             r"Effective level $P_\mathrm{eff}$ (proposed)",
    #"B_power_mean_k2":                   "RMS power",
    #"A_mean":                            "Mean power",
    # grid-operator rules
    "Max_change_in_5s_MW":               "Max. power change in 5 s (ERCOT/MISO/ATC)",
    "SoCo_band_0.1_0.5Hz_amp_60s_MW":    "Oscillation amplitude, 0.1–0.5 Hz (Southern Co.)",
    "SoCo_band_0.5_0.8Hz_amp_60s_MW":    "Oscillation amplitude, 0.5–0.8 Hz (Southern Co.)",
    "SoCo_band_0.8_2Hz_amp_60s_MW":      "Oscillation amplitude, 0.8–2 Hz (Southern Co.)",
    "Swing_avg_4s_MW":                   "Power swing of 4 s averages (SCADA)",
    "Max_change_in_0.1s_MW":             "Max. power change in 0.1 s (AESO draft)",
    "LIPA_band_5_23.75Hz_amp_10s_MW":    "Oscillation amplitude, 5–25 Hz (LIPA)",
    "Ramp_max_MW_per_min":               "Max. ramp rate per min (AESO/MISO/ATC)",
    "Swing_avg_60s_MW":                  "Power swing of 1 min averages",
    "Swing_avg_300s_MW":                 "Power swing of 5 min averages (dispatch)",
    "ERCOT_changes_gt25pct_in_5s_per_h": "Count of 5 s changes > 25 % (ERCOT)",
    "Flicker_Pst_max_SCR20": "Flicker severity Pst (IEC 61000-4-15)",
    #"Peak_demand_15min_MW": "15 min peak demand (metering)",
    #"Load_factor_15min": "Load factor, 15 min (metering)",
    #"Variability_1min_std_MW": "1 min power variability (balancing)",


    # thermal
    #"IGBT_burst_dT_eq_K":                "Junction temperature swing per burst",
    #"IGBT_burst_Tmean_C":                "Mean junction temperature per burst",
    #"IGBT_burst_duration_mean_s":        "Heating time per burst",

}


def plot_correlation_heatmap(ranking_csv="ranking_normal_damage_pooled_B200_H100.csv",
                             search_csv="load_metric_search_normal_damage.csv",
                             corr_dir=CORR_DIR, fig_dir=FIG_DIR,
                             figsize=(6.4, 4.8 * 1.5), gap=0.25,
                             cbar_label="Correlation with damage",
                             file_name="heatmap_correlation_Peff"):
    """
    Single-column heat map: proposed metric P_eff on top, then the grid-operator rule metrics,
    then the thermal quantities, separated by white space; each block ordered by |rho| (then |tau|).
    P_eff comes from the load-metric search CSV, the other blocks from the ranking CSV.
    Columns = Spearman rho and Kendall tau.
    """
    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)

    # ---- both CSVs into one table with the same columns ----
    rank = pd.read_csv(Path(corr_dir) / ranking_csv, sep=";")
    search = pd.read_csv(Path(corr_dir) / search_csv, sep=";")
    search = search.rename(columns={"metric": "characteristic", "rho": "spearman_rho", "tau": "kendall_tau"})
    search["section"] = "search"
    df = pd.concat([rank[["section", "characteristic", "spearman_rho", "kendall_tau"]],
                    search[["section", "characteristic", "spearman_rho", "kendall_tau"]]],
                   ignore_index=True)

    # ---- rows per block ----
    # ---- rows per block: only characteristics listed in LABELS are shown ----
    groups = []
    for label, (section, keep) in BLOCKS:
        t = df[df["section"] == section]
        t = t[t["characteristic"].isin(LABELS.keys())]           # commented out in LABELS -> hidden
        if keep is not None:
            t = t[t["characteristic"].isin(keep)]
        t = t.assign(a_rho=t["spearman_rho"].abs(), a_tau=t["kendall_tau"].abs()) \
             .sort_values(["a_rho", "a_tau"], ascending=False)
        if len(t):
            groups.append((label, t["characteristic"].tolist(),
                           t[["spearman_rho", "kendall_tau"]].to_numpy()))
        else:
            print(f"Block '{label}' ({section}): no rows found")

    # ---- layout: blocks with white spacer rows in between ----
    ratios = []
    for i, (_, rows, _) in enumerate(groups):
        ratios.append(len(rows))
        if i < len(groups) - 1:
            ratios.append(gap)
    fig, axs = plt.subplots(len(ratios), 1, figsize=figsize,
                            gridspec_kw={"height_ratios": ratios, "hspace": 0.0})
    axs = np.atleast_1d(axs)
    for ax in axs[1::2]:                                         # spacer axes
        ax.axis("off")
    axes = axs[::2]

    norm = TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)

    for k, (ax, (label, rows, block)) in enumerate(zip(axes, groups)):
        im = ax.imshow(block, cmap="RdBu_r", norm=norm, aspect="auto")

        for i in range(len(rows)):
            for j in range(2):
                v = block[i, j]
                ax.text(j, i, f"{v:.3f}", ha="center", va="center",
                        color="white" if abs(v) > 0.6 else "black")

        ax.set_yticks(range(len(rows)))
        ax.set_yticklabels([LABELS.get(r, r) for r in rows])
        for lbl, r in zip(ax.get_yticklabels(), rows):
            if r == PROPOSED:
                lbl.set_fontweight("bold")

        ax.set_xticks([0, 1])
        if k == 0:
            ax.xaxis.tick_top()
            ax.tick_params(labeltop=True, labelbottom=False)
            ax.set_xticklabels(["Spearman ρ (rank correlation)", "Kendall τ (pair agreement)"])
        else:
            ax.tick_params(labelbottom=False, labeltop=False)
        ax.tick_params(length=0, pad=4)

        if label:
            ax.text(1.58, (len(rows) - 1) / 2, label, rotation=270, va="center", ha="center", clip_on=False)

        ax.set_xticks([-0.5, 0.5, 1.5], minor=True)
        ax.set_yticks(np.arange(-0.5, len(rows)), minor=True)
        ax.grid(which="minor", color="white", lw=1.2)
        ax.tick_params(which="minor", length=0)

    n_last = len(groups[-1][1])
    cax = axes[-1].inset_axes([0.0, -0.9 / n_last, 1.0, 0.25 / n_last])
    cbar = fig.colorbar(im, cax=cax, orientation="horizontal")
    cbar.ax.tick_params(length=3, pad=2)
    cbar.set_label(cbar_label, labelpad=2)

    fig.savefig(fig_dir / f"{file_name}.png", dpi=600, bbox_inches="tight")
    plt.close(fig)


plot_correlation_heatmap()
