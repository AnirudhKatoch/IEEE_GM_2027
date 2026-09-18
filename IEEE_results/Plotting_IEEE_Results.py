import re
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import json
plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15, "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})


def norm():
    base_dir= r"E:\IEEE_GM_2027\IEEE_results\Results\norm"
    figures_dir = r"E:\IEEE_GM_2027\IEEE_results\Results\norm\Figures"
    file_name = r"dictionary_master.json"

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
            "P_mean_MW":             "Mean power (MW)",
            "P_max_MW":              "Maximum power (MW)",
            "P_min_MW":              "Minimum power (MW)",
            # "Energy_MWh":            "Energy (MWh)",               # = P_mean for 1 h window
            "Peak_to_mean":          "Peak-to-mean ratio (-)",
            "Swing_p95_p05_MW":      "Power swing p95-p05 (MW)",
            "Time_at_high_load_pct": "Time at high load (%)",
            "Dominant_period_s":     "Dominant period (s)",
            "Transitions_per_h":     "Load transitions (1/h)",
            "Ramp_p99_MW_per_s":     "Ramp rate p99 (MW/s)",
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
    def Lifetime_characteristics_plotting(dictionary_master, figures_dir):
        """Grouped bar charts of lifetime characteristics (log scale for Nf).
        Saved in figures_dir/Lifetime_characteristics."""

        # characteristic, same for IGBT and diode -> (y axis label, log scale)
        lifetime_characteristics = {
            "Nf_eq": ("Nf,eq all cycles (-)", True),                           # = heat-up half cycle
            # "Nf_eq_dT_ge10": ("Nf,eq cycles ΔTj ≥ 10 K (-)", True),            # = heat-up half cycle
            # "Nf_eq_dT_lt10": ("Nf,eq cycles ΔTj < 10 K (-)", True),            # misleading: excludes 10-20 K cycles
            # "Nf_eq_load_cycles": ("Nf,eq load cycles (-)", True),              # = heat-up half cycle
            # "Nf_eq_grid_cycles": ("Nf,eq grid cycles (-)", True),
            # "Nf_worst_cycle": ("Nf of worst cycle (-)", True),                 # = heat-up half cycle
            # "worst_cycle_dT_K": ("ΔTj of worst cycle (K)", False),             # = Tj_max - 25
            # "worst_cycle_Tmean_C": ("mean temp. of worst cycle (°C)", False),  # = (25 + Tj_max) / 2
            # "Nf_eq_workload": ("Nf,eq workload cycles (-)", True),             # heat-up removed (computed below)
            "Damage_ratio": ("workload damage rel. to min. (-)", True),          # computed below
        }
        devices = ("IGBT",)                                                      # ("IGBT", "Diode") to include diode

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

        # ---- workload-only Nf_eq: remove the heat-up half cycle (count 0.5 = worst cycle) ----
        # valid only while simulations start at ambient; remove after warm-start fix
        for device in devices:
            for v in lifetime.values():
                nf, nw = v.get(f"{device}_Nf_eq"), v.get(f"{device}_Nf_worst_cycle")
                if nf and nw:
                    D_workload = 1 / nf - 0.5 / nw
                    v[f"{device}_Nf_eq_workload"] = 1 / D_workload if D_workload > 0 else None

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


