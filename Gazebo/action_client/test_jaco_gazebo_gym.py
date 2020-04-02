import gym
import jaco_gazebo_gym
import random
import rospy
import numpy as np 


env = gym.make('JacoGazebo-v0')


# obs = env.reset()
# print("observation: ", obs)

# action = [0, 180, 180, 0, 0, 0]
# obs, reward, done, info = env.step(action)


for episode in range(3):

    obs = env.reset()
    rewards = []

    for t in range(10):

        # create action
        ang0 = random.randrange(0, 360)
        ang1 = 180    # random.randrange(90, 180)
        ang2 = random.randrange(90, 270)
        ang3 = random.randrange(0, 360)
        ang4 = random.randrange(0, 360)
        ang5 = random.randrange(0, 360)

        action = [ang0, ang1, ang2, ang3, ang4, ang5]

        obs, reward, done, info = env.step(action)

        print("timestep:", t)
        print("action: ", action)
        print("observation: ", obs)
        print("reward: ", reward)
        print("done: ", done)
        print("info: ", info)

        rewards.append(reward)

    print("Episode: {}, Cumulated reward: {}".format(episode, sum(rewards)))
    print("******************")