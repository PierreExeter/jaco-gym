# Jaco Gym Environment
An OpenAI Gym environment for the Jaco2 robotic arm by Kinova.
The environment is implemented both for the real arm and the Gazebo simulator.

## Installation

Install [ROS](http://wiki.ros.org/ROS/Installation).
ROS Melodic on Ubuntu 18.04
or 
ROS Kinetic on Ubuntu 16.04


Install and configure your [Catkin workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).


Install [Kinova-ros](https://github.com/Kinovarobotics/kinova-ros) and build.
```bash
cd ~/catkin_ws/src
git clone https://github.com/Kinovarobotics/kinova-ros.git
cd ..
catkin_make
```

Install [Gym](https://github.com/openai/gym).

```bash
pip install gym
```


Install [jaco-gym](https://github.com/PierreExeter/jaco-gym.git).

```bash
git clone https://github.com/PierreExeter/jaco-gym.git
cd jaco-gym/Real/jaco-real-gym/    # Environment for the physical arm
pip3 install -e .
cd ../../publish_in_topics/jaco-gazebo-gym/  # Environment for the arm in Gazebo
pip3 install -e .
```

## Test your environment

For the physical arm (only tested on ROS Kinetic):

In terminal 1:
```bash
roslaunch kinova_bringup kinova_robot.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 Real/test_jaco_real.py
```

For the arm in Gazebo (tested with ROS Melodic and Kinetic):

In terminal 1:
```bash
roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 Gazebo/publish_in_topics/test_jaco_gazebo_gym.py
```

## Supported systems
Tested on:
- Ubuntu 18.04 and 16.04 
- Python 3.6
- Gym 0.15.4

