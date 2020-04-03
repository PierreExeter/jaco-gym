import gym
import jaco_gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2


# first launch Jaco in Gazebo
# roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300

env_id = 'JacoGazebo-v1'
env = gym.make(env_id)
env.reset()

model = PPO2.load("../results/trained_agents/"+env_id)

# Enjoy trained agent
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)

