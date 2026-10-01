import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import re
import pyarrow

plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15,"xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

def cut_to_window(df, minutes=15, dt=0.02):
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    t = (df["timestamp"] - df["timestamp"].iloc[0]).dt.total_seconds().to_numpy()

    n = int(round(minutes * 60 / dt))              # 45000 rows
    grid = np.round(np.arange(n) * dt, 6)          # exact 0.00, 0.02, ... 899.98 s

    # last real sample at or before each grid time (tolerance for timestamp jitter)
    idx = np.searchsorted(t, grid + dt / 2, side="right") - 1
    idx = np.clip(idx, 0, len(df) - 1)

    out = df.iloc[idx].reset_index(drop=True)
    out["time_s"] = grid

    if t[-1] < grid[-1] - dt / 2:
        print(f"Padded: data ended at {t[-1]:.2f} s, copied last value up to {grid[-1]:.2f} s")

    return out

def plot_total_power(df,figure_dir,chip):

    power_cols = [f"gpu{i}_power_W" for i in range(8)]
    total_W = df[power_cols].sum(axis=1)

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(df["time_s"] / 60, total_W, lw=0.8,color="black")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel(f"8×{chip} node GPU power (W)")
    ax.set_xlim(0, df["time_s"].max() / 60)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    plt.savefig(figure_dir)

def process_folder_image_generation(folder, key):
    folder = Path(folder)
    chip = folder.parent.name
    figure_dir = folder / "Figures"
    figure_dir.mkdir(exist_ok=True)
    power_cols = [f"gpu{i}_power_W" for i in range(8)]

    csvs = sorted(folder.glob("*.csv"),
                  key=lambda f: int(re.search(rf"{key}(\d+)", f.stem).group(1)))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    rows = []

    for csv in csvs:
        df = cut_to_window(pd.read_csv(csv), 15)
        label = re.search(rf"{key}\d+", csv.stem).group(0)     # e.g. "ImageSize64"

        plot_total_power(df, figure_dir=figure_dir / f"{label}.png",chip=chip)
        plt.close()

        p = df[power_cols].sum(axis=1)
        dt = df["time_s"].diff()
        ramp = (p.diff() / dt).abs()

        ax.plot(df["time_s"] / 60, p, lw=0.8, label=label)

        rows.append({
            "chip": folder.parent.name,
            "scenario": folder.name,
            "case": label,
            "mean_W": p.mean(),
            "median_W": p.median(),
            "min_W": p.min(),
            "max_W": p.max(),
            "p95_W": p.quantile(0.95),
            "p05_W": p.quantile(0.05),
            "std_W": p.std(),
            "peak_to_mean": p.max() / p.mean(),
            "swing_p95_p05_W": p.quantile(0.95) - p.quantile(0.05),
            "energy_kWh": (p * dt).sum() / 3.6e6,
            "time_above_2000W_pct": (p > 2000).mean() * 100,
            "ramp_p99_W_per_s": ramp.quantile(0.99),
            "mean_util_pct": df[[f"gpu{i}_utilization_percent" for i in range(8)]].mean(axis=1).mean(),
            "max_mem_MB": df[[f"gpu{i}_mem_used_MB" for i in range(8)]].max().max(),
        })

    ax.set_xlabel("Time (min)")
    ax.set_ylabel("8×H100 node GPU power (W)")
    ax.set_xlim(0, 15)
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(figure_dir / "Comparison.png")
    plt.close(fig)

    summary = pd.DataFrame(rows).round(2)
    summary.to_csv(figure_dir / f"{folder.parent.name}_{folder.name}_power_comparison.csv", index=False, sep=";")

base = r"E:\IEEE_GM_2027\Dataset\Node_Dataset\Image Generation Diffusion Models\H100"

#process_folder_image_generation(rf"{base}\Batch_size_impact", key="BatchSize")
#process_folder_image_generation(rf"{base}\Image_size_impact", key="ImageSize")
#process_folder_image_generation(rf"{base}\Model_size_impact", key="ModelSize")

