import re
from matplotlib.patches import Patch
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.stats import spearmanr, kendalltau
from matplotlib.ticker import FuncFormatter, LogLocator


plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15, "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

#########################################################################################################################
# Plotting different characteristics from dictionary
#########################################################################################################################

def plotting(base_dir,figures_dir,file_name):


    # ---- load dictionary_master ----
    with open(Path(base_dir) / file_name) as f:
        dictionary_master = json.load(f)

    # sweep -> (prefix of scenario names in dictionary, label on x axis, colormap)
    # all scenarios starting with the prefix are found automatically and sorted low -> high by their number
    GROUPS = {
        "Image batch size": ("Image_B200_BatchSize_", "Image\nBatch size", "Blues"),
        "Image size":       ("Image_B200_ImageSize_", "Image\nImage size", "Blues"),
        "Image model size": ("Image_B200_ModelSize_", "Image\nModel size", "Blues"),
        "LLM batch size":   ("Text_B200_BatchSize",   "LLM\nBatch size",   "Oranges"),
        "LLM model size":   ("Text_B200_Lamma_",      "LLM\nModel size",   "Oranges"),
        "LLM seq. length":  ("Text_B200_SeqLength_",  "LLM\nSeq. length",  "Oranges"),
        # "LLM ZeRO stage": ("Text_B200_Deepspeedds_z", "LLM\nZeRO stage", "Oranges"),  # Z3 = Llama 8B
    }

    def _find_members(section):
        """Scenarios of each sweep in the dictionary section, sorted low -> high."""
        number = lambda name, prefix: float(re.search(r"\d+", name[len(prefix):]).group())
        members = {}
        for g, (prefix, _, _) in GROUPS.items():
            members[g] = sorted((s for s in section if s.startswith(prefix)), key=lambda s: number(s, prefix))
            if not members[g]:
                print(f"No scenarios found for '{g}' (prefix {prefix})")
        return members
    def _grouped_bar_plot(section, members, key, ylabel, save_path, log=False):
        """One grouped bar chart: one group per sweep, one thin bar per setting (light = low, dark = high)."""
        n_max = max(len(m) for m in members.values())
        width = 0.8 / n_max
        x = np.arange(len(GROUPS))

        # x axis label: sweep name + tested values, e.g. "Image\nBatch size\n128 | 256 | 512"
        xlabels = []
        for g, (prefix, label, _) in GROUPS.items():
            xlabels.append(f"{label}\n" + " | ".join(s[len(prefix):].lstrip("_") for s in members[g]))

        fig, ax = plt.subplots(figsize=(11, 5))
        plotted = []

        for i, (g, (_, _, cmap)) in enumerate(GROUPS.items()):
            m = members[g]
            shades = plt.get_cmap(cmap)(np.linspace(0.35, 0.9, max(len(m), 1)))
            for j, s in enumerate(m):
                v = section.get(s, {}).get(key)
                v = np.nan if v is None else float(v)                          # JSON null -> NaN
                if not np.isfinite(v) or (log and v <= 0):
                    v = np.nan
                else:
                    plotted.append(v)
                pos = x[i] + (j - (len(m) - 1) / 2) * width
                ax.bar(pos, v, width, color=shades[j], edgecolor="black", linewidth=0.8)

        # legend: shade = setting level
        grey = plt.get_cmap("Greys")(np.linspace(0.35, 0.9, n_max))
        level = ["Low", "Moderate", "High"] if n_max == 3 else [f"Setting {k + 1}" for k in range(n_max)]
        ax.legend(handles=[Patch(facecolor=grey[k], edgecolor="black", label=level[k]) for k in range(n_max)],
                  loc="upper left", ncol=n_max, frameon=False, fontsize=12)

        ax.set_xticks(x)
        ax.set_xticklabels(xlabels, fontsize=12)
        ax.set_ylabel(ylabel)

        if plotted:
            if log:
                ax.set_yscale("log")
                ax.set_ylim(min(plotted) / 10, max(plotted) * 100)         # room for legend
            else:
                ax.set_ylim(0, max(plotted) * 1.2 if max(plotted) > 0 else 1)

        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        fig.tight_layout()
        fig.savefig(save_path, dpi=300)
        plt.close(fig)
    def Load_characteristics_plotting(dictionary_master, figures_dir):
        """Grouped bar charts of load characteristics. Saved in figures_dir/Load_characteristics."""

        characteristics = {
            "P_mean_MW": "Mean power (MW)",
            "P_max_MW": "Maximum power (MW)",
            "P_min_MW": "Minimum power (MW)",
            # "Energy_MWh":            "Energy (MWh)",               # = P_mean for 1 h window
            "Peak_to_mean": "Peak-to-mean ratio (-)",
            "Swing_p95_p05_MW": "Power swing p95-p05 (MW)",
            "Swing_p95_p05_avg1s_MW": "Power swing p95-p05, 1 s resolution (MW)",  # main metric for the paper
            "Power_cycle_dP_max_MW": "Largest power cycle (MW)",  # ≈ P_max − P_min
            "Time_at_high_load_pct": "Time at high load (%)",
            "Dominant_period_s": "Dominant period (s)",
            "Transitions_per_h": "Load transitions (1/h)",
            "Ramp_p99_MW_per_s": "Ramp rate p99 (MW/s)",
            "Step_height_MW": "Step height (MW)",
            "Dwell_high_mean_s": "Mean high-load dwell (s)",
            "Damage_proxy_per_h": "Damage proxy (1/h)",
            "Max_change_in_1s_MW": "Max. change within 1 s (MW)",
            "Max_change_in_5s_MW": "Max. change within 5 s (MW)",
            "Swing_avg_60s_MW": "Swing after 1-min averaging (MW)",
        }

        save_dir = Path(figures_dir) / "Load_characteristics"
        save_dir.mkdir(parents=True, exist_ok=True)

        load = dictionary_master.get("Load_characteristics", dictionary_master)
        members = _find_members(load)

        for key, ylabel in characteristics.items():
            _grouped_bar_plot(load, members, key, ylabel, save_dir / f"{key}.png")

        print(f"Saved {len(characteristics)} figures to {save_dir}")

    def Electrical_characteristics_plotting(dictionary_master, figures_dir):
        """Grouped bar charts of electrical characteristics. Saved in figures_dir/Electrical_characteristics."""

        characteristics = {
            "I_IGBT_rms_A": "IGBT RMS current (A)",
            # "I_IGBT_peak_A": "IGBT peak current (A)",
            "I_Diode_rms_A": "Diode RMS current (A)",                 # fixed fraction of IGBT RMS current
            # "I_Diode_peak_A": "Diode peak current (A)",               # fixed fraction of IGBT peak current
            "P_loss_IGBT_mean_W": "IGBT mean loss (W)",
            # "P_loss_IGBT_max_W": "IGBT max loss (W)",
            "P_loss_IGBT_swing_W": "IGBT loss swing p95-p05 (W)",
            "P_loss_Diode_mean_W": "Diode mean loss (W)",             # ~fixed fraction of IGBT mean loss
            # "P_loss_Diode_max_W": "Diode max loss (W)",               # ~fixed fraction of IGBT max loss
            "P_loss_Diode_swing_W": "Diode loss swing p95-p05 (W)",   # ~fixed fraction of IGBT loss swing
            # "Switching_share_pct": "Switching loss share (%)",
            # "Diode_share_pct": "Diode loss share (%)",                # constant ~7.7 % (set by M and pf)
            # "Loss_ratio_pct": "Switch losses / load power (%)",
        }

        save_dir = Path(figures_dir) / "Electrical_characteristics"
        save_dir.mkdir(parents=True, exist_ok=True)

        elec = dictionary_master.get("Electrical_characteristics", dictionary_master)
        members = _find_members(elec)

        for key, ylabel in characteristics.items():
            _grouped_bar_plot(elec, members, key, ylabel, save_dir / f"{key}.png")

        print(f"Saved {len(characteristics)} figures to {save_dir}")
    def Thermal_characteristics_plotting(dictionary_master, figures_dir):
        """Grouped bar charts of thermal characteristics. Saved in figures_dir/Thermal_characteristics."""

        # thermal response -> y axis label
        characteristics = {
            "Tj_IGBT_mean_C": "IGBT mean junction temp. (°C)",
            # "Tj_IGBT_max_C": "IGBT max junction temp. (°C)",
            # "Tj_IGBT_min_C": "IGBT min junction temp. (°C)",          # = 25 °C start temperature
            "Tj_IGBT_swing_K": "IGBT junction swing p95-p05 (K)",     # dominated by warm-up
            # "Tj_Diode_mean_C": "Diode mean junction temp. (°C)",      # diode not limiting
            # "Tj_Diode_max_C": "Diode max junction temp. (°C)",        # diode not limiting
            # "Tj_Diode_min_C": "Diode min junction temp. (°C)",        # = 25 °C start temperature
            # "Tj_Diode_swing_K": "Diode junction swing p95-p05 (K)",   # dominated by warm-up
            # "T_case_mean_C": "Mean case temp. (°C)",
            # "T_case_swing_K": "Case swing p95-p05 (K)",               # warm-up artifact
        }

        # thermal cycle statistics -> y axis label
        cycle_characteristics = {
            # "cycles_per_h": "cycles (1/h)",                                # 180000 for all (50 Hz)
            # "dT_max_K": "max cycle ΔTj (K)",                               # = heat-up cycle
            # "dT_mean_K": "mean cycle ΔTj (K)",                             # dominated by grid cycles
            # "dT_p95_K": "cycle ΔTj p95 (K)",                               # dominated by grid cycles
            # "cycles_dT_lt5_per_h": "cycles ΔTj < 5 K (1/h)",               # ~180000 for all (grid)
            "cycles_dT_5_10_per_h": "cycles ΔTj 5-10 K (1/h)",
            "cycles_dT_10_20_per_h": "cycles ΔTj 10-20 K (1/h)",
            # "cycles_dT_ge20_per_h": "cycles ΔTj ≥ 20 K (1/h)",             # 0.5 for all (heat-up)
            # "cycle_Tmean_C": "mean cycle temp. (°C)",
            # "cycle_duration_mean_s": "mean cycle heating time (s)",        # dominated by grid cycles
            # "cycle_duration_p95_s": "cycle heating time p95 (s)",          # dominated by grid cycles
            # "grid_cycles_per_h": "grid cycles (1/h)",                      # ~constant
            # "grid_cycle_dT_mean_K": "mean grid cycle ΔTj (K)",
            # "grid_cycle_dT_max_K": "max grid cycle ΔTj (K)",               # proportional to IGBT max loss
            # "load_cycles_per_h": "load cycles (1/h)",                      # dominated by small cycles
            # "load_cycle_dT_mean_K": "mean load cycle ΔTj (K)",             # diluted by small cycles
            # "load_cycle_dT_max_K": "max load cycle ΔTj (K)",               # = heat-up cycle
            # "load_cycle_Tmean_C": "mean load cycle temp. (°C)",
            # "load_cycle_duration_mean_s": "mean load cycle heating time (s)",  # diluted by small cycles
        }
        for device in ("IGBT",):                                             # ("IGBT", "Diode") to include diode
            for key, label in cycle_characteristics.items():
                characteristics[f"{device}_{key}"] = f"{device} {label}"

        save_dir = Path(figures_dir) / "Thermal_characteristics"
        save_dir.mkdir(parents=True, exist_ok=True)

        thermal = dictionary_master.get("Thermal_characteristics", dictionary_master)
        members = _find_members(thermal)

        for key, ylabel in characteristics.items():
            _grouped_bar_plot(thermal, members, key, ylabel, save_dir / f"{key}.png")

        print(f"Saved {len(characteristics)} figures to {save_dir}")

    def Lifetime_characteristics_plotting(dictionary_master, figures_dir, steady_state=True):
        """Grouped bar charts of lifetime characteristics (log scale for Nf and years).
        steady_state=True : simulations use steady-state cycles (no heat-up) -> Nf_eq used directly.
        steady_state=False: old runs from ambient -> heat-up half cycle removed analytically.
        Saved in figures_dir/Lifetime_characteristics."""

        # characteristic, same for IGBT and diode -> (y axis label, log scale)
        lifetime_characteristics = {
            # "Nf_eq": ("Nf,eq all cycles (-)", True),
            # "Nf_eq_dT_ge10": ("Nf,eq cycles ΔTj ≥ 10 K (-)", True),
            # "Nf_eq_dT_lt10": ("Nf,eq cycles ΔTj < 10 K (-)", True),
            # "Nf_eq_load_cycles": ("Nf,eq load cycles (-)", True),
            # "Nf_eq_grid_cycles": ("Nf,eq grid cycles (-)", True),
            # "Nf_worst_cycle": ("Nf of worst cycle (-)", True),
            # "worst_cycle_dT_K": ("ΔTj of worst cycle (K)", False),
            # "worst_cycle_Tmean_C": ("mean temp. of worst cycle (°C)", False),
            #"Nf_eq_workload": ("Nf,eq workload cycles (-)", True),  # computed below
            "Damage_ratio": ("workload damage rel. to min. (-)", True),  # computed below

            # ---- lifetime in years ----
            #"lifetime_years_workload": ("lifetime (years)", True),  # computed below
            "lifetime_years_actual": ("lifetime, from simulation (years)", False),  # as saved by mother_function
            # "lifetime_years_dT_ge10": ("lifetime, cycles ΔTj ≥ 10 K (years)", True),
            # "lifetime_years_load_cycles": ("lifetime, load cycles (years)", True),
            # "lifetime_years_grid_cycles": ("lifetime, grid cycles (years)", True),
        }
        devices = ("IGBT",)  # ("IGBT", "Diode") to include diode

        characteristics = {}
        for device in devices:
            for key, (label, log) in lifetime_characteristics.items():
                characteristics[f"{device}_{key}"] = (f"{device} {label}", log)

        save_dir = Path(figures_dir) / "Lifetime_characteristics"
        save_dir.mkdir(parents=True, exist_ok=True)

        # copy, so the input dictionary stays unchanged
        lifetime = {s: dict(v) for s, v in dictionary_master.get("Nf_results", dictionary_master).items()}
        members = _find_members(lifetime)
        plotted_scenarios = [s for m in members.values() for s in m]
        seconds_per_year = 365 * 24 * 3600

        for device in devices:
            for v in lifetime.values():
                nf = v.get(f"{device}_Nf_eq")
                if steady_state:
                    # no heat-up in the cycles -> Nf_eq is already workload-only
                    v[f"{device}_Nf_eq_workload"] = nf
                else:
                    # old runs: remove the heat-up half cycle (count 0.5 = worst cycle)
                    nw = v.get(f"{device}_Nf_worst_cycle")
                    if nf and nw:
                        D_workload = 1 / nf - 0.5 / nw
                        v[f"{device}_Nf_eq_workload"] = 1 / D_workload if D_workload > 0 else None

                # workload lifetime in years = Nf_eq_workload * mission duration
                nwl, mission_s = v.get(f"{device}_Nf_eq_workload"), v.get("Mission_duration_s")
                if nwl and mission_s:
                    v[f"{device}_lifetime_years_workload"] = nwl * mission_s / seconds_per_year

            # damage relative to the least damaged plotted scenario (= 1)
            nf_wl = {s: lifetime[s].get(f"{device}_Nf_eq_workload") for s in plotted_scenarios}
            nf_max = max((n for n in nf_wl.values() if n), default=None)
            for s, n in nf_wl.items():
                if n and nf_max:
                    lifetime[s][f"{device}_Damage_ratio"] = nf_max / n

        for key, (ylabel, log) in characteristics.items():
            _grouped_bar_plot(lifetime, members, key, ylabel, save_dir / f"{key}.png", log=log)

        print(f"Saved {len(characteristics)} figures to {save_dir}")

    # ---- plot ----
    Load_characteristics_plotting(dictionary_master, figures_dir)
    Electrical_characteristics_plotting(dictionary_master, figures_dir)
    Thermal_characteristics_plotting(dictionary_master, figures_dir)
    Lifetime_characteristics_plotting(dictionary_master, figures_dir)

