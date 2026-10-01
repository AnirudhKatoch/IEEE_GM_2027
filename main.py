import gc
import time
import traceback
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import pandas as pd


def run_one(column, load, results_base):
    """Runs one complete simulation in a fresh process."""
    import matplotlib
    matplotlib.use("Agg")                  # no GUI windows in background processes

    from mother_function import mother_function   # imported inside the worker process

    t0 = time.time()
    try:
        mother_function(Load=load, sim_name=column, results_base=results_base)
        return column, "OK", time.time() - t0
    except Exception:
        return column, traceback.format_exc(), time.time() - t0


if __name__ == "__main__":                 # required on Windows for new processes

    base_dir = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")
    out_root = Path(r"E:\IEEE_GM_2027\IEEE_results\Results_run2")   # new folder: old results stay untouched
    until_s = 43200                                                  # simulate only up to this time [s]

    SETS = {  # set -> {chip folder: parquet file}
        "2MW":  {"H_100": "df_H_100_2MW.parquet",  "B_200": "df_B_200_2MW.parquet"},
        "norm": {"H_100": "df_H_100_norm.parquet", "B_200": "df_B_200_norm.parquet"},
    }

    all_results = []

    for set_name, files in SETS.items():
        results_base = out_root / set_name / "Dataframes"         # one folder per set -> no overwriting
        results_base.mkdir(parents=True, exist_ok=True)

        for chip, file in files.items():
            Location = base_dir / chip / "Dataframes"

            df = pd.read_parquet(Location / file)
            df = df[df["time_s"] < until_s].reset_index(drop=True)
            print(f"\n===== {set_name} | {chip}: {file} | {len(df)} steps = {len(df) * 0.02:.0f} s =====")

            columns = [c for c in df.columns if c != "time_s"]
            loads = {c: df[c].to_numpy(dtype=np.float64) for c in columns}
            del df
            gc.collect()

            for i, column in enumerate(columns, start=1):
                print(f"\n[{set_name} | {chip} {i}/{len(columns)}] Starting {column}")

                # one worker, one task -> new clean process for every simulation
                with ProcessPoolExecutor(max_workers=1) as pool:
                    name, status, runtime = pool.submit(run_one, column, loads[column], str(results_base)).result()

                ok = status == "OK"
                all_results.append({"set": set_name, "chip": chip, "profile": name,
                                    "status": "OK" if ok else "FAILED", "runtime_s": round(runtime, 1)})
                print(f"[{set_name} | {chip} {i}/{len(columns)}] {name}: {'OK' if ok else 'FAILED'} in {runtime:.1f} s")
                if not ok:
                    print(status)          # full error, the loop continues with the next profile

            del loads
            gc.collect()

        # summary per set
        pd.DataFrame([r for r in all_results if r["set"] == set_name]) \
          .to_csv(out_root / set_name / "simulation_run_summary.csv", index=False, sep=";")

    all_summary = pd.DataFrame(all_results)
    all_summary.to_csv(out_root / "simulation_run_summary_all.csv", index=False, sep=";")
    print("\n", all_summary)