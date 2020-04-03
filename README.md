# Jaco Gym Environment
An OpenAI Gym environment for the Jaco2 robotic arm by Kinova.
The environment is implemented both for the real arm and the Gazebo simulator.


![Jaco Gazebo](/images/jaco_training.gif)

## Installation

1. Install [ROS](http://wiki.ros.org/ROS/Installation).

ROS Melodic on Ubuntu 18.04

or 

ROS Kinetic on Ubuntu 16.04


2. Install and configure your [Catkin workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).



3. Install dependencies for the Kinova-ros package, as indicated [here](https://github.com/Kinovarobotics/kinova-ros/wiki/Gazebo).

```bash
sudo apt-get install ros-<distro>-gazebo-ros-control
sudo apt-get install ros-<distro>-ros-controllers*
sudo apt-get install ros-<distro>-trac-ik-kinematics-plugin
sudo apt-get install ros-<distro>-effort-controllers 
sudo apt-get install ros-<distro>-joint-state-controller 
sudo apt-get install ros-<distro>-joint-trajectory-controller 
sudo apt-get install ros-<distro>-controller-*
```

(replace `<distro>` by your ROS distribution, for example `kinetic` or `melodic`)


4. Install the ROS packages and build.

```bash
cp -r ROS_packages/sphere_description ~/catkin_ws/src
cp -r ROS_packages/kinova-ros ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```
Note, the kinova-ros package was adapted from the [official package](https://github.com/Kinovarobotics/kinova-ros).


5. Install [Gym](https://github.com/openai/gym).

```bash
pip3 install gym
```

6. Install [jaco-gym](https://github.com/PierreExeter/jaco-gym.git).

```bash
git clone https://github.com/PierreExeter/jaco-gym.git
pip3 install -e .
```

### (OPTIONAL: install the RL library Stable-Baselines)

8. Install [Stable-baselines](https://github.com/pirobot/stable-baselines).

```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
pip3 install stable-baselines[mpi]
```

9. Install the dependencies for [RL Baselines Zoo](https://github.com/araffin/rl-baselines-zoo).
```bash
sudo apt-get install swig ffmpeg
pip3 install box2d box2d-kengz pyyaml optuna pytablewriter
```

10. Install [Tensorflow 1.14](https://www.tensorflow.org/). Stable-baselines does not yet support Tensorflow 2.

```bash
pip3 install tensorflow-gpu==1.14
```


## Test your environment

### For the physical arm (only tested on ROS Kinetic)

In terminal 1:
```bash
roslaunch kinova_bringup kinova_robot.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 scripts/0_test_jaco_real.py
```

### For the arm in Gazebo (tested on ROS Melodic and Kinetic)

In terminal 1:
```bash
roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 scripts/0_test_jaco_gazebo_action_gym.py
```

## Train the agent

In terminal 1:
```bash
roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 scripts/1_train_ppo2.py
```

## Enjoy a trained agent

In terminal 1:
```bash
roslaunch kinova_gazebo robot_launch.launch kinova_robotType:=j2n6s300
```

In terminal 2:
```bash
python3 scripts/2_enjoy_ppo2.py
```


## Supported systems
Tested on:
- Ubuntu 18.04 and 16.04 
- Python 3.6
- Gym 0.15.4

