import rospy
import time
from jaco_gazebo_publish_topic import JacoGazeboPublishTopic


	

robot = JacoGazeboPublishTopic()

# robot.moveJoint([1.0, 2.9, 1.3, 4.2, 1.4, 0.0])
robot.moveJoint([0, 2, 3, 0, 0, 0])


