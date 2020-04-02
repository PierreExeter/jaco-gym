from gym.envs.registration import register

register(
    id='JacoGazebo-v0',
    entry_point='jaco_gazebo_gym.jaco_env:JacoEnv',
    max_episode_steps=50
)
