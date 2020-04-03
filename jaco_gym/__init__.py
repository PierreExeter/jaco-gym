from gym.envs.registration import register


# environment to move the real arm
register(
    id='JacoReal-v0',
    entry_point='jaco_gym.envs.jaco_real_env:JacoEnv',
)


# environment using the ROS Topics to move the arm in Gazebo
register(
    id='JacoGazebo-v0',
    entry_point='jaco_gym.envs.jaco_gazebo_topic_env:JacoEnv'
)


# environment using ROS Action client to move the arm in Gazebo
register(
    id='JacoGazebo-v1',
    entry_point='jaco_gym.envs.jaco_gazebo_action_env:JacoEnv'
)


