import re
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

DATA = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")
FIG_DIR = Path(r"E:\IEEE_GM_2027\Dataset\Figures")
SCALE = 50                                   # 2 MW -> 100 MW
DUPLICATES = ("ImageSize_32", "ModelSize_128", "Deepspeedds_z3", "Lamma_8B", "SeqLength_2048")   # same as Correlation.py


def to_100MW(df, factor=SCALE):
    out = df.copy()
    cols = out.columns.drop("time_s")
    out[cols] = out[cols] * factor
    return out

def short_label(col):
    """'Image_B200_BatchSize_128' -> 'Img BS 128', 'Text_B200_Lamma_8B' -> 'LLM Llama 8B'"""
    work, _, rest = col.split("_", 2)
    work = "Img" if work == "Image" else "LLM"
    for key, abbr in (("BatchSize", "BS"), ("ImageSize", "IS"), ("ModelSize", "MS"),
                      ("Deepspeedds_z", "ZeRO"), ("Lamma", "Llama"), ("SeqLength", "SL")):
        if rest.startswith(key):
            return f"{work} {abbr} {rest[len(key):].strip('_')}"
    return f"{work} {rest}"

def unique_cols(df):
    return [c for c in df.columns if c != "time_s" and not c.endswith(DUPLICATES)]

PATTERN = re.compile(r"^(Image|Text)_[A-Z]\d+_(BatchSize|ImageSize|ModelSize|Deepspeedds_z|Lamma|SeqLength)_?(\d+)")

def moderate_cols(df):
    """Middle (moderate) level of each sweep, e.g. BatchSize 128/256/512 -> 256."""
    sweeps = {}
    for c in df.columns:
        m = PATTERN.match(c)
        if m:
            sweeps.setdefault((m.group(1), m.group(2)), []).append((int(m.group(3)), c))
    return [sorted(v)[len(v) // 2][1] for v in sweeps.values()]

def moderate_unique_cols(df):
    """Moderate level of each sweep, each measured profile shown only once."""
    keep = []
    for c in moderate_cols(df):
        if not any(np.allclose(df[c].to_numpy(), df[k].to_numpy()) for k in keep):
            keep.append(c)
    return keep

def plot_heatmap(sets, save_path, window_s=120.0, dt=0.02, vmax=100.0):
    """
    sets : {panel title: [(chip label, dataframe in W), ...]}
    One panel per set, one row per profile, shared colour scale 0..vmax MW.
    """
    n = int(round(window_s / dt))
    fig, axes = plt.subplots(1, len(sets), figsize=(6.4, 4.8), sharex=True)
    axes = np.atleast_1d(axes)

    for ax, (title, chips) in zip(axes, sets.items()):
        rows, labels, bounds = [], [], []
        for chip, df in chips:
            #cols = unique_cols(df)
            #cols = moderate_cols(df)
            cols = moderate_unique_cols(df)
            rows += [df[c].to_numpy()[:n] / 1e6 for c in cols]
            labels += [short_label(c) for c in cols]
            bounds.append((chip, len(rows)))

        im = ax.imshow(np.vstack(rows), aspect="auto", cmap="YlOrRd", vmin=0, vmax=vmax,
                       interpolation="nearest", extent=[0, window_s, len(rows), 0])
        ax.set_yticks(np.arange(len(rows)) + 0.5)
        ax.set_yticklabels(labels, fontsize=10)
        ax.set_xlabel("Time (s)")
        ax.set_xticks(np.arange(0, window_s + 1, 20))
        ax.set_title(title)

        start = 0
        for chip, end in bounds:                                   # chip separator and label
            if end < len(rows):
                ax.axhline(end, color="white", lw=2)
            ax.text(1.01, (start + end) / 2, chip, transform=ax.get_yaxis_transform(),
                    rotation=90, va="center", ha="left")
            start = end

    fig.tight_layout()
    cbar = fig.colorbar(im, ax=axes, fraction=0.025, pad=0.075)
    cbar.set_label("Power (MW)", labelpad=0)
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path, dpi=600, bbox_inches="tight")
    fig.savefig(save_path.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)


dfs = {}
for chip, folder in (("B200", "B_200"), ("H100", "H_100")):
    for case in ("2MW", "norm"):
        df = pd.read_parquet(DATA / folder / "Dataframes" / f"df_{folder}_{case}.parquet")
        dfs[(chip, case)] = to_100MW(df)
        del df

# ---- check: max 100 MW in each set, mean 40 MW in the equal power set ----
for case in ("2MW", "norm"):
    vals = pd.concat([dfs[(c, case)][unique_cols(dfs[(c, case)])] for c in ("B200", "H100")], axis=1)
    #print(f"{case}: {vals.shape[1]} profiles | max {vals.max().max() / 1e6:.2f} MW | "
    #      f"mean {vals.mean().min() / 1e6:.2f} to {vals.mean().max() / 1e6:.2f} MW")

sets = {"(a) Actual power":     [("B200", dfs[("B200", "2MW")]),  ("H100", dfs[("H100", "2MW")])],
        "(b) Equal mean power": [("B200", dfs[("B200", "norm")]), ("H100", dfs[("H100", "norm")])]}

plot_heatmap(sets, FIG_DIR / "Load_profiles_heatmap.png", window_s=60)


def plot_mean_vs_std(data_dir=r"E:\IEEE_GM_2027\Dataset\Data_for_simulation",fig_dir=r"E:\IEEE_GM_2027\Dataset\Figures",
                     file_name="Load_profiles_mean_vs_std.png", factor=50, window_s=900.0, dt=0.02):

    duplicates = ("ImageSize_32", "ModelSize_128", "Deepspeedds_z3", "Lamma_8B", "SeqLength_2048")
    chips = {"B200": ("B_200", "o"), "H100": ("H_100", "s")}  # chip -> (folder, marker)
    sets = {"2MW": ("Actual power", "blue"), "norm": ("Equal mean power", "red")}  # file -> (label, colour)
    n = int(round(window_s / dt))  # first 15 min = repeated block

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    count = 0

    for case, (set_label, colour) in sets.items():
        for chip, (folder, marker) in chips.items():
            df = pd.read_parquet(Path(data_dir) / folder / "Dataframes" / f"df_{folder}_{case}.parquet")
            cols = [c for c in df.columns if c != "time_s" and not c.endswith(duplicates)]
            p = df[cols].to_numpy()[:n] * factor / 1e6  # 2 MW -> 100 MW, in MW
            del df

            mean, std = p.mean(axis=0), p.std(axis=0)
            ax.scatter(mean, std, s=50, marker=marker, color=colour, edgecolor="black",
                       linewidth=0.6, label=f"{set_label}, {chip}", zorder=3)
            count += len(mean)

    ax.set_xlabel("Mean power (MW)")
    ax.set_ylabel("Standard deviation (MW)")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=11)
    fig.tight_layout()

    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(fig_dir / file_name, dpi=600, bbox_inches="tight")
    plt.close(fig)
    print(f"{count} scenarios plotted")

#plot_mean_vs_std()