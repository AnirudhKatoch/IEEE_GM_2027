import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path




plt.rcParams.update({"font.size": 15, "font.family": "Calibri", "axes.labelsize": 15, "axes.titlesize": 15,
                     "xtick.labelsize": 15, "ytick.labelsize": 15, "legend.fontsize": 15})

column = "Image_B200_BatchSize_128"

raw = pd.read_csv(rf"E:\IEEE_GM_2027\Powerfactory\PF_results\{column}.csv", header=[0, 1])

# combine the two header rows: "Inverter (IBR) | Active Power in MW"
raw.columns = ["time_s"] + [f"{elem.split('.')[0]} | {var}" for elem, var in raw.columns[1:]]

# clean the time: round to 10 ms, turn -0.00 into 0.00, drop the double 900.0 row
raw["time_s"] = raw["time_s"].round(2) + 0.0
raw = raw.drop_duplicates("time_s", keep="last")

# 0.00, 0.02, ... 900.00 s
grid = np.round(np.arange(45001) * 0.02, 2)
df = raw.set_index("time_s").reindex(grid).rename_axis("time_s").reset_index()

print(df.columns.tolist())



def read_pf_results(path, dt=0.02, t_end=900.0):
    """Reads a PowerFactory CSV export (two header rows) and returns it on an exact dt grid."""
    raw = pd.read_csv(path, header=[0, 1])
    raw.columns = ["time_s"] + [f"{elem.split('.')[0]} | {var}" for elem, var in raw.columns[1:]]

    raw["time_s"] = raw["time_s"].round(2) + 0.0             # -0.00 -> 0.00
    raw = raw.drop_duplicates("time_s", keep="last")         # double 900.0 row

    grid = np.round(np.arange(int(round(t_end / dt)) + 1) * dt, 2)   # 0.00 ... 900.00 s
    return raw.set_index("time_s").reindex(grid).rename_axis("time_s").reset_index()


def _find(cols, element, key):
    """First column of the given element whose variable name contains key."""
    return next((c for c in cols if c.startswith(element) and key in c), None)


def plot_pf_results(df, name, fig_dir, until_s=None):
    """
    1) every exported variable in its own subplot
    2) inverter P vs data centre P, plus the share the inverter carries
    until_s: plot only up to this time (None = everything)
    """
    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)

    d = df if until_s is None else df[df["time_s"] <= until_s]
    t_max = d["time_s"].max()
    scale, unit = (60, "min") if t_max > 300 else (1, "s")
    t = d["time_s"] / scale
    tag = "full" if until_s is None else f"0-{until_s:g}s"
    cols = [c for c in df.columns if c != "time_s"]

    # ---- 1) all variables ----
    fig, axes = plt.subplots(len(cols), 1, figsize=(10, 2.2 * len(cols)), sharex=True)
    for ax, c in zip(np.atleast_1d(axes), cols):
        ax.plot(t, d[c], lw=0.6, color="black")
        ax.set_title(c, fontsize=12)
        ax.grid(alpha=0.3)
    np.atleast_1d(axes)[-1].set_xlabel(f"Time ({unit})")
    np.atleast_1d(axes)[-1].set_xlim(0, t_max / scale)
    fig.tight_layout()
    fig.savefig(fig_dir / f"{name}_all_{tag}.png", dpi=200)
    plt.close(fig)

    # ---- 2) inverter vs load ----
    p_inv = _find(cols, "Inverter (IBR)", "Total Active Power")
    p_load = _find(cols, "Data center", "Total Active Power") or _find(cols, "Data center", "Active Power")
    if p_inv is None or p_load is None:
        print("Inverter or load active power not found, skipping comparison plot. Columns:", cols)
        return

    share = 100 * d[p_inv] / d[p_load]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    ax1.plot(t, d[p_load], lw=0.8, color="black", label="Data centre")
    ax1.plot(t, d[p_inv], lw=0.8, color="tab:red", label="Inverter", alpha=0.8)
    ax1.set_ylabel("Active power (MW)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(t, share, lw=0.8, color="tab:blue")
    ax2.set_ylabel("Inverter share (%)")
    ax2.set_xlabel(f"Time ({unit})")
    ax2.set_xlim(0, t_max / scale)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(fig_dir / f"{name}_P_inverter_vs_load_{tag}.png", dpi=200)
    plt.close(fig)

    print(f"{name} ({tag}): inverter share mean {share.mean():.1f} %, "
          f"min {share.min():.1f} %, max {share.max():.1f} %")


def compare_load_with_original(df_pf, p_orig, name, fig_dir, until_s=120, dt=0.02,pf_col="Data center | Total Active Power in MW"):
    """
    Compares the load power from PowerFactory with the original profile written to the .txt file.
    df_pf  : PowerFactory results on the 0.02 s grid (from read_pf_results)
    p_orig : original profile in MW, one value per 0.02 s, starting at t = 0
    """
    fig_dir = Path(fig_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)

    n = min(len(p_orig), len(df_pf))                     # PF has 45001 points (incl. 900.00 s), original 45000
    t = np.arange(n) * dt
    p_pf = df_pf[pf_col].to_numpy()[:n]
    p_or = np.asarray(p_orig, dtype=float)[:n]

    # ---- check over the whole run, also for a one-sample shift ----
    for lag in (0, 1):
        err = p_pf[lag:] - p_or[:n - lag]
        print(f"lag {lag} ({lag * dt:.2f} s): max |error| {np.abs(err).max():.4f} MW, "
              f"mean |error| {np.abs(err).mean():.4f} MW, RMS {np.sqrt(np.mean(err ** 2)):.4f} MW")
    print(f"Energy: PowerFactory {p_pf.sum() * dt / 3600:.4f} MWh, original {p_or.sum() * dt / 3600:.4f} MWh")

    # ---- plot up to until_s ----
    m = t <= until_s
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
    ax1.plot(t[m], p_or[m], lw=1.5, color="black", label="Original profile")
    ax1.plot(t[m], p_pf[m], lw=0.8, color="tab:red", ls="--", label="PowerFactory load")
    ax1.set_ylabel("Active power (MW)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(t[m], p_pf[m] - p_or[m], lw=0.8, color="tab:blue")
    ax2.set_ylabel("Difference (MW)")
    ax2.set_xlabel("Time (s)")
    ax2.set_xlim(0, until_s)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(fig_dir / f"{name}_load_vs_original_0-{until_s:g}s.png", dpi=200)
    plt.close(fig)


##########################
# For running
##########################

column = "Image_B200_BatchSize_128"
results_dir = Path(r"E:\IEEE_GM_2027\Powerfactory\PF_results")
fig_dir = Path(r"E:\IEEE_GM_2027\Powerfactory\Figures")

df = read_pf_results(results_dir / f"{column}.csv")

plot_pf_results(df, column, fig_dir, until_s=120)    # zoom on the first 2 min

# ---- original profile, exactly as written to the .txt file ----
df_orig = pd.read_parquet(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation\B_200\Dataframes\df_B_200_2MW.parquet")
p = df_orig[column].to_numpy()[:45000] * 50 / 1e6   # 15 min, 50 units -> MW
del df_orig

compare_load_with_original(df, p, column, fig_dir, until_s=120)


