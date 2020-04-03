#! /usr/bin/env python
"""Publishes joint trajectory to move robot to given pose"""

import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
import argparse

def argumentParser(argument):
  """ Argument parser """
  parser = argparse.ArgumentParser(description='Drive robot joint to command position')
  parser.add_argument('kinova_robotType', metavar='kinova_robotType', type=str, default='j2n6a300',
                    help='kinova_RobotType is in format of: [{j|m|r|c}{1|2}{s|n}{4|6|7}{s|a}{2|3}{0}{0}]. eg: j2n6a300 refers to jaco v2 6DOF assistive 3fingers. Please be noted that not all options are valided for different robot types.')
  #args_ = parser.parse_args(argument)
  argv = rospy.myargv()
  args_ = parser.parse_args(argv[1:])
  prefix = args_.kinova_robotType
  nbJoints = int(args_.kinova_robotType[3])	
  nbfingers = int(args_.kinova_robotType[5])	
  return prefix, nbJoints, nbfingers

def moveJoint (jointcmds,prefix,nbJoints):
  topic_name = '/' + prefix + '/effort_joint_trajectory_controller/command'
  pub = rospy.Publisher(topic_name, JointTrajectory, queue_size=1)
  jointCmd = JointTrajectory()  
  point = JointTrajectoryPoint()
  jointCmd.header.stamp = rospy.Time.now() + rospy.Duration.from_sec(0.0);  
  point.time_from_start = rospy.Duration.from_sec(5.0)
  for i in range(0, nbJoints):
    jointCmd.joint_names.append(prefix +'_joint_'+str(i+1))
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

def moveFingers (jointcmds,prefix,nbJoints):
  topic_name = '/' + prefix + '/effort_finger_trajectory_controller/command'
  pub = rospy.Publisher(topic_name, JointTrajectory, queue_size=1)  
  jointCmd = JointTrajectory()  
  point = JointTrajectoryPoint()
  jointCmd.header.stamp = rospy.Time.now() + rospy.Duration.from_sec(0.0);  
  point.time_from_start = rospy.Duration.from_sec(5.0)
  for i in range(0, nbJoints):
    jointCmd.joint_names.append(prefix +'_joint_finger_'+str(i+1))
    point.positions.append(jointcmds[i])
    point.velocities.append(0)
    point.accelerations.append(0)
    point.effort.append(0) 
  jointCmd.points.append(point)
  rate = rospy.Rate(100)
  count = 0
  while (count < 500):
    pub.publish(jointCmd)
    count = count + 1
    rate.sleep()     

if __name__ == '__main__':
  try:    
    rospy.init_node('move_robot_using_trajectory_msg')		
    prefix, nbJoints, nbfingers = argumentParser(None)    
    #allow gazebo to launch
    rospy.sleep(1)

    if (nbJoints==6):
      #home robots
      moveJoint ([0.0,0.7853,0.5236,0.0,0.0,0.0],prefix,nbJoints)
    else:
      moveJoint ([0.0,2.9,0.0,1.3,4.2,1.4,0.0],prefix,nbJoints)

    moveFingers ([1,1,1],prefix,nbfingers)
  except rospy.ROSInterruptException:
    print "program interrupted before completion"
