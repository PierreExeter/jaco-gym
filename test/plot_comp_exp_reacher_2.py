import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
from sklearn import preprocessing



# plot learning curves

df1 = pd.read_csv("logs/a2c/Reacher2Dof-v0_Env_8_norm/a2c/all_rewards.csv")
df2 = pd.read_csv("logs/acktr/Reacher2Dof-v0_Env_8_norm/acktr/all_rewards.csv")
# df3 = pd.read_csv("logs/ddpg/Reacher2Dof-v0_Env_8_norm/ddpg/all_rewards.csv")
df4 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8_norm/ppo2/all_rewards.csv")
# df5 = pd.read_csv("logs/sac/Reacher2Dof-v0_Env_8_norm/sac/all_rewards.csv")
# df6 = pd.read_csv("logs/td3/Reacher2Dof-v0_Env_8_norm/td3/all_rewards.csv")
# df7 = pd.read_csv("logs/trpo/Reacher2Dof-v0_Env_8_norm/trpo/all_rewards.csv")


# df8 = pd.read_csv("logs/a2c/Reacher2Dof-v0_Env_8/a2c/all_rewards.csv")
# df9 = pd.read_csv("logs/acktr/Reacher2Dof-v0_Env_8/acktr/all_rewards.csv")
# df10 = pd.read_csv("logs/ddpg/Reacher2Dof-v0_Env_8/ddpg/all_rewards.csv")
# df11 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8/ppo2/all_rewards.csv")
# df12 = pd.read_csv("logs/sac/Reacher2Dof-v0_Env_8/sac/all_rewards.csv")
# df13 = pd.read_csv("logs/td3/Reacher2Dof-v0_Env_8/td3/all_rewards.csv")
# df14 = pd.read_csv("logs/trpo/Reacher2Dof-v0_Env_8/trpo/all_rewards.csv")



# apply curve smoothing by moving average

def smooth_reward(df):
    df['mean_reward'] = df['mean_reward'].rolling(window=50).mean()


smooth_reward(df1)
smooth_reward(df2)
# smooth_reward(df3)
smooth_reward(df4)
# smooth_reward(df5)
# smooth_reward(df6)
# smooth_reward(df7)
# smooth_reward(df8)
# smooth_reward(df9)
# smooth_reward(df10)
# smooth_reward(df11)
# smooth_reward(df12)
# smooth_reward(df13)
# smooth_reward(df14)




plt.figure(1)
ax1 = plt.axes()

df1.plot(x='timesteps', y='mean_reward', ax=ax1, label="a2c norm")
df2.plot(x='timesteps', y='mean_reward', ax=ax1, label="acktr norm")
# df3.plot(x='timesteps', y='mean_reward', ax=ax1, label="ddpg norm")
df4.plot(x='timesteps', y='mean_reward', ax=ax1, label="ppo2 norm")
# df5.plot(x='timesteps', y='mean_reward', ax=ax1, label="sac norm")
# df6.plot(x='timesteps', y='mean_reward', ax=ax1, label="td3 norm")
# df7.plot(x='timesteps', y='mean_reward', ax=ax1, label="trpo norm")

# df8.plot(x='timesteps', y='mean_reward', ax=ax1, label="a2c norm")
# df9.plot(x='timesteps', y='mean_reward', ax=ax1, label="acktr norm")
# df10.plot(x='timesteps', y='mean_reward', ax=ax1, label="ddpg norm")
# df11.plot(x='timesteps', y='mean_reward', ax=ax1, label="ppo2 norm")
# df12.plot(x='timesteps', y='mean_reward', ax=ax1, label="sac norm")
# df13.plot(x='timesteps', y='mean_reward', ax=ax1, label="td3 norm")
# df14.plot(x='timesteps', y='mean_reward', ax=ax1, label="trpo norm")


plt.ylabel("Episode reward")
plt.savefig("./logs/reacher_benchmark/learning_curves_by_env.png", dpi=100)



# plot training stats

