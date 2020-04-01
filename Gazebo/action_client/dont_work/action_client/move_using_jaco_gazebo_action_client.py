import rospy
from jaco_gazebo_action_client import JacoGazeboActionClient


rospy.init_node('jaco_gazebo_action_client_node')
robot_client = JacoGazeboActionClient()

robot_client.cancel_move()
robot_client.move_arm(0, 180, 180, 0, 0, 0)

