#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32 
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


# def callback(msg):       # Define a function called 'callback' that receives a parameter named 'msg'                                 
#     print("position: ", msg.position)       # Print the value 'position' inside the 'msg' parameter
#     print("velocity: ", msg.velocity)
#     print("effort: ", msg.effort)

# rospy.init_node('topic_subscriber')    # Initiate a Node called 'topic_subscriber'

# # Create a Subscriber object that will listen 
# # to the /j2n6s300/joint_states topic and will call the
# # 'callback' function each time it reads something from the topic

# rospy.Subscriber("/j2n6s300/joint_states", JointState, callback)
  
# rospy.spin()   




#################



joint_pub = None

def joint_callback(data): # data of type JointState
    pub_msg = JointState() # Make a new msg to publish results
    pub_msg.header = Header()
    pub_msg.name = data.name
    pub_msg.velocity = [10] * len(data.name)
    pub_msg.effort = [100] * len(data.name)
    joint_pub.publish(pub_msg) # Send it when ready!


print("1")
# Init ROS
rospy.init_node('joint_logger_node', anonymous=True)

print("2")
# Subscribers
rospy.Subscriber('/j2n6s300/joint_states', JointState, joint_callback)

print("3")
# Publishers
joint_pub = rospy.Publisher('target_joint_states', JointState, queue_size = 10)

print("4")
# Spin
rospy.spin()

