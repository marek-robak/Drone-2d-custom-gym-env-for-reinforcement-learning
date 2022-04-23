from stable_baselines3 import PPO
import gym

import drone_2d_custom_gym_env

env = gym.make('drone-2d-custom-v0', render_sim=False, render_path=True, render_shade=True,
            shade_distance=70, n_steps=500, n_fall_steps=10, change_target=True, initial_throw=True)

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=1800000)
model.save('new_agent')
