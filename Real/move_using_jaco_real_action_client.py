import rospy
from jaco_real_action_client import JacoRealActionClient


rospy.init_node('jaco_real_action_client_node')
robot_client = JacoRealActionClient()

robot_client.cancel_move()
robot_client.move_arm(0, 180, 180, 0, 0, 0)