base_dir= r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm"
figures_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm\Figures"
file_name = r"dictionary_master.json"

#plotting(base_dir,figures_dir,file_name)

base_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"
figures_dir = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW\Figures"
file_name = r"dictionary_master.json"

#plotting(base_dir,figures_dir,file_name)



#########################################################################################################################
# Plotting damage to proposed framework
#########################################################################################################################


def workload_damage(v, dev="IGBT"):
    """Workload-only damage per mission: direct sum if saved, else heat-up half cycle subtracted."""
    D = v.get(f"{dev}_D_workload")
    if D is None:                                             # older dictionaries: subtraction
        nf, nw = v.get(f"{dev}_Nf_eq"), v.get(f"{dev}_Nf_worst_cycle")
        D = (1 / nf - 0.5 / nw) if (nf and nw) else np.nan
    return D if (D is not None and D > 0) else np.nan


def workload_damage_per_1e9h(v, dev="IGBT"):
    """Workload-only damage per 10^9 operating hours (scale of FIT figures), heat-up removed."""
    D = workload_damage(v, dev)
    mission_s = v.get("Mission_duration_s")
    if not np.isfinite(D) or not mission_s:
        return np.nan
    return D * (3600.0 / mission_s) * 1e9

def plot_metric_vs_target(sets, chips, colours, figures_dir, filename,
                          x_key, target, x_label, y_label, relative=False,
                          log_x=False, log_y=False, rating_axis=False, P_rated_MW=2.0,
                          legend_loc="upper right", show_corr=False, fit_line=True, fit_deg=1,
                          dedup_cols=("P_mean_MW", "P_max_MW", "Swing_p95_p05_MW")):
    """
    Any load characteristic (x_key) against any target for all scenarios of the selected
    chips and both scalings.

    target = "workload_damage"          : workload-only damage per mission (heat-up removed);
                                          relative=True -> least damaging scenario = 1
    target = "workload_damage_per_1e9h" : workload-only damage per 10^9 operating hours
    target = any Nf_results key         : e.g. "IGBT_Nf_eq"

    rating_axis adds a top axis in p.u.^2 (for x = swing x RMS power in MW^2).
    """

    TARGETS = {"workload_damage": workload_damage,
               "workload_damage_per_1e9h": workload_damage_per_1e9h}

    rows = []
    for set_key, (_, folder) in sets.items():
        with open(Path(folder) / "dictionary_master.json") as f:
            dm = json.load(f)
        load = pd.DataFrame.from_dict(dm["Load_characteristics"], orient="index")

        for chip in chips:
            keep = [s for s in load.index if f"_{chip}_" in s and s in dm["Nf_results"]]
            dup = load.loc[keep][list(dedup_cols)].round(6).duplicated()
            for s in dup[~dup].index:
                v = dm["Nf_results"][s]
                yv = TARGETS[target](v) if target in TARGETS else v.get(target)
                rows.append({"set": set_key, "chip": chip, "scenario": s,
                             "x": pd.to_numeric(load.loc[s, x_key], errors="coerce"),
                             "y": np.nan if yv is None else float(yv)})

    df = pd.DataFrame(rows).dropna(subset=["x", "y"])
    if target == "workload_damage" and relative:
        df["y"] = df["y"] / df["y"].min()                                  # least damaging = 1

    rho, _ = spearmanr(df["x"], df["y"])
    tau, _ = kendalltau(df["x"], df["y"])
    print(f"{len(df)} scenarios | {x_key} vs {target} | rho = {rho:.3f} | tau = {tau:.3f}")
    print(df.sort_values("y", ascending=False).head(5)[["set", "chip", "scenario", "y"]])  # largest values

    fig, ax = plt.subplots(figsize=(6.4, 4.8 * 0.75))

    for (set_key, chip), d in df.groupby(["set", "chip"]):
        ax.scatter(d["x"], d["y"], marker=chips[chip], s=70, color=colours[set_key],
                   edgecolor="black", linewidth=0.8, zorder=3)

    # ---- black trend line: polynomial fit in log-log space (deg 1 = power law) ----
    if fit_line:
        fx, fy = np.log10(df["x"].to_numpy()), np.log10(df["y"].to_numpy())
        coef = np.polyfit(fx, fy, fit_deg)
        r2 = 1 - np.sum((fy - np.polyval(coef, fx)) ** 2) / np.sum((fy - fy.mean()) ** 2)
        xs = np.linspace(fx.min(), fx.max(), 300)
        ax.plot(10 ** xs, 10 ** np.polyval(coef, xs), color="black", lw=1.8, zorder=2)
        if fit_deg == 1:
            print(f"Fit: y = {10 ** coef[1]:.3g} * x^{coef[0]:.2f} | R² = {r2:.3f}")
        else:
            print(f"Fit (log-log, deg {fit_deg}): coefficients {np.round(coef, 3)} | R² = {r2:.3f}")

    if log_x:
        ax.set_xscale("log")
    else:
        ax.set_xlim(0, df["x"].max() * 1.08)
    if log_y:
        ax.set_yscale("log")
    else:
        ax.set_ylim(0, df["y"].max() * 1.15)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    if rating_axis:
        sec = ax.secondary_xaxis("top", functions=(lambda x: x / P_rated_MW ** 2,
                                                   lambda u: u * P_rated_MW ** 2))
        sec.set_xlabel("Swing × RMS power (p.u.², base = inverter rating)")

    if show_corr:
        ax.text(0.02, 0.04, rf"$\rho$ = {rho:.3f},  $\tau$ = {tau:.3f}",
                transform=ax.transAxes, ha="left", va="bottom")

    handles = [Line2D([], [], marker="o", linestyle="", color=colours[k],
                      markeredgecolor="black", markersize=9, label=sets[k][0]) for k in sets]
    if len(chips) > 1:
        handles += [Line2D([], [], marker=m, linestyle="", color="lightgrey",
                           markeredgecolor="black", markersize=9, label=c) for c, m in chips.items()]
    if fit_line:
        handles += [Line2D([], [], color="black", lw=1.8, label="Fit")]

    ax.legend(handles=handles, ncol=2 if len(chips) > 1 else 1, loc=legend_loc, frameon=True,
              handlelength=2, borderpad=0.5, columnspacing=1, labelspacing=0.25)

    fig.savefig(f"{figures_dir}/{filename}", dpi=600, bbox_inches="tight")
    plt.close(fig)
    return df

