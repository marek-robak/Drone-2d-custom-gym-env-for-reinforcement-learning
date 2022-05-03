# Drone-2d-custom-gym-env-for-reinforcement-learning

This repository contains OpenAI Gym environment designed for teaching RL
agents the ability to control a two-dimensional drone. To make this easy
to use, the environment has been packed into a Python package, which automatically
registers the environment in the Gym library when the package is included in the code.
As a result, it can be easily used in conjunction with reinforcement learning
libraries such as StableBaselines3. There is also a sample code for training and
evaluating agents in this environment.

<p align="center">
  <img src="media/drone_540.gif"/>
</p>

## Installation

These instructions will guide you through installation of the environment and
show you how to use it for your projects. Whichever method of installation you
choose I recommend running it in a virtual environment created by Miniconda.
This program is used to simplify package management and deployment.

So, to get started, install Miniconda, [here](https://docs.conda.io/en/latest/miniconda.html)
is the official installation guide along with a detailed description.

In the following way you can create and activate virtual environment:

```
conda create -n <environment_name> python=3.9
conda activate <environment_name>
```

### Installation via pip - package installer for Python

You just need to type

```
pip install drone-2d-custom-gym-env
```

### Installation via source code from GitHub repository

If you want to make specific changes to the source code or extend it with your
own functionalities this method will suit you.

```
git clone https://github.com/marek-robak/Drone-2d-custom-gym-env-for-reinforcement-learning.git
cd Drone-2d-custom-gym-env-for-reinforcement-learning/drone_2d_custom_gym_env_package
pip install -e .
```

### How to use it in your code

Now all you need to do to use this environment in your code is import the package.
After that, you can use it with Gym and StableBaselines3 library via its
id: drone-2d-custom-v0.

```
from stable_baselines3 import PPO
import gym

import drone_2d_custom_gym_env

env = gym.make('drone-2d-custom-v0')

model = PPO("MlpPolicy", env)

model.learn(total_timesteps=1800000)
model.save('new_agent')
```

### Environment prerequisites

Environment to run needs Python3 with Gym, Pygame, Pymunk, Numpy and StableBaselines3
libraries. All of them are automatically installed when the package is installed.

## Environment details

This environment is divided into three areas marked by individual squares.
The smallest square is a graphical representation of the space in which the drone
can be spawned at the beginning of each episode. The larger square limits the space
in which the target point can appear. The agent must learn how to fly the drone to this
point. The largest square is the limitation of the space that drone can fly to.
If the drone flies beyond this, the current episode ends.

The drone model in this environment is a rigid body consisting of three segments.
Two of them represent the drone's motors. They can generate a lifting force, the
values of which are shown by the length of the red lines coming from the individual
motors. The gray lines behind them are there for scale. At the beginning of each
episode, the drone is thrown away in random directions with random force and for a
fixed number of timesteps his motors are blocked. This is to create a situation
where the RL agent has to cope with controlling the flight of the falling drone.
The red color of the trajectory line shows the flight stage in which the agent had
no control over the drone.

The physics engine for this environment runs at 60fps.

### Initial episode conditions

At the start of each episode, the aircraft is placed in the smallest square with
a random slope angle from -45° to 45°. Then it is thrown in random directions with
random force. The values of this force and the size of the square were selected
experimentally so that the drone in each possible situation could save himself.

### Ending episode conditions

Each episode ends if the drone's inclination exceeds 90° or if the aircraft flies
outside the allowed area. Additionally, each episode is limited in duration by the
maximum number of timesteps.

### Agent action and observation space

The space of actions made available to the RL agent consists of two values from -1
to 1. They are correlated with the forces with which the left and right motors of
the drone can operate. The value -1 means no force, and value 1 is the maximum
possible force.

The observation space consists of eight values, all ranging from -1 to 1.
- The first two represent the linear speed of the drone in the x and y axes.
They are calibrated so that the values -1 and 1 are the maximum possible speeds
that the aircraft can reach in the available space.
- The third number shows the current angular speed of the drone. Like the first two
was scaled so that the numbers -1 and 1 represent the maximum possible value to
obtain in this simulation.
- The fourth number contains the aircraft pitch information, the numbers -1 and 1
are returned for 90° tilts.
- The fifth and sixth numbers carry information about the drone's distance from
the target in the x and y axes. They are calibrated to return 0 when the drone is
on target and values of -1 and 1 when the drone is at the boundary of the space it
is allowed to move in.
- The seventh and eighth numbers contain information about the drone's position
in the available space. Value 0 is returned when the drone is in the center
of available space.

### Reward function

The RL agent controlling the drone must be effectively encouraged to approach the
target point. Therefore, the reward function for this environment adopts the
following formula.

<img src="https://render.githubusercontent.com/render/math?math={\Large\color{black}R(d_{x}, d_{y})=\frac{1}{d_{x}%2B0.1}%2B\frac{1}{d_{y}%2B0.1}}#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\Large\color{white}R(d_{x}, d_{y})=\frac{1}{d_{x}%2B0.1}%2B\frac{1}{d_{y}%2B0.1}}#gh-dark-mode-only">

Variables dx and dy are the fifth and sixth values from the agent observation space.

Additionally, the drone is penalized for ending the episode prematurely with -10 penalties.

### Environment parameters

This environment provides several parameters that can change the way it works.

- render_sim: (bool) if true, a graphic is generated
- render_path: (bool) if true, the drone's path is drawn
- render_shade: (bool) if true, the drone's shade is drawn
- shade_distance: (int) distance between consecutive drone's shades
- n_steps: (int) number of time steps
- n_fall_steps: (int) the number of initial steps for which the drone can't do anything
- change_target: (bool) if true, mouse click change target positions
- initial_throw: (bool) if true, the drone is initially thrown with random force

You can change them when creating env variable.

```
env = gym.make('drone-2d-custom-v0', render_sim=True, render_path=True, render_shade=True,
               shade_distance=70, n_steps=500, n_fall_steps=10, change_target=True,
               initial_throw=True)
```

## See also

Everything available in this repository was created for the needs of my bachelor thesis.
If you can read in Polish and you are interested in it, you can find it
[here](https://www.ap.uj.edu.pl/diplomas/151837/?_s=1). It includes details on the
training process for sample agents and a description of the reward function selection process.

You may also be interested in other environments I have created. Go to the repositories
where they are located by clicking on the gifs below.

<p align="center">
  <a href="https://github.com/mareo1208/Single-cartpole-custom-gym-env-for-reinforcement-learning.git">
    <img src="media/cartpole_360.gif"/>
  </a>
  <a href="https://github.com/mareo1208/Double-cartpole-custom-gym-env-for-reinforcement-learning.git">
    <img src="media/double_cartpole_360.gif"/>
  </a>
</p>
