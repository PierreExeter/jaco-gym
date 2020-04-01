#! /usr/bin/env python

import rospy
import actionlib
from kinova_msgs.msg import ArmJointAnglesGoal, ArmJointAnglesAction
from geometry_msgs.msg import PoseStamped
from trajectory_msgs.msg import JointTrajectory
from control_msgs.msg import FollowJointTrajectoryActionGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from std_srvs.srv import Empty

class JacoGazeboActionClient:

  def __init__(self):

    # with Gazebo
    self.topic_name = '/j2n6s300/effort_joint_trajectory_controller/follow_joint_trajectory/goal'
    # self.client = actionlib.SimpleActionClient(self.topic_name, JointTrajectory)
    self.client = actionlib.SimpleActionClient(self.topic_name, FollowJointTrajectoryAction)
    
    # with the real arm
    # self.topic_name = '/j2n6s300_driver/joints_action/joint_angles'
    # self.client = actionlib.SimpleActionClient(self.topic_name, ArmJointAnglesAction)

  def move_arm(self, angle1, angle2, angle3, angle4, angle5, angle6):

    # Unpause the physics
    rospy.wait_for_service('/gazebo/unpause_physics')
    unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
    unpause_gazebo()


    print("4")
    # self.client.wait_for_server()
    print("5")
    goal = FollowJointTrajectoryActionGoal()
    print("goal :", goal)
    # goal.path_tolerance = angle1
    goal.goal.trajectory.points = angle1
    # goal.angles.joint2 = angle2
    # goal.angles.joint3 = angle3
    # goal.angles.joint4 = angle4
    # goal.angles.joint5 = angle5
    # goal.angles.joint6 = angle6
    print("goal :", goal)
    print("6")
    self.client.send_goal(goal)
    print("7")
    self.client.wait_for_result()
    print("8")

  def cancel_move(self):
    self.client.cancel_all_goals()

  def read_angles(self):

    self.client.wait_for_server()
    self.client.wait_for_result()
    joint_angles = self.client.get_result()
    angles_list = [
      joint_angles.angles.joint1, 
      joint_angles.angles.joint2, 
      joint_angles.angles.joint3, 
      joint_angles.angles.joint4, 
      joint_angles.angles.joint5, 
      joint_angles.angles.joint6, 
    ]
    return angles_list

  def read_tip_position(self):
    pos = rospy.wait_for_message('/j2n6s300_driver/out/tool_pose', PoseStamped)
    pos_list = [pos.pose.position.x, pos.pose.position.y, pos.pose.position.z]
    return pos_list



if __name__ == '__main__':

  rospy.init_node('jaco_gazebo_action_client_node')

  print("1")
  robot_client = JacoGazeboActionClient()

  print("2")
  robot_client.cancel_move()
  
  print("3")
  robot_client.move_arm(1, 180, 180, 0, 0, 0)