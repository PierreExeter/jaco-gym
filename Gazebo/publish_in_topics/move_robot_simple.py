#! /usr/bin/env python
"""Publishes joint trajectory to move robot to given pose"""

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_srvs.srv import Empty
import time


def moveJoint (jointcmds):
    topic_name = '/j2n6s300/effort_joint_trajectory_controller/command'
    pub = rospy.Publisher(topic_name, JointTrajectory, queue_size=1)

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
  
    jointCmd.points.append(point)
    rate = rospy.Rate(100)
    count = 0
  
    while (count < 50):
        pub.publish(jointCmd)
        count = count + 1
        rate.sleep()     


if __name__ == '__main__':
    try:    
        rospy.init_node('move_robot_using_trajectory_msg')	

        #allow gazebo to launch
        time.sleep(5)

        # Unpause the physics
        rospy.wait_for_service('/gazebo/unpause_physics')
        unpause_gazebo = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        resp = unpause_gazebo()

        moveJoint ([3.0, 2.9 ,1.3 ,4.2 ,1.4 ,0.0])

    except rospy.ROSInterruptException:
        print "program interrupted before completion"
