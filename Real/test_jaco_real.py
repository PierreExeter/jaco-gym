import gym
import jaco_real_gym
import random
import rospy
# from kinova_client import KinovaClient
# from jaco_real_action_client import JacoRealActionClient

env = gym.make('jacoReal-v0')
rospy.init_node('kinova_controller_angles')

state = env.reset()
print("current state: ", state)

action = [0, 180, 180, 60, 0, 0]
state = env.step(action)
env.print_tip_pos()
print("current state: ", state)


# for t in range(3):

#     # create action
#     ang0 = 0
#     ang1 = 180
#     ang2 = random.randrange(90, 270)
#     ang3 = random.randrange(0, 359)
#     ang4 = random.randrange(0, 359)
#     ang5 = random.randrange(0, 359)
#     action = [ang0, ang1, ang2, ang3, ang4, ang5]
#     print("action sent: ", action)

#     state = env.step(action)
#     print("current state: ", state)


#     print("time step {}".format(t))
