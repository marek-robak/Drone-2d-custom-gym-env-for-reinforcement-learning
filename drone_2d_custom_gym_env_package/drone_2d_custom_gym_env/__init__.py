from drone_2d_custom_gym_env.drone_2d_env import *
from gym.envs.registration import register

register(
    id='drone-2d-custom-v0',
    entry_point='drone_2d_custom_gym_env:Drone2dEnv',
    kwargs={'render_sim': False, 'render_path': True, 'render_shade': True,
            'shade_distance': 75, 'n_steps': 500, 'n_fall_steps': 10, 'change_target': False,
            'initial_throw': True}
)
