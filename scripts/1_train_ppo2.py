import gym
import jaco_gym
import os
import rospy

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.bench import Monitor
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2


# first launch Jaco in Gazebo with
# roslaunch kinova_gazebo robot_launch_noRender.launch kinova_robotType:=j2n6s300
# roslaunch kinova_gazebo robot_launch_render.launch kinova_robotType:=j2n6s300


rospy.init_node("kinova_client", anonymous=True, log_level=rospy.INFO)

env_id = 'JacoGazebo-v1'

# Create log dir
log_dir = "../results/"+env_id+"/"
os.makedirs(log_dir, exist_ok=True)

env = gym.make(env_id)
env = Monitor(env, filename=log_dir, allow_early_resets=True)
env = DummyVecEnv([lambda: env])

env.reset()

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=10000)

model.save(log_dir+env_id)

env.close()
