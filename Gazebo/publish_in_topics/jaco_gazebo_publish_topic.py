#! /usr/bin/env python
"""Publishes joint trajectory to move robot to given pose"""

import rospy
import time
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_srvs.srv import Empty
from sensor_msgs.msg import JointState


class JacoGazeboPublishTopic:
    
    def __init__(self):

        rospy.init_node('jaco_gazebo_publish_topic_node')

        self.pub_topic = '/j2n6s300/effort_joint_trajectory_controller/command'
        self.pub = rospy.Publisher(self.pub_topic, JointTrajectory, queue_size=1)


    def moveJoint(self, jointcmds):
        
        #allow gazebo to launch
        # time.sleep(5)

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
    
        jointCmd.points.append(point)
        rate = rospy.Rate(100)
        count = 0
    
        while (count < 50):
            self.pub.publish(jointCmd)
            count = count + 1
            rate.sleep()     


    # def callback(self, msg):       # Define a function called 'callback' that receives a parameter named 'msg'                                 
    #     print("\n position: ", msg.position)       # Print the value 'position' inside the 'msg' parameter
    #     print("\n velocity: ", msg.velocity)
    #     print("\n effort: ", msg.effort)

    #     rospy.loginfo("\n" + rospy.get_caller_id() + " position rospy: %s", msg.position)
    #     rospy.loginfo("\n" + rospy.get_caller_id() + " velocity rospy: %s", msg.velocity)
    #     rospy.loginfo("\n" + rospy.get_caller_id() + " effort rospy: %s", msg.effort)
        
    
    def read_state(self):

        # rospy.init_node('topic_subscriber')
        # self.sub_topic = '/j2n6s300/joint_states'
        # self.sub = rospy.Subscriber(self.sub_topic, JointState, self.callback)
        # print(self.sub)
        # rospy.spin()  

        self.sub_topic = '/j2n6s300/joint_states'
        self.status = rospy.wait_for_message(self.sub_topic, JointState)
        
        self.position = self.status.position
        self.velocity = self.status.velocity
        self.effort = self.status.effort

        return self.position, self.velocity, self.effort



if __name__ == '__main__':

    rospy.init_node('jaco_gazebo_publish_topic_node')	
    
    robot = JacoGazeboPublishTopic()

    robot.moveJoint([0.0, 2.9, 1.3, 4.2, 1.4, 0.0])

    print(robot.read_state())