#! /usr/bin/env python

import actionlib
import rospy
import numpy as np

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal, JointTrajectoryControllerState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from gazebo_msgs.msg import LinkStates, ModelState
from std_srvs.srv import Empty
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose, Point


class JacoGazeboActionClient:

    def __init__(self):
        
        action_address = "/j2n6s300/effort_joint_trajectory_controller/follow_joint_trajectory"
        self.client = actionlib.SimpleActionClient(action_address, FollowJointTrajectoryAction)

        self.pub_topic = '/gazebo/set_model_state'
        self.pub = rospy.Publisher(self.pub_topic, ModelState, queue_size=1)

        # Unpause the physics
        rospy.wait_for_service('/gazebo/unpause_physics')
        unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        unpause_gazebo()


    def move_arm(self, points_list):
        # # Unpause the physics
        # rospy.wait_for_service('/gazebo/unpause_physics')
        # unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        # unpause_gazebo()

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
        
        points_msg.positions = [0, 0, 0, 0, 0, 0]
        points_msg.velocities = [0, 0, 0, 0, 0, 0]
        points_msg.accelerations = [0, 0, 0, 0, 0, 0]
        points_msg.effort = [0, 1, 0, 0, 0, 0]
        points_msg.time_from_start = rospy.Duration(0.01)

        # fill in points message of the trajectory message
        trajectory_msg.points = [points_msg]

        # fill in trajectory message of the goal
        goal.trajectory = trajectory_msg

        print(trajectory_msg)

        # self.client.send_goal_and_wait(goal)
        self.client.send_goal(goal)
        self.client.wait_for_result()

        rospy.sleep(2)      # wait for 2s

        # return self.client.get_state()

    def move_sphere(self, coords_list):

        model_state_msg = ModelState()
        # check msg structure with: rosmsg info gazebo_msgs/ModelState
        # It is composed of 4 sub-messages:
        # model_name of type string
        # pose of type geometry_msgs/Pose
        # twist of type geometry_msgs/Twist 
        # reference_frame of type string

        pose_msg = Pose()
        # rosmsg info geometry_msgs/Pose
        # It is composed of 2 sub-messages
        # position of type geometry_msgs/Point
        # orientation of type geometry_msgs/Quaternion 

        point_msg = Point()
        # rosmsg info geometry_msgs/Point
        # It is composed of 3 sub-messages
        # x of type float64
        # y of type float64
        # z of type float64
        point_msg.x = coords_list[0]
        point_msg.y = coords_list[1]
        point_msg.z = coords_list[2]

        pose_msg.position = point_msg

        model_state_msg.model_name = "my_sphere3"
        model_state_msg.pose = pose_msg
        model_state_msg.reference_frame = "world"

        # print(model_state_msg)
        
        self.pub.publish(model_state_msg)



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
        return np.asarray(self.pos + self.vel + self.eff)


    def get_tip_coord(self):
        self.status = rospy.wait_for_message("/gazebo/link_states", LinkStates)
        # see also topic /tf

        self.joint_names = self.status.name
        self.pos = self.status.pose

        # BE CAREFUL: joint number changes if I add a sphere!
        # print(self.joint_names[8])
        # print(self.status.pose[8].position)


        # for i in range(14):
        #     print(i)
        #     print("joint:")
        #     print(self.joint_names[i])
        #     print("pose:")
        #     print(self.status.pose[i])

        return [self.status.pose[8].position.x, self.status.pose[8].position.y, self.status.pose[8].position.z]
        


rospy.init_node("kinova_client")
client = JacoGazeboActionClient()
client.cancel_move()
client.move_arm([3, 1.57, 3.14, 0, 0, 0])

# client.move_sphere([1, 1, 1])

# # print(client.read_state())
# # print(client.read_state2())
# print(client.get_tip_coord())   # PB: reading coordinate doesn't wait until the arm has finished moving. SOLUTION: wait for 2s. To improve.

# client.read_state()
