import gc
import time
import traceback
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import pandas as pd

def run_one(column, load):
    """Runs one complete simulation in a fresh process."""
    import matplotlib
    matplotlib.use("Agg")                  # no GUI windows in background processes

    from mother_function import mother_function   # imported inside the worker process

    t0 = time.time()
    try:
        mother_function(Load=load, sim_name=column)
        return column, "OK", time.time() - t0
    except Exception:
        return column, traceback.format_exc(), time.time() - t0


if __name__ == "__main__":                 # required on Windows for new processes

    base_dir = Path(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation")
    files = {
        "H_100": "df_H_100_2MW.parquet",
        "B_200": "df_B_200_2MW.parquet",
    }
    until_s = 3600                           # simulate only up to this time [s]

    all_results = []

    for chip, file in files.items():
        Location = base_dir / chip / "Dataframes"

        df = pd.read_parquet(Location / file)
        df = df[df["time_s"] < until_s].reset_index(drop=True)
        print(f"\n===== {chip}: {file} | {len(df)} steps = {len(df) * 0.02:.0f} s =====")

        columns = [c for c in df.columns if c != "time_s"]
        loads = {c: df[c].to_numpy(dtype=np.float64) for c in columns}
        del df
        gc.collect()

        results = []
        for i, column in enumerate(columns, start=1):
            print(f"\n[{chip} {i}/{len(columns)}] Starting {column}")

            # one worker, one task -> new clean process for every simulation
            with ProcessPoolExecutor(max_workers=1) as pool:
                name, status, runtime = pool.submit(run_one, column, loads[column]).result()

            ok = status == "OK"
            results.append({"chip": chip, "profile": name,
                            "status": "OK" if ok else "FAILED", "runtime_s": round(runtime, 1)})
            print(f"[{chip} {i}/{len(columns)}] {name}: {'OK' if ok else 'FAILED'} in {runtime:.1f} s")
            if not ok:
                print(status)              # full error, the loop continues with the next profile

        summary = pd.DataFrame(results)
        summary.to_csv(Location / "simulation_run_summary.csv", index=False, sep=";")
        all_results.extend(results)

        del loads
        gc.collect()

    all_summary = pd.DataFrame(all_results)
    all_summary.to_csv(base_dir / "simulation_run_summary_all.csv", index=False, sep=";")
    print("\n", all_summary)