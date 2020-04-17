import gym
import numpy as np
import random

from gym import error, spaces, utils
from gym.utils import seeding
from jaco_gym.envs.ros_scripts.jaco_gazebo_action_client import JacoGazeboActionClient



class JacoEnv(gym.Env):

    def __init__(self):

        self.robot = JacoGazeboActionClient()

        self.action_dim = 6
        # self.obs_dim = 36
        self.obs_dim = 12   # when using read_state_simple

        high = np.ones([self.action_dim])
        self.action_space = gym.spaces.Box(-high, high)
        
        high = np.inf * np.ones([self.obs_dim])
        self.observation_space = gym.spaces.Box(-high, high)
        

    def convert_action_to_deg(self, a, OldMin, OldMax, NewMin, NewMax):
    
        OldRange = (OldMax - OldMin)  
        NewRange = (NewMax - NewMin)  

        return (((a - OldMin) * NewRange) / OldRange) + NewMin
    
    
    def action2deg(self, action):
        action[0] = self.convert_action_to_deg(action[0], OldMin=-1, OldMax=1, NewMin=0, NewMax=360)
        action[1] = 180
        action[2] = self.convert_action_to_deg(action[2], OldMin=-1, OldMax=1, NewMin=90, NewMax=270)
        action[3] = self.convert_action_to_deg(action[3], OldMin=-1, OldMax=1, NewMin=0, NewMax=360)
        action[4] = self.convert_action_to_deg(action[4], OldMin=-1, OldMax=1, NewMin=0, NewMax=360)
        action[5] = self.convert_action_to_deg(action[5], OldMin=-1, OldMax=1, NewMin=0, NewMax=360)

        return action


    def step(self, action):

        # convert action from range [-1, 1] to [0, 360] 
        self.action = self.action2deg(action)

        # convert to radians    
        self.action = np.radians(self.action)

        # move arm 
        self.robot.move_arm(self.action)
       
        # get state
        # self.observation = self.robot.read_state()
        self.observation = self.robot.read_state_simple()   # only return 12 values instead of 36

        # calculate reward
        self.tip_coord = self.robot.get_tip_coord()
        self.dist_to_target = np.linalg.norm(self.tip_coord - self.target_vect)
        self.reward = - self.dist_to_target 

        # create info
        self.info = {"tip coordinates": self.tip_coord, "target coordinates": self.target_vect}

        # create done
        self.done = False

        # IF DEFINING DONE AS FOLLOWS, THE EPISODE ENDS EARLY AND A GOOD AGENT WILL RECEIVED A PENALTY FOR BEING GOOD
        # COOMENT THIS
        # if self.dist_to_target < 0.01:
            # self.done = True
            
        # print("tip position: ", self.tip_coord)
        # print("target vect: ", self.target_vect)
        # print("dist_to_target: ", self.dist_to_target)

        return self.observation, self.reward, self.done, self.info


    def reset(self): 

        self.robot.cancel_move()

        pos = [0, 180, 180, 0, 0, 0]
        pos = np.radians(pos)
        self.robot.move_arm(pos)
        print("Jaco reset to initial position")

        # get observation
        # self.obs = self.robot.read_state()
        self.obs = self.robot.read_state_simple()

        # generate random coordinates of a point in space
        # limits of real robot
        # x_target = random.uniform(-0.49, 0.49)
        # y_target = random.uniform(-0.49, 0.49)
        # z_target = random.uniform(0.69, 1.18)

        # limits in Gazebo
        x_target = random.uniform(-0.335, 0.335)
        y_target = random.uniform(-0.337, 0.337)
        z_target = random.uniform(0.686, 1.021)
        
        self.target_vect = np.array([x_target, y_target, z_target])
        print("Random target coordinates generated")

        # if testing: graphically move the sphere target, if training, comment this line
        # self.robot.move_sphere(self.target_vect)

        return self.obs


    def render(self, mode='human', close=False):
        pass