def sce_2MW():
    base_dir = r"E:\IEEE_GM_2027\IEEE_results\Results\2MW"
    figures_dir = r"E:\IEEE_GM_2027\IEEE_results\Results\2MW\Figures"
    file_name = r"dictionary_master.json"

    # ---- load dictionary_master ----
    with open(Path(base_dir) / file_name) as f:
        dictionary_master = json.load(f)

    # sweep -> (prefix of scenario names in dictionary, label on x axis, colormap)
    # all scenarios starting with the prefix are found automatically and sorted low -> high by their number
    GROUPS = {
        "Image batch size": ("Image_B200_BatchSize_", "Image\nBatch size", "Blues"),
        "Image size": ("Image_B200_ImageSize_", "Image\nImage size", "Blues"),
        "Image model size": ("Image_B200_ModelSize_", "Image\nModel size", "Blues"),
        "LLM batch size": ("Text_B200_BatchSize", "LLM\nBatch size", "Oranges"),
        "LLM model size": ("Text_B200_Lamma_", "LLM\nModel size", "Oranges"),
        "LLM seq. length": ("Text_B200_SeqLength_", "LLM\nSeq. length", "Oranges"),
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
                v = np.nan if v is None else float(v)  # JSON null -> NaN
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
                ax.set_ylim(min(plotted) / 10, max(plotted) * 100)  # room for legend
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
            "Time_at_high_load_pct": "Time at high load (%)",
            "Dominant_period_s": "Dominant period (s)",
            "Transitions_per_h": "Load transitions (1/h)",
            "Ramp_p99_MW_per_s": "Ramp rate p99 (MW/s)",
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
            "I_Diode_rms_A": "Diode RMS current (A)",  # fixed fraction of IGBT RMS current
            # "I_Diode_peak_A": "Diode peak current (A)",               # fixed fraction of IGBT peak current
            "P_loss_IGBT_mean_W": "IGBT mean loss (W)",
            # "P_loss_IGBT_max_W": "IGBT max loss (W)",
            "P_loss_IGBT_swing_W": "IGBT loss swing p95-p05 (W)",
            "P_loss_Diode_mean_W": "Diode mean loss (W)",  # ~fixed fraction of IGBT mean loss
            # "P_loss_Diode_max_W": "Diode max loss (W)",               # ~fixed fraction of IGBT max loss
            "P_loss_Diode_swing_W": "Diode loss swing p95-p05 (W)",  # ~fixed fraction of IGBT loss swing
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
            "Tj_IGBT_swing_K": "IGBT junction swing p95-p05 (K)",  # dominated by warm-up
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
        for device in ("IGBT",):  # ("IGBT", "Diode") to include diode
            for key, label in cycle_characteristics.items():
                characteristics[f"{device}_{key}"] = f"{device} {label}"

        save_dir = Path(figures_dir) / "Thermal_characteristics"
        save_dir.mkdir(parents=True, exist_ok=True)

        thermal = dictionary_master.get("Thermal_characteristics", dictionary_master)
        members = _find_members(thermal)

        for key, ylabel in characteristics.items():
            _grouped_bar_plot(thermal, members, key, ylabel, save_dir / f"{key}.png")

        print(f"Saved {len(characteristics)} figures to {save_dir}")

    def Lifetime_characteristics_plotting(dictionary_master, figures_dir):
        """Grouped bar charts of lifetime characteristics (log scale for Nf).
        Saved in figures_dir/Lifetime_characteristics."""

        # characteristic, same for IGBT and diode -> (y axis label, log scale)
        lifetime_characteristics = {
            "Nf_eq": ("Nf,eq all cycles (-)", True),  # = heat-up half cycle
            # "Nf_eq_dT_ge10": ("Nf,eq cycles ΔTj ≥ 10 K (-)", True),            # = heat-up half cycle
            # "Nf_eq_dT_lt10": ("Nf,eq cycles ΔTj < 10 K (-)", True),            # misleading: excludes 10-20 K cycles
            # "Nf_eq_load_cycles": ("Nf,eq load cycles (-)", True),              # = heat-up half cycle
            # "Nf_eq_grid_cycles": ("Nf,eq grid cycles (-)", True),
            # "Nf_worst_cycle": ("Nf of worst cycle (-)", True),                 # = heat-up half cycle
            # "worst_cycle_dT_K": ("ΔTj of worst cycle (K)", False),             # = Tj_max - 25
            # "worst_cycle_Tmean_C": ("mean temp. of worst cycle (°C)", False),  # = (25 + Tj_max) / 2
            # "Nf_eq_workload": ("Nf,eq workload cycles (-)", True),             # heat-up removed (computed below)
            "Damage_ratio": ("workload damage rel. to min. (-)", True),  # computed below
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

        # ---- workload-only Nf_eq: remove the heat-up half cycle (count 0.5 = worst cycle) ----
        # valid only while simulations start at ambient; remove after warm-start fix
        for device in devices:
            for v in lifetime.values():
                nf, nw = v.get(f"{device}_Nf_eq"), v.get(f"{device}_Nf_worst_cycle")
                if nf and nw:
                    D_workload = 1 / nf - 0.5 / nw
                    v[f"{device}_Nf_eq_workload"] = 1 / D_workload if D_workload > 0 else None

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

sce_2MW()