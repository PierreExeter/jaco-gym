#! /usr/bin/env python

import actionlib
import rospy

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal, JointTrajectoryControllerState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from gazebo_msgs.msg import LinkStates
from std_srvs.srv import Empty
from sensor_msgs.msg import JointState


class JacoGazeboActionClient:

    def __init__(self):
        rospy.init_node("kinova_client")
        action_address = "/j2n6s300/effort_joint_trajectory_controller/follow_joint_trajectory"
        self.client = actionlib.SimpleActionClient(action_address, FollowJointTrajectoryAction)


    def move_arm(self, points_list):
        # Unpause the physics
        rospy.wait_for_service('/gazebo/unpause_physics')
        unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        unpause_gazebo()

        self.client.wait_for_server()

        goal = FollowJointTrajectoryGoal()    

        # We need to fill the goal message with its components
        #         
        # check msg structure with: rosmsg info FollowJointTrajectoryGoal
        # It is composed of 4 sub-messages:
        # "trajectory" of type trajectory_msgs/JointTrajectory 
        # "path_tolerance" of type control_msgs/JointTolerance
        # "goal_tolerance" of type control_msgs/JointTolerance
        # "goal_time_tolerance" of type duration

        trajectory_msg = JointTrajectory()
        # check msg structure with: rosmsg info JointTrajectory
        # It is composed of 3 sub-messages:
        # "header" of type std_msgs/Header 
        # "joint_names" of type string
        # "points" of type trajectory_msgs/JointTrajectoryPoint

        trajectory_msg.joint_names = [
            "j2n6s300_joint_1", 
            "j2n6s300_joint_2", 
            "j2n6s300_joint_3", 
            "j2n6s300_joint_4", 
            "j2n6s300_joint_5", 
            "j2n6s300_joint_6"
            ]

        points_msg = JointTrajectoryPoint()
        # check msg structure with: rosmsg info JointTrajectoryPoint
        # It is composed of 5 sub-messages:
        # "positions" of type float64
        # "velocities" of type float64
        # "accelerations" of type float64
        # "efforts" of type float64
        # "time_from_start" of type duration
        
        points_msg.positions = points_list
        points_msg.velocities = [0, 0, 0, 0, 0, 0]
        points_msg.accelerations = [0, 0, 0, 0, 0, 0]
        points_msg.effort = [0, 0, 0, 0, 0, 0]
        points_msg.time_from_start = rospy.Duration(0.01)

        # fill in points message of the trajectory message
        trajectory_msg.points = [points_msg]

        # fill in trajectory message of the goal
        goal.trajectory = trajectory_msg

        self.client.send_goal_and_wait(goal)

        return self.client.get_state()


    def cancel_move(self):
        self.client.cancel_all_goals()

    def read_state_old(self):
        self.status = rospy.wait_for_message("/j2n6s300/effort_joint_trajectory_controller/state", JointTrajectoryControllerState)
        
        # convert tuple to list and concatenate
        self.state = list(self.status.actual.positions) + list(self.status.actual.velocities)
        # also self.status.actual.accelerations, self.status.actual.effort

        return self.state

    def read_state(self):
        self.status = rospy.wait_for_message("/j2n6s300/joint_states", JointState)
        
        self.joint_names = self.status.name
        # print(self.joint_names)

        self.pos = self.status.position
        self.vel = self.status.velocity
        self.eff = self.status.effort

        # return self.status
        return self.pos + self.vel + self.eff


    def get_tip_coord(self):
        self.status = rospy.wait_for_message("/gazebo/link_states", LinkStates)
        # see also topic /tf

        self.joint_names = self.status.name
        self.pos = self.status.pose

        # print(self.status.pose[7].position.x)

        # for i in range(14):
        #     print(i)
        #     print("joint:")
        #     print(self.joint_names[i])
        #     print("pose:")
        #     print(self.status.pose[i])

        return [self.status.pose[7].position.x, self.status.pose[7].position.y, self.status.pose[7].position.z]
        



# client = JacoGazeboActionClient()
# client.cancel_move()
# client.move_arm([0, 1.57, 3.14, 0, 0, 0])

# # print(client.read_state())
# # print(client.read_state2())
# print(client.get_tip_coord())   # PB: reading coordinate doesn't wait until the arm has finished moving

