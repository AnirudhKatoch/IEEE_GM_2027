import numpy as np, pandas as pd

df = pd.read_parquet(r"E:\IEEE_GM_2027\Dataset\Data_for_simulation\B_200\Dataframes\df_B_200_2MW_15min.parquet")


col = "Image_B200_BatchSize_128"                         # profile to test
p = df[col].to_numpy()[:45000] * 50 / 1e6                # 15 min, 50 units -> MW
t = np.arange(len(p)) * 0.02

with open(rf"E:\IEEE_GM_2027\Powerfactory\Datasets\{col}.txt", "w") as f:
    f.write("1\n")                                 # number of signals
    for ti, pi in zip(t, p):
        f.write(f"{ti:.2f} {pi:.6f}\n")            # decimal point, space-separated
print(p[0], p.min(), p.max())                      # p[0] is needed in step 5


