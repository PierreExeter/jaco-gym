import gym
import numpy as np
import random

from gym import error, spaces, utils
from gym.utils import seeding
from jaco_gazebo_action_client import JacoGazeboActionClient


class JacoEnv(gym.Env):


    def __init__(self):
        self.robot = JacoGazeboActionClient()
        

    def step(self, action):

        # convert to radians    
        action = np.radians(action)
        self.robot.move_arm(action)
       
        # get state
        self.observation = self.robot.read_state()

        # calculate reward
        self.tip_coord = self.robot.get_tip_coord()
        self.dist_to_target = np.linalg.norm(self.tip_coord - self.target_vect)
        self.reward = - self.dist_to_target 

        # create info
        self.info = self.tip_coord, self.target_vect

        # create done
        self.done = False
        if self.dist_to_target < 0.01:
            self.done = True
            
        print("tip position: ", self.tip_coord)
        print("target vect: ", self.target_vect)
        print("dist_to_target: ", self.dist_to_target)

        return self.observation, self.reward, self.done, self.info


    def reset(self): 

        self.robot.cancel_move()

        pos = [0, 180, 180, 0, 0, 0]
        pos = np.radians(pos)
        self.robot.move_arm(pos)
        print("Jaco reset to initial position")

        # get observation
        self.observation = self.robot.read_state()

        # generate random coordinates of a point in space
        x_target = random.uniform(-0.49, 0.49)
        y_target = random.uniform(-0.49, 0.49)
        z_target = random.uniform(0.69, 1.18)
        
        self.target_vect = np.array([x_target, y_target, z_target])
        print("Random target coordinates generated")

        return self.observation


    def render(self, mode='human', close=False):
        pass