base = r"E:\IEEE_GM_2027\Dataset\Node_Dataset\Image Generation Diffusion Models\B200"

#process_folder_image_generation(rf"{base}\Batch_size_impact", key="BatchSize")
#process_folder_image_generation(rf"{base}\Image_size_impact", key="ImageSize")
#process_folder_image_generation(rf"{base}\Model_size_impact", key="ModelSize")

def process_folder_text_generation(folder, key, threshold_W=2000):

    folder = Path(folder)
    chip = folder.parent.name
    figure_dir = folder / "Figures"
    figure_dir.mkdir(exist_ok=True)
    power_cols = [f"gpu{i}_power_W" for i in range(8)]

    pattern = rf"{key}\D*?(\d+)[A-Za-z]?"
    csvs = sorted(folder.glob("*.csv"), key=lambda f: int(re.search(pattern, f.stem).group(1)))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    rows = []

    for csv in csvs:
        df = cut_to_window(pd.read_csv(csv), 15)
        label = re.search(pattern, csv.stem).group(0)

        plot_total_power(df, figure_dir=figure_dir / f"{label}.png", chip=chip)
        plt.close()

        p = df[power_cols].sum(axis=1)
        dt = df["time_s"].diff()
        ramp = (p.diff() / dt).abs()

        ax.plot(df["time_s"] / 60, p, lw=0.8, label=label)

        rows.append({
            "chip": chip,
            "scenario": folder.name,
            "case": label,
            "mean_W": p.mean(),
            "median_W": p.median(),
            "min_W": p.min(),
            "max_W": p.max(),
            "p95_W": p.quantile(0.95),
            "p05_W": p.quantile(0.05),
            "std_W": p.std(),
            "peak_to_mean": p.max() / p.mean(),
            "swing_p95_p05_W": p.quantile(0.95) - p.quantile(0.05),
            "energy_kWh": (p * dt).sum() / 3.6e6,
            f"time_above_{threshold_W}W_pct": (p > threshold_W).mean() * 100,
            "ramp_p99_W_per_s": ramp.quantile(0.99),
            "mean_util_pct": df[[f"gpu{i}_utilization_percent" for i in range(8)]].mean(axis=1).mean(),
            "max_mem_MB": df[[f"gpu{i}_mem_used_MB" for i in range(8)]].max().max(),
        })

    ax.set_xlabel("Time (min)")
    ax.set_ylabel(f"8×{chip} node GPU power (W)")
    ax.set_xlim(0, 15)
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(figure_dir / "Comparison.png")
    plt.close(fig)

    summary = pd.DataFrame(rows).round(2)
    summary.to_csv(figure_dir / f"{chip}_{folder.name}_power_comparison.csv", index=False, sep=";")

base = r"E:\IEEE_GM_2027\Dataset\Node_Dataset\Text Generation LLMs\B200"

#process_folder_text_generation(rf"{base}\Batch_size", key="BatchSize")
#process_folder_text_generation(rf"{base}\DeepSpeed_parallel_sitting", key="Deepspeedds_z")
#process_folder_text_generation(rf"{base}\Model_Size", key="Lamma")
#process_folder_text_generation(rf"{base}\Sequence_length_cut", key="SeqLength")

base = r"E:\IEEE_GM_2027\Dataset\Node_Dataset\Text Generation LLMs\H100"

#process_folder_text_generation(rf"{base}\Batch_size", key="BatchSize")
#process_folder_text_generation(rf"{base}\DeepSpeed_parallel_sitting", key="Deepspeedds_z")
#process_folder_text_generation(rf"{base}\Model_Size", key="Lamma")
#process_folder_text_generation(rf"{base}\Sequence_length_cut", key="SeqLength")



def extend_to_day(df, repeats=96, dt=0.02):
    cols = df.columns.drop("time_s")
    data = {c: np.tile(df[c].to_numpy(), repeats) for c in cols}   # copy each 15-min block 96 times
    out = pd.DataFrame(data)
    out.insert(0, "time_s", np.round(np.arange(len(out)) * dt, 2))  # 0.00 ... 86399.98 s
    return out

