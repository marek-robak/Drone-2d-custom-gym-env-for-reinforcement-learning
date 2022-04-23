from stable_baselines3 import PPO
import gym
import time
import sys

import drone_2d_custom_gym_env

continuous_mode = True #if True, after completing one episode the next one will start automatically
random_action = False #if True, the agent will take actions randomly

render_sim = True #if True, a graphic is generated

env = gym.make('drone-2d-custom-v0', render_sim=render_sim, render_path=True, render_shade=True,
            shade_distance=70, n_steps=500, n_fall_steps=10, change_target=True, initial_throw=True)

"""
The example agent used here was originally trained with Python 3.7
For this reason, it is not compatible with Python version >= 3.8
Agent has been adapted to run in the newer version of Python,
but because of this, you cannot easily resume their training.
If you are interested in resuming learning, please use Python 3.7.
"""
if sys.version_info.major == 3 and sys.version_info.minor >= 8:
    model = PPO.load("ppo_agents/ppo_agent.zip")
else:
    model = PPO.load("ppo_agents/ppo_agent_python3.7.zip")

model.set_env(env)

random_seed = int(time.time())
model.set_random_seed(random_seed)

obs = env.reset()

try:
    while True:
        if render_sim:
            env.render()

        if random_action:
            action = env.action_space.sample()
        else:
            action, _states = model.predict(obs)

        obs, reward, done, info = env.step(action)

        if done is True:
            if continuous_mode is True:
                state = env.reset()
            else:
                break

finally:
    env.close()