SETS = {  # folder key -> (label, results folder)
    "norm": ("Equal energy", r"E:\IEEE_GM_2027\IEEE_results\Results\norm"),
    "2MW": ("Actual power", r"E:\IEEE_GM_2027\IEEE_results\Results\2MW"),
}
CHIPS = {"B200": "o", "H100": "s"}  # chip -> marker
#CHIPS = {"B200": "o"}                 # chip -> marker
COLOURS = {"norm": "red", "2MW": "blue"}  # set -> colour

"""
plot_metric_vs_target(SETS, CHIPS, COLOURS, figures_dir=r"E:\IEEE_GM_2027\IEEE_results\Figures",
                      filename="swing1s_x_Prms_vs_workload_damage_per_1e9h.png",
                      x_key="Swing_period1s_max_MW_x_Prms_MW",
                      target="workload_damage_per_1e9h",
                      x_label="Max. 1 s swing × RMS power (MW²)",
                      y_label="Damage rate (FIT)",
                      legend_loc="lower right", log_y=True,
                      rating_axis=True, P_rated_MW=2.0)

"""


#########################################################################################################################
# Damage rate (FIT) per scenario
#########################################################################################################################
#########################################################################################################################
# Damage rate (FIT) grouped by hyperparameter sweep
#########################################################################################################################

