from gym.envs.registration import register

register(
    id='jacoReal-v0',
    entry_point='jaco_real_gym.envs:JacoEnv',
)
