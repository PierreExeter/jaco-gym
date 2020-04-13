import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


# file_path = "logs/a2c/Pendulum-v0_1_opti_1M_100trials_noPruning/a2c/"
# report_name = "report_Pendulum-v0_100-trials-1000000-tpe-none_1586498287.csv"

# file_path = "logs/a2c/Pendulum-v0_1_opti_2M_20trials/"
# report_name = "report_Pendulum-v0_20-trials-2000000-tpe-median_1586456075.csv"

file_path = "logs/a2c/Pendulum-v0_1_opti_100000_20trials/a2c/"
report_name = "report_Pendulum-v0_20-trials-100000-tpe-median_1586458021.csv"



df = pd.read_csv(file_path+report_name)

print(df)

cols = df.columns
print(cols)

for col in cols[5:-2]:
    print(col)

    df.plot.scatter(x=col, y='value')
    plt.savefig(file_path+col+"_vs_value.png", dpi=100)
    # plt.show()