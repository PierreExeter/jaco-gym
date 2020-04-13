import gym
import jaco_gym
import random
import numpy as np 
import rospy

from stable_baselines.common.env_checker import check_env


# first launch Jaco in Gazebo with
# roslaunch kinova_gazebo robot_launch_noRender.launch kinova_robotType:=j2n6s300
# roslaunch kinova_gazebo robot_launch_render.launch kinova_robotType:=j2n6s300


# to profile this script
# kernprof -l 4_profiling_test_jaco_gazebo_action_gym.py

# run this to read results
# python -m line_profiler 4_profiling_test_jaco_gazebo_action_gym.py.lprof > profiling_result_test.txt


rospy.init_node("kinova_client", anonymous=True, log_level=rospy.INFO)

env = gym.make('JacoGazebo-v1')

## It will check your custom environment and output additional warnings if needed
# print("starting check")
# check_env(env, warn=True)
# print("check done")


print('Action space:')
print(env.action_space)
print(env.action_space.high)
print(env.action_space.low)

print('State space:')
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)



# obs = env.reset()
# action = env.action_space.sample()
# print('random action:', action)
# obs, reward, done, info = env.step(action)

@profile
def main():

    for episode in range(3):

        obs = env.reset()
        rewards = []

        for t in range(5):

            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)

            print("timestep:", t)
            print("action: ", action)
            print("observation: ", obs)
            print("reward: ", reward)
            print("done: ", done)
            print("info: ", info)

            if done:
                rewards.append(reward)
                break

        print("Episode: {}, Cumulated reward: {}".format(episode, sum(rewards)))
        print("******************")

    env.close()


main()