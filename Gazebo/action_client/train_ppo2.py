import gym
import jaco_gazebo_gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2

env = gym.make('JacoGazebo-v0')

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=1)

model.save("ppo2_cartpole")
model = PPO2.load("ppo2_cartpole")

# Enjoy trained agent
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
