# Jaco Gym Environment
An OpenAI Gym environment for the Jaco2 robotic arm by Kinova.
The environment is implemented both for the real arm and the Gazebo simulator. 
The goal is to bring the arm's end effector as close as possible to the target green ball.
The target object position is initialised randomly at the beginning of each episode.


![Jaco Gazebo](/images/jaco_training.gif)




## Installation

1. Install [ROS](http://wiki.ros.org/ROS/Installation).

* ROS Melodic on Ubuntu 18.04
* ROS Kinetic on Ubuntu 16.04

To use ROS with Python 3, run:

```bash
sudo apt-get install python3-pip
sudo pip3 install rospkg catkin_pkg
```

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


4. Install [Gym](https://github.com/openai/gym).

```bash
pip3 install gym
```

5. Install [jaco-gym](https://github.com/PierreExeter/jaco-gym.git).

```bash
git clone https://github.com/PierreExeter/jaco-gym.git
cd jaco-gym
pip3 install -e .
```

6. Install the ROS packages and build.

```bash
cp -r ROS_packages/sphere_description ~/catkin_ws/src
cp -r ROS_packages/kinova-ros ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```
Note, the kinova-ros package was adapted from the [official package](https://github.com/Kinovarobotics/kinova-ros).



### (OPTIONAL: install the RL library Stable-Baselines)

7. Install [Stable-baselines](https://github.com/pirobot/stable-baselines).

```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
pip3 install stable-baselines[mpi]
```

8. Install the dependencies for [RL Baselines Zoo](https://github.com/araffin/rl-baselines-zoo).
```bash
sudo apt-get install swig ffmpeg
pip3 install box2d box2d-kengz pyyaml optuna pytablewriter
```

9. Install [Tensorflow 1.14](https://www.tensorflow.org/). Stable-baselines does not yet support Tensorflow 2.

```bash
pip3 install tensorflow-gpu==1.14
```


## Test your environment

### For the physical arm (only tested on ROS Kinetic)

In terminal 1:
```bash
roslaunch kinova_bringup kinova_robot.launch kinova_robotType:=j2n6s300
```

Note, by default graphics rendering in Gazebo is disabled. To enable it, edit the launch file

```
~/catkin_ws/src/kinova-ros/kinova_gazebo/launch/robot_launch.launch
```
and replace 
```
  <arg name="gui" default="false"/>
```

by 
```
  <arg name="gui" default="true"/>
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

## Plot learning curves

```bash
python3 scripts/3_plot_results.py
```

## Environment details

### Observation
Type: Box(36)

| Num           | Observation                        | Min   | Max  |
| ------------- | ---------------------------------- | ----- | ---- |
| 0             | joint_1 angle (rad)                | -inf  | inf  |
| 1             | joint_2 angle (rad)                | -inf  | inf  |
| 2             | joint_3 angle (rad)                | -inf  | inf  |
| 3             | joint_4 angle (rad)                | -inf  | inf  |
| 4             | joint_5 angle (rad)                | -inf  | inf  |
| 5             | joint_6 angle (rad)                | -inf  | inf  |
| 6             | joint_finger_1 angle (rad)         | -inf  | inf  |
| 7             | joint_finger_2 angle (rad)         | -inf  | inf  |
| 8             | joint_finger_3 angle (rad)         | -inf  | inf  |
| 9             | joint_finger_tip_1 angle (rad)     | -inf  | inf  |
| 10            | joint_finger_tip_2 angle (rad)     | -inf  | inf  |
| 11            | joint_finger_tip_3 angle (rad)     | -inf  | inf  |
| 12            | joint_1 velocity (rad/s)           | -inf  | inf  |
| 13            | joint_2 velocity (rad/s)           | -inf  | inf  |
| 14            | joint_3 velocity (rad/s)           | -inf  | inf  |
| 15            | joint_4 velocity (rad/s)           | -inf  | inf  |
| 16            | joint_5 velocity (rad/s)           | -inf  | inf  |
| 17            | joint_6 velocity (rad/s)           | -inf  | inf  |
| 18            | joint_finger_1 velocity (rad/s)    | -inf  | inf  |
| 19            | joint_finger_2 velocity (rad/s)    | -inf  | inf  |
| 20            | joint_finger_3 velocity (rad/s)    | -inf  | inf  |
| 21            | joint_finger_tip_1 velocity (rad/s)| -inf  | inf  |
| 22            | joint_finger_tip_2 velocity (rad/s)| -inf  | inf  |
| 23            | joint_finger_tip_3 velocity (rad/s)| -inf  | inf  |
| 24            | joint_1 effort (N.m)               | -inf  | inf  |
| 25            | joint_2 effort (N.m)               | -inf  | inf  |
| 26            | joint_3 effort (N.m)               | -inf  | inf  |
| 27            | joint_4 effort (N.m)               | -inf  | inf  |
| 28            | joint_5 effort (N.m)               | -inf  | inf  |
| 29            | joint_6 effort (N.m)               | -inf  | inf  |
| 30            | joint_finger_1 effort (N.m)        | -inf  | inf  |
| 31            | joint_finger_2 effort (N.m)        | -inf  | inf  |
| 32            | joint_finger_3 effort (N.m)        | -inf  | inf  |
| 33            | joint_finger_tip_1 effort (N.m)    | -inf  | inf  |
| 34            | joint_finger_tip_2 effort (N.m)    | -inf  | inf  |
| 35            | joint_finger_tip_3 effort (N.m)    | -inf  | inf  |



### Actions
Type: Box(6)

| Num           | Action                        | Min   | Max  |
| ------------- | ----------------------------- | ----- | ---- |
| 0             | joint_1 angle (scaled)        | -1    | 1    |
| 1             | joint_2 angle (scaled)        | -1    | 1    |
| 2             | joint_3 angle (scaled)        | -1    | 1    |
| 3             | joint_4 angle (scaled)        | -1    | 1    |
| 4             | joint_5 angle (scaled)        | -1    | 1    |
| 5             | joint_6 angle (scaled)        | -1    | 1    |

Note, at the moment joint_2 angle is restricted to 180 deg and joint_3 angle is restricted to the interval [90, 270] deg in order to reduce the arm's amplitude of motion.

### Reward
The reward is incremented at each time step by the negative of the distance between the target object position and the end deflector position (joint_6).


### Starting State
The arm is initialised with its joint angles as follows (in degrees): [0, 180, 180, 0, 0, 0].
The target object is initialised to a random location within the arm's reach.


### Episode Termination
An episode terminates if more than 50 time steps are completed.


### Step info
The info dictionary returned by the env.step function is structured as follows:
```python
info = {'tip coordinates': [x, y, z], 'target coordinates': array([x, y, z])}
```

## Python profiling
You can profile the time individual lines of code take to execute to monitor the code performance using [line_profiler](https://github.com/rkern/line_profiler).

### Install line-profiler

```bash
pip install line-profiler
```

### Decorate the functions you want to profile with @profile

For example:

```bash
vim scripts/0_test_jaco_gazebo_action_gym.py
```

```python
@profile
def main():

    for episode in range(3):

        obs = env.reset()
        ...
```

### Execute code and profile

```bash
kernprof -l 0_test_jaco_gazebo_action_gym.py
```

### read profiling results line by line

```bash
python -m line_profiler 0_test_jaco_gazebo_action_gym.py.lprof
```

## Supported systems
Tested on:
- Ubuntu 18.04 and 16.04 
- Python 3.6.9
- Gym 0.15.4

