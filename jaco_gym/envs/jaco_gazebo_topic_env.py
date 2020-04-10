import gym
import numpy as np
import random

from gym import error, spaces, utils
from gym.utils import seeding
from jaco_gym.envs.ros_scripts.jaco_gazebo_publish_topic import JacoGazeboPublishTopic



class JacoEnv(gym.Env):

    def __init__(self):
        
        self.robot = JacoGazeboPublishTopic()
        

    def step(self, action):

        # convert to radians    
        action = np.radians(action)

        self.robot.moveJoint(action)
       
        # get state
        self.state = self.robot.read_state()

        # # calculate reward
        # self.tip_position = self.print_tip_pos()

        # self.reward = np.linalg.norm(self.tip_position - self.target_vect)

        # print("tip position: ", self.tip_position)
        # print("target vect: ", self.target_vect)
        # print("reward: ", self.reward)

        # return self.state, self.reward


    def print_tip_pos(self):
        tip_position = self.robot.read_tip_position()
        return np.array(tip_position)


    def reset(self): 

        for i in range(6):
            # self.robot.cancel_move()
            # self.robot.move_arm(0, 180, 180, 0, 0, 0)

            neutral_pos = np.radians([0, 180, 180, 0, 0, 0])

            self.robot.moveJoint(neutral_pos)

        print("Jaco reset to initial position")

        # get state
        self.state = self.robot.read_state()

        # # generate random coordinates of a point in space
        # x_target = random.uniform(-0.49, 0.49)
        # y_target = random.uniform(-0.49, 0.49)
        # z_target = random.uniform(0.69, 1.18)
        
        # self.target_vect = np.array([x_target, y_target, z_target])

        return self.state


    def render(self, mode='human', close=False):
        pass