ff1 = pd.read_csv("logs/a2c/Reacher2Dof-v0_Env_8_norm/a2c/results_seed_exp.csv")
ff2 = pd.read_csv("logs/acktr/Reacher2Dof-v0_Env_8_norm/acktr/results_seed_exp.csv")
# ff3 = pd.read_csv("logs/ddpg/Reacher2Dof-v0_Env_8_norm/ddpg/results_seed_exp.csv")
ff4 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8_norm/ppo2/results_seed_exp.csv")
# ff5 = pd.read_csv("logs/sac/Reacher2Dof-v0_Env_8_norm/sac/results_seed_exp.csv")
# ff6 = pd.read_csv("logs/td3/Reacher2Dof-v0_Env_8_norm/td3/results_seed_exp.csv")
# ff7 = pd.read_csv("logs/trpo/Reacher2Dof-v0_Env_8_norm/trpo/results_seed_exp.csv")

# ff8 = pd.read_csv("logs/a2c/Reacher2Dof-v0_Env_8/a2c/results_seed_exp.csv")
# ff9 = pd.read_csv("logs/acktr/Reacher2Dof-v0_Env_8/acktr/results_seed_exp.csv")
# ff10 = pd.read_csv("logs/ddpg/Reacher2Dof-v0_Env_8/ddpg/results_seed_exp.csv")
# ff11 = pd.read_csv("logs/ppo2/Reacher2Dof-v0_Env_8/ppo2/results_seed_exp.csv")
# ff12 = pd.read_csv("logs/sac/Reacher2Dof-v0_Env_8/sac/results_seed_exp.csv")
# ff13 = pd.read_csv("logs/td3/Reacher2Dof-v0_Env_8/td3/results_seed_exp.csv")
# ff14 = pd.read_csv("logs/trpo/Reacher2Dof-v0_Env_8/trpo/results_seed_exp.csv")



print(ff1)

ff_list = [
    ff1,
    ff2,
    # ff3,
    ff4,
    # ff5,
    # ff6,
    # ff7,
    # ff8,
    # ff9,
    # ff10,
    # ff11,
    # ff12,
    # ff13,
    # ff14,
 ]


ff = pd.concat(ff_list, axis=0)

ff['exp type'] =  [
    "a2c norm",
    "acktr norm",
    # "ddpg norm",
    "ppo2 norm",
    # "sac norm",
    # "td3 norm",
    # "trpo norm",
    # "a2c",
    # "acktr",
    # "ddpg",
    # "ppo2",
    # "sac",
    # "td3",
    # "trpo",
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
plt.savefig("./logs/reacher_benchmark/reward_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean reward scaled', rot=45)
plt.ylabel("Mean reward scaled")
plt.tight_layout()
plt.savefig("./logs/reacher_benchmark/reward_by_exp_type_scaled.png", dpi=100)



ax = ff.plot.bar(x='exp type', y='mean train walltime (s)', yerr='std train walltime (s)', rot=45)
plt.ylabel("Mean train time (s)")
plt.tight_layout()
plt.savefig("./logs/reacher_benchmark/walltime_by_exp_type.png", dpi=100)
# plt.show()

ax = ff.plot.bar(x='exp type', y='mean train walltime scaled', rot=45)
plt.ylabel("Mean train time scaled")
plt.tight_layout()
plt.savefig("./logs/reacher_benchmark/walltime_by_exp_type_scaled.png", dpi=100)


ax = ff.plot.bar(x='exp type', y='efficiency (reward / s)', rot=45)
plt.ylabel("Eficiency (reward / s)")
plt.tight_layout()
plt.savefig("./logs/reacher_benchmark/efficiency_by_exp_type.png", dpi=100)
# plt.show()


ax = ff.plot.bar(x='exp type', y='efficiency scaled', rot=45)
plt.ylabel("Eficiency (scaled)")
plt.tight_layout()
plt.savefig("./logs/reacher_benchmark/efficiency_by_exp_type_scaled.png", dpi=100)
# plt.show()





