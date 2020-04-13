import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
from sklearn import preprocessing



# plot learning curves

df1 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_1_norm/ppo2/all_rewards.csv")
df2 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8_norm/ppo2/all_rewards.csv")
df3 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8/ppo2/all_rewards.csv")


# apply curve smoothing by moving average
df1['mean_reward'] = df1['mean_reward'].rolling(window=50).mean()
df2['mean_reward'] = df2['mean_reward'].rolling(window=50).mean()
df3['mean_reward'] = df3['mean_reward'].rolling(window=50).mean()



plt.figure(1)
ax1 = plt.axes()

df1.plot(x='timesteps', y='mean_reward', ax=ax1, label="1 env norm")
df2.plot(x='timesteps', y='mean_reward', ax=ax1, label="8 env norm")
df3.plot(x='timesteps', y='mean_reward', ax=ax1, label="8 env")

plt.ylabel("Episode reward")
plt.savefig("./logs/ppo2/learning_curves_by_env.png", dpi=100)



# plot training stats

ff1 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_1_norm/ppo2/results_seed_exp.csv")
ff2 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8_norm/ppo2/results_seed_exp.csv")
ff3 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8/ppo2/results_seed_exp.csv")


print(ff1)

ff_list = [
    ff1,
    ff2,
    ff3,
 ]


ff = pd.concat(ff_list, axis=0)

ff['exp type'] =  [
    "1 env",
    "8 env norm",
    "8 env",
]



# min max scaled
ff['mean reward scaled'] = (ff['mean reward']-ff['mean reward'].min())/(ff['mean reward'].max()-ff['mean reward'].min())
ff['mean train walltime scaled'] = (ff['mean train walltime (s)']-ff['mean train walltime (s)'].min())/(ff['mean train walltime (s)'].max()-ff['mean train walltime (s)'].min())

# standard scaler
# ff['mean reward scaled'] = (ff['mean reward']-ff['mean reward'].mean())/ff['mean reward'].std()
# ff['mean train walltime scaled'] = (ff['mean train walltime (s)']-ff['mean train walltime (s)'].mean())/ff['mean train walltime (s)'].std()

ff['efficiency (reward / s)'] = ff['mean reward'] / ff['mean train walltime (s)']
# ff['efficiency scaled'] = 1 / (ff['mean reward scaled'] * ff['mean train walltime scaled'])

ff['efficiency scaled'] = (ff['efficiency (reward / s)']-ff['efficiency (reward / s)'].min())/(ff['efficiency (reward / s)'].max()-ff['efficiency (reward / s)'].min())

print(ff)


ax = ff.plot.bar(x='exp type', y='mean reward', yerr='std reward (seed)', rot=45)
plt.ylabel("Mean reward")
plt.tight_layout()
plt.savefig("./logs/ppo2/reward_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean reward scaled', rot=45)
plt.ylabel("Mean reward scaled")
plt.tight_layout()
plt.savefig("./logs/ppo2/reward_by_exp_type_scaled.png", dpi=100)



ax = ff.plot.bar(x='exp type', y='mean train walltime (s)', yerr='std train walltime (s)', rot=45)
plt.ylabel("Mean train time (s)")
plt.tight_layout()
plt.savefig("./logs/ppo2/walltime_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean train walltime scaled', rot=45)
plt.ylabel("Mean train time scaled")
plt.tight_layout()
plt.savefig("./logs/ppo2/walltime_by_exp_type_scaled.png", dpi=100)


ax = ff.plot.bar(x='exp type', y='efficiency (reward / s)', rot=45)
plt.ylabel("Eficiency (reward / s)")
plt.tight_layout()
plt.savefig("./logs/ppo2/efficiency_by_exp_type.png", dpi=100)
# plt.show()


ax = ff.plot.bar(x='exp type', y='efficiency scaled', rot=45)
plt.ylabel("Eficiency (scaled)")
plt.tight_layout()
plt.savefig("./logs/ppo2/efficiency_by_exp_type_scaled.png", dpi=100)
# plt.show()





