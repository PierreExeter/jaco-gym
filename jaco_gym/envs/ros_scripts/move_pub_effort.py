#! /usr/bin/env python
"""Publishes joint trajectory to move robot to given pose"""

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_srvs.srv import Empty
from sensor_msgs.msg import JointState


class JacoGazeboPublishTopic:
    
    def __init__(self):

        self.pub_topic = '/j2n6s300/effort_joint_trajectory_controller/command'
        self.pub = rospy.Publisher(self.pub_topic, JointTrajectory, queue_size=1)


    def moveJoint(self, jointcmds):

        # Unpause the physics
        rospy.wait_for_service('/gazebo/unpause_physics')
        unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        resp = unpause_gazebo()

        jointCmd = JointTrajectory()  
        point = JointTrajectoryPoint()
    
        jointCmd.header.stamp = rospy.Time.now() + rospy.Duration.from_sec(0.0)  
        point.time_from_start = rospy.Duration.from_sec(5.0)
    
        nbJoints = 6

        for i in range(0, nbJoints):
            jointCmd.joint_names.append('j2n6s300_joint_'+str(i+1))
            point.positions.append(jointcmds[i])
            point.velocities.append(0)
            point.accelerations.append(0)
            point.effort.append(0) 

            # point.effort.append(jointcmds[i])   # give TCP/IP error
    
        jointCmd.points.append(point)
        rate = rospy.Rate(100)
        count = 0
    
        print(jointCmd)

        while (count < 50):
            self.pub.publish(jointCmd)
            count = count + 1
            rate.sleep()           
    
    def read_state(self):

        self.sub_topic = '/j2n6s300/joint_states'
        self.status = rospy.wait_for_message(self.sub_topic, JointState)
        
        self.position = self.status.position
        self.velocity = self.status.velocity
        self.effort = self.status.effort

        return self.position, self.velocity, self.effort



rospy.init_node('jaco_gazebo_publish_topic_node')	
robot = JacoGazeboPublishTopic()
robot.moveJoint([0, 3.14, 3.14, 0, 0, 0])
# print(robot.read_state())