def plot_all(df, save_path, until_s):
    cols = [c for c in df.columns if c != "time_s"]
    d = df[df["time_s"] < until_s]                       # only plot up to the given time

    # choose a readable time unit
    if until_s > 3 * 3600:
        scale, unit = 3600, "h"
    elif until_s > 300:
        scale, unit = 60, "min"
    else:
        scale, unit = 1, "s"

    fig, axes = plt.subplots(7, 3, figsize=(15, 20), sharex=True, sharey=True)

    for ax, col in zip(axes.flat, cols):
        ax.plot(d["time_s"] / scale, d[col], lw=0.5, color="black")
        ax.set_title(col, fontsize=12)
        ax.set_xlim(0, until_s / scale)
        ax.grid(alpha=0.3)

    for ax in axes[-1]:
        ax.set_xlabel(f"Time ({unit})")
    for ax in axes[:, 0]:
        ax.set_ylabel("Power (W)")

    fig.tight_layout()
    fig.savefig(save_path, dpi=200)
    plt.close(fig)

def normalize_local(df):
    out = df.copy()
    cols = df.columns.drop("time_s")
    out[cols] = (df[cols] - df[cols].min()) / (df[cols].max() - df[cols].min())
    return out

def normalize_mean(df):
    out = df.copy()
    cols = df.columns.drop("time_s")
    out[cols] = df[cols] / df[cols].mean()        # each profile: average = 1
    return out

def max_power(df):
    cols = [c for c in df.columns if c != "time_s"]
    peaks = df[cols].max().sort_values(ascending=False)
    #print(peaks)
    #print(f"\nOverall max: {peaks.iloc[0]:.1f} W in {peaks.index[0]}")
    return peaks.iloc[0]

def profile_multiplier(df,value):
    df = df.copy()
    cols = df.columns.drop("time_s")
    df[cols] = df[cols] * value
    return df


def build_parquet(chip):
    img = rf"E:\IEEE_GM_2027\Dataset\Node_Dataset\Image Generation Diffusion Models\{chip}"
    txt = rf"E:\IEEE_GM_2027\Dataset\Node_Dataset\Text Generation LLMs\{chip}"

    jobs = [  # (folder, regex, column name)
        (rf"{img}\Batch_size_impact",          r"BatchSize(\d+)",     f"Image_{chip}_BatchSize_{{}}"),
        (rf"{img}\Image_size_impact",          r"ImageSize(\d+)",     f"Image_{chip}_ImageSize_{{}}"),
        (rf"{img}\Model_size_impact",          r"ModelSize(\d+)",     f"Image_{chip}_ModelSize_{{}}"),
        (rf"{txt}\Batch_size",                 r"BatchSize(\d+)",     f"Text_{chip}_BatchSize{{}}"),
        (rf"{txt}\DeepSpeed_parallel_sitting", r"Deepspeedds_z(\d+)", f"Text_{chip}_Deepspeedds_z{{}}"),
        (rf"{txt}\Model_Size",                 r"Lamma(\d+B)",        f"Text_{chip}_Lamma_{{}}"),
        (rf"{txt}\Sequence_length_cut",        r"SeqLength(\d+)",     f"Text_{chip}_SeqLength_{{}}"),
    ]

    power_cols = [f"gpu{i}_power_W" for i in range(8)]
    out = pd.DataFrame({"time_s": np.round(np.arange(45000) * 0.02, 2)})  # 0.00 ... 899.98 s

    for folder, pattern, name in jobs:
        csvs = sorted(Path(folder).glob("*.csv"),
                      key=lambda f: int(re.search(r"\d+", re.search(pattern, f.stem).group(1)).group()))
        for csv in csvs:
            df = cut_to_window(pd.read_csv(csv), 15)
            col = name.format(re.search(pattern, csv.stem).group(1))
            out[col] = df[power_cols].sum(axis=1).to_numpy()

    return out


