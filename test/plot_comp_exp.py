import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
from sklearn import preprocessing



# plot learning curves

df1 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_1/a2c/all_rewards.csv")
df2 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_2/a2c/all_rewards.csv")
df3 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_3/a2c/all_rewards.csv")
df4 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_4/a2c/all_rewards.csv")
df5 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_5/a2c/all_rewards.csv")
df6 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_6/a2c/all_rewards.csv")
df7 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_7/a2c/all_rewards.csv")
df8 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_8/a2c/all_rewards.csv")

df9 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_1_norm/a2c/all_rewards.csv")
df10 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_8_norm/a2c/all_rewards.csv")



# apply curve smoothing by moving average
df1['mean_reward'] = df1['mean_reward'].rolling(window=50).mean()
df2['mean_reward'] = df2['mean_reward'].rolling(window=50).mean()
df3['mean_reward'] = df3['mean_reward'].rolling(window=50).mean()
df4['mean_reward'] = df4['mean_reward'].rolling(window=50).mean()
df5['mean_reward'] = df5['mean_reward'].rolling(window=50).mean()
df6['mean_reward'] = df6['mean_reward'].rolling(window=50).mean()
df7['mean_reward'] = df7['mean_reward'].rolling(window=50).mean()
df8['mean_reward'] = df8['mean_reward'].rolling(window=50).mean()
df9['mean_reward'] = df9['mean_reward'].rolling(window=50).mean()
df10['mean_reward'] = df10['mean_reward'].rolling(window=50).mean()




plt.figure(1)
ax1 = plt.axes()

df1.plot(x='timesteps', y='mean_reward', ax=ax1, label="1 env")
df2.plot(x='timesteps', y='mean_reward', ax=ax1, label="2 env")
df3.plot(x='timesteps', y='mean_reward', ax=ax1, label="3 env")
df4.plot(x='timesteps', y='mean_reward', ax=ax1, label="4 env")
df5.plot(x='timesteps', y='mean_reward', ax=ax1, label="5 env")
df6.plot(x='timesteps', y='mean_reward', ax=ax1, label="6 env")
df7.plot(x='timesteps', y='mean_reward', ax=ax1, label="7 env")
df8.plot(x='timesteps', y='mean_reward', ax=ax1, label="8 env")
plt.ylabel("Episode reward")

plt.savefig("./logs/a2c/learning_curves_by_env.png", dpi=100)

plt.figure(2)
ax2 = plt.axes()

df1.plot(x='timesteps', y='mean_reward', ax=ax2, label="1 env")
df9.plot(x='timesteps', y='mean_reward', ax=ax2, label="1 env norm")

plt.ylabel("Episode reward")
plt.savefig("./logs/a2c/learning_curves_norm1.png", dpi=100)


plt.figure(3)
ax3 = plt.axes()

df8.plot(x='timesteps', y='mean_reward', ax=ax3, label="8 env")
df10.plot(x='timesteps', y='mean_reward', ax=ax3, label="8 env norm")


plt.ylabel("Episode reward")
plt.savefig("./logs/a2c/learning_curves_norm8.png", dpi=100)


# plot training stats

ff1 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_1/a2c/results_seed_exp.csv")
ff2 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_2/a2c/results_seed_exp.csv")
ff3 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_3/a2c/results_seed_exp.csv")
ff4 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_4/a2c/results_seed_exp.csv")
ff5 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_5/a2c/results_seed_exp.csv")
ff6 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_6/a2c/results_seed_exp.csv")
ff7 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_7/a2c/results_seed_exp.csv")
ff8 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_8/a2c/results_seed_exp.csv")
ff8_8 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_8_8nodes/a2c/results_seed_exp.csv")

ff9 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_1_norm/a2c/results_seed_exp.csv")
ff10 = pd.read_csv("./logs/a2c/Pendulum-v0_Env_8_norm/a2c/results_seed_exp.csv")

print(ff1)

ff_list = [
    ff1,
    ff2,
    ff3,
    ff4,
    ff5,
    ff6,
    ff7,
    ff8,
    ff8_8,
    ff9,
    ff10
 ]


ff = pd.concat(ff_list, axis=0)

ff['exp type'] =  [
    "1 env",
    "2 env",
    "3 env",
    "4 env",
    "5 env",
    "6 env",
    "7 env",
    "8 env",
    "8 env 8 nodes",
    "1 env norm",
    "8 env norm"
]



# min max scaled
ff['mean reward scaled'] = (ff['mean reward']-ff['mean reward'].min())/(ff['mean reward'].max()-ff['mean reward'].min())
ff['mean train walltime scaled'] = (ff['mean train walltime (s)']-ff['mean train walltime (s)'].min())/(ff['mean train walltime (s)'].max()-ff['mean train walltime (s)'].min())

# standard scaler
# ff['mean reward scaled'] = (ff['mean reward']-ff['mean reward'].mean())/ff['mean reward'].std()
# ff['mean train walltime scaled'] = (ff['mean train walltime (s)']-ff['mean train walltime (s)'].mean())/ff['mean train walltime (s)'].std()

ff['efficiency (reward / s)'] = 1/ (-1* ff['mean reward'] * ff['mean train walltime (s)'])
# ff['efficiency scaled'] = 1 / (ff['mean reward scaled'] * ff['mean train walltime scaled'])

ff['efficiency scaled'] = (ff['efficiency (reward / s)']-ff['efficiency (reward / s)'].min())/(ff['efficiency (reward / s)'].max()-ff['efficiency (reward / s)'].min())

print(ff)


ax = ff.plot.bar(x='exp type', y='mean reward', yerr='std reward (seed)', rot=45)
plt.ylabel("Mean reward")
plt.tight_layout()
plt.savefig("./logs/a2c/reward_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean reward scaled', rot=45)
plt.ylabel("Mean reward scaled")
plt.tight_layout()
plt.savefig("./logs/a2c/reward_by_exp_type_scaled.png", dpi=100)



ax = ff.plot.bar(x='exp type', y='mean train walltime (s)', yerr='std train walltime (s)', rot=45)
plt.ylabel("Mean train time (s)")
plt.tight_layout()
plt.savefig("./logs/a2c/walltime_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean train walltime scaled', rot=45)
plt.ylabel("Mean train time scaled")
plt.tight_layout()
plt.savefig("./logs/a2c/walltime_by_exp_type_scaled.png", dpi=100)


ax = ff.plot.bar(x='exp type', y='efficiency (reward / s)', rot=45)
plt.ylabel("Eficiency (reward / s)")
plt.tight_layout()
plt.savefig("./logs/a2c/efficiency_by_exp_type.png", dpi=100)
# plt.show()


ax = ff.plot.bar(x='exp type', y='efficiency scaled', rot=45)
plt.ylabel("Eficiency (scaled)")
plt.tight_layout()
plt.savefig("./logs/a2c/efficiency_by_exp_type_scaled.png", dpi=100)
# plt.show()