# sweep -> (scenario name prefix with {chip}, x axis label, colour map)
SWEEPS = {
    "Image batch size": ("Image_{chip}_BatchSize_", "Image\nBatch size", "Blues"),
    "Image size":       ("Image_{chip}_ImageSize_", "Image\nImage size", "Blues"),
    "Image model size": ("Image_{chip}_ModelSize_", "Image\nModel size", "Blues"),
    "LLM batch size":   ("Text_{chip}_BatchSize",   "LLM\nBatch size",   "Oranges"),
    "LLM model size":   ("Text_{chip}_Lamma_",      "LLM\nModel size",   "Oranges"),
    "LLM seq. length":  ("Text_{chip}_SeqLength_",  "LLM\nSeq. length",  "Oranges"),
}


def plot_damage_rate(sets, chips, figures_dir, filename, sweeps=SWEEPS,
                     y_label="Damage rate (FIT)", figsize=(6.4 * 2, 4.8)):
    """
    Grouped bar chart of the workload damage per 10^9 h (FIT): one group per hyperparameter sweep,
    one bar per setting (light = low, dark = high). One figure per set and chip.
    """
    for set_key, (set_label, folder) in sets.items():
        with open(Path(folder) / "dictionary_master.json") as f:
            nf = json.load(f)["Nf_results"]

        for chip in chips:
            number = lambda name, prefix: float(re.search(r"\d+", name[len(prefix):]).group())

            fig, ax = plt.subplots(figsize=figsize)
            x = np.arange(len(sweeps))
            n_max, xlabels, plotted = 3, [], []

            for i, (g, (prefix_t, label, cmap)) in enumerate(sweeps.items()):
                prefix = prefix_t.format(chip=chip)
                members = sorted((s for s in nf if s.startswith(prefix)), key=lambda s: number(s, prefix))
                if not members:
                    print(f"[{set_key} | {chip}] no scenarios for '{g}'")
                n_max = max(n_max, len(members))
                xlabels.append(f"{label}\n" + " | ".join(s[len(prefix):].lstrip("_") for s in members))

                width = 0.8 / max(len(members), 1)
                shades = plt.get_cmap(cmap)(np.linspace(0.35, 0.9, max(len(members), 1)))
                for j, s in enumerate(members):
                    v = workload_damage_per_1e9h(nf[s])
                    if np.isfinite(v) and v > 0:
                        plotted.append(v)
                        print(f"[{set_key} | {chip}] {s}: {v:.3g} FIT")
                    else:
                        v = np.nan
                    pos = x[i] + (j - (len(members) - 1) / 2) * width
                    ax.bar(pos, v, width, color=shades[j], edgecolor="black", linewidth=0.8)

            grey = plt.get_cmap("Greys")(np.linspace(0.35, 0.9, n_max))
            level = ["Low", "Moderate", "High"] if n_max == 3 else [f"Setting {k + 1}" for k in range(n_max)]
            ax.legend(handles=[Patch(facecolor=grey[k], edgecolor="black", label=level[k]) for k in range(n_max)],
                      loc="upper left", ncol=n_max, frameon=False)

            ax.set_xticks(x)
            ax.set_xticklabels(xlabels)
            ax.set_ylabel(y_label)
            ax.set_yscale("log")
            if plotted:
                ax.set_ylim(min(plotted) / 10, max(plotted) * 100)        # room for the legend
            ax.grid(axis="y", alpha=0.3)
            ax.set_axisbelow(True)

            out = Path(figures_dir) / f"{Path(filename).stem}_{set_key}_{chip}.png"
            fig.savefig(out, dpi=600, bbox_inches="tight")
            plt.close(fig)
            print(f"Saved {out}")