def name_of(chip):
    return f"{chip[0]}_{chip[1:]}"          # "H100" -> "H_100", "B200" -> "B_200"


##########################
# For running
##########################

base_dir = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")
chips = ["H100", "B200"]

# ---- build 15-min profiles, extend to one day, save ----
profiles = {}
for chip in chips:
    name = name_of(chip)
    df_dir = base_dir / name / "Dataframes"
    fig_dir = base_dir / name / "Figures"
    df_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    df_15min = build_parquet(chip)
    df_15min.to_parquet(df_dir / f"df_{name}_15min.parquet", index=False)

    df = extend_to_day(df_15min)
    df.to_parquet(df_dir / f"df_{name}.parquet", index=False)
    plot_all(df, fig_dir / f"{name}.png", until_s=1800)

    profiles[chip] = (df, df_dir, fig_dir)
    del df_15min

# ---- 2 MW scaling (both by B200 peak) and local normalization ----
peak_B200 = max_power(profiles["B200"][0])

for chip in chips:
    name = name_of(chip)
    df, df_dir, fig_dir = profiles[chip]

    df_2MW = profile_multiplier(df=df, value=2e6 / peak_B200)
    df_2MW.to_parquet(df_dir / f"df_{name}_2MW.parquet", index=False)
    plot_all(df_2MW, fig_dir / f"{name}_2MW.png", until_s=1800)
    del df_2MW

def build_equal_energy_profiles(profiles, chips, P_max=2e6, dt=0.02):
    """
    1) energy of every scenario (both chips)
    2) average energy over all scenarios
    3) scale every scenario so its energy = average energy
    4) global maximum power over all scaled scenarios
    5) multiply everything by P_max / global maximum -> global maximum = 2 MW
    """

    # ---- 1) energy of each scenario [J] ----
    energy = {}
    for chip in chips:
        df = profiles[chip][0]
        cols = df.columns.drop("time_s")
        energy[chip] = (df[cols] * dt).sum()                  # Series: one energy per scenario

    # ---- 2) average energy over all scenarios of both chips ----
    E_all = pd.concat(energy.values())
    E_avg = E_all.mean()

    # ---- 3) scale each scenario to equal energy ----
    scaled = {}
    for chip in chips:
        df = profiles[chip][0].copy()
        cols = df.columns.drop("time_s")
        df[cols] = df[cols] * (E_avg / energy[chip])           # factor per column
        scaled[chip] = df

    # ---- 4) global maximum power after equal-energy scaling ----
    global_max = max(df.drop(columns="time_s").max().max() for df in scaled.values())

    # ---- 5) scale so that global maximum = 2 MW ----
    k = P_max / global_max

    print(f"Average energy: {E_avg/3.6e9:.3f} MWh per scenario (before 2 MW scaling)")
    print(f"Global max after equal energy: {global_max/1e6:.3f} MW -> factor {k:.4f}")

    for chip in chips:
        name = name_of(chip)
        _, df_dir, fig_dir = profiles[chip]

        df = scaled[chip]
        cols = df.columns.drop("time_s")
        df[cols] = df[cols] * k

        check = pd.DataFrame({
            "profile": cols,
            "energy_MWh": ((df[cols] * dt).sum() / 3.6e9).to_numpy(),
            "mean_MW": (df[cols].mean() / 1e6).to_numpy(),
            "min_MW": (df[cols].min() / 1e6).to_numpy(),
            "max_MW": (df[cols].max() / 1e6).to_numpy(),
        }).round(4)
        check.to_csv(df_dir / f"{name}_norm_check.csv", index=False, sep=";")

        df.to_parquet(df_dir / f"df_{name}_norm.parquet", index=False)
        plot_all(df, fig_dir / f"{name}_norm.png", until_s=1800)

        del scaled[chip]
    
build_equal_energy_profiles(profiles, chips)