FIG_DIR = r"E:\IEEE_GM_2027\IEEE_results\Results_run2\Figures"
Path(FIG_DIR).mkdir(parents=True, exist_ok=True)

SETS = {  # folder key -> (label, results folder)
    #"norm": ("Equal energy", r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm"),
    "2MW": ("Actual power", r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"),
}
CHIPS = {"B200": "o"}#, "H100": "s"}  # chip -> marker
COLOURS = {"norm": "red", "2MW": "blue"}  # set -> colour

#plot_damage_rate(SETS, CHIPS, figures_dir=FIG_DIR,filename="damage_rate_FIT.png")








#########################################################################################################################
# Normal damage vs effective power level sqrt(mean^2 + 0.5 var)
#########################################################################################################################

DATA = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")
PROFILE_FILES = {  # set -> {chip: parquet file relative to DATA}
    "norm": {"H100": "H_100/Dataframes/df_H_100_norm.parquet", "B200": "B_200/Dataframes/df_B_200_norm.parquet"},
    "2MW":  {"H100": "H_100/Dataframes/df_H_100_2MW.parquet",  "B200": "B_200/Dataframes/df_B_200_2MW.parquet"},
}
DUPLICATES = ("ImageSize_32", "ModelSize_128", "Deepspeedds_z3", "Lamma_8B", "SeqLength_2048")


def normal_damage(v, dev="IGBT"):
    """Total damage per mission: Miner's rule over all cycles, heat-up included."""
    nf = v.get(f"{dev}_Nf_eq")
    return 1.0 / nf if nf else np.nan

def effective_level(p_MW, lam=0.5):
    """Effective power level sqrt(mean^2 + lam * var) [MW]."""
    p = np.asarray(p_MW, dtype=float)
    return np.sqrt(p.mean() ** 2 + lam * p.var())

def plot_effective_level_vs_damage(sets, chips, colours, figures_dir, filename,
                                   profile_files=PROFILE_FILES, data_dir=DATA,
                                   window_s=900.0, dt=0.02, P_rated_MW=2.0,
                                   x_label="Effective level, sqrt(mean² + 0.5·var) (MW)",
                                   y_label="Damage per mission (–)",
                                   legend_loc="lower right", fit_line=True, fit_deg=2, rating_axis=True):
    """x = effective power level of the first 15 min, y = normal damage (1 / IGBT_Nf_eq, log axis)."""
    Path(figures_dir).mkdir(parents=True, exist_ok=True)
    n_keep = int(round(window_s / dt))

    # ---- collect data ----
    rows = []
    for set_key, (_, folder) in sets.items():
        with open(Path(folder) / "dictionary_master.json") as f:
            nf = json.load(f)["Nf_results"]
        for chip in chips:
            df = pd.read_parquet(Path(data_dir) / profile_files[set_key][chip]).iloc[:n_keep]
            for col in df.columns.drop("time_s"):
                if col.endswith(DUPLICATES) or col not in nf:
                    continue
                rows.append({"set": set_key, "chip": chip, "scenario": col,
                             "x": effective_level(df[col].to_numpy() / 1e6),
                             "y": normal_damage(nf[col])})
            del df

    d = pd.DataFrame(rows).replace([np.inf, -np.inf], np.nan).dropna(subset=["x", "y"])
    rho, _ = spearmanr(d["x"], d["y"])
    tau, _ = kendalltau(d["x"], d["y"])
    print(f"{len(d)} scenarios | effective level vs normal damage | rho = {rho:.3f} | tau = {tau:.3f}")

    # ---- plot ----
    fig, ax = plt.subplots(figsize=(6.4, 4.8 * 0.75))
    for (set_key, chip), g in d.groupby(["set", "chip"]):
        ax.scatter(g["x"], g["y"], marker=chips[chip], s=70, color=colours[set_key],
                   edgecolor="black", linewidth=0.8, zorder=3)

    if fit_line:  # log10(damage) as polynomial in the effective level
        fx, fy = d["x"].to_numpy(), np.log10(d["y"].to_numpy())
        coef = np.polyfit(fx, fy, fit_deg)
        r2 = 1 - np.sum((fy - np.polyval(coef, fx)) ** 2) / np.sum((fy - fy.mean()) ** 2)
        xs = np.linspace(fx.min(), fx.max(), 300)
        ax.plot(xs, 10 ** np.polyval(coef, xs), color="black", lw=1.8, zorder=2)
        print(f"Fit: log10(D) = poly(P_eff), coefficients {np.round(coef, 4)} | R² = {r2:.3f}")

    # ---- axes: plain tick labels, no mathtext ----
    ax.set_yscale("log")
    ax.yaxis.set_major_locator(LogLocator(base=10))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"1e{int(round(np.log10(v)))}"))
    ax.set_xlim(0, d["x"].max() * 1.1)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    if rating_axis:  # top axis: same quantity in % of converter rating
        sec = ax.secondary_xaxis("top", functions=(lambda x: 100.0 * x / P_rated_MW,
                                                   lambda p: p * P_rated_MW / 100.0))
        sec.set_xlabel("Effective level (% of rating)")

    # ---- legend ----
    handles = [Line2D([], [], marker="o", linestyle="", color=colours[k],
                      markeredgecolor="black", markersize=9, label=sets[k][0]) for k in sets]
    if len(chips) > 1:
        handles += [Line2D([], [], marker=m, linestyle="", color="lightgrey",
                           markeredgecolor="black", markersize=9, label=c) for c, m in chips.items()]
    if fit_line:
        handles += [Line2D([], [], color="black", lw=1.8, label="Fit")]
    ax.legend(handles=handles, ncol=2 if len(chips) > 1 else 1, loc=legend_loc, frameon=True,
              handlelength=2, borderpad=0.5, columnspacing=1, labelspacing=0.25)

    fig.savefig(Path(figures_dir) / filename, dpi=600, bbox_inches="tight")
    plt.close(fig)
    return d

SETS = {  # folder key -> (label, results folder)
    "norm": ("Equal energy", r"E:\IEEE_GM_2027\IEEE_results\Results_run2\norm"),
    "2MW": ("Actual power", r"E:\IEEE_GM_2027\IEEE_results\Results_run2\2MW"),
}

CHIPS = {"B200": "o", "H100": "s"}
COLOURS = {"norm": "red", "2MW": "blue"}

df_eff = plot_effective_level_vs_damage(SETS, CHIPS, COLOURS,figures_dir=r"E:\IEEE_GM_2027\IEEE_results\Figures",filename="effective_level_vs_normal_damage.png")