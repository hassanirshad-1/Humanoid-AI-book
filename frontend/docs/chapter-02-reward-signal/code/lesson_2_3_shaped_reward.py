# Copyright 2025 The AI-Native Textbook Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This script contains a shaped reward function for our humanoid robot.
It combines multiple reward components to encourage more complex behavior.
"""
import numpy as np

# --- Hyperparameters for Reward Components ---
# These weights control the trade-off between different objectives.
UPRIGHT_WEIGHT = 1.0
VELOCITY_WEIGHT = 1.5
CONTROL_COST_WEIGHT = -0.05
DESIRED_VELOCITY = 1.0

def is_fallen(d):
  """
  Checks if the robot has fallen based on its torso orientation and height.
  This is the same as in the previous lesson, acting as a "kill condition."
  """
  torso_z_axis = d.xmat['torso', 'zz']
  torso_z_height = d.qpos[2]
  return torso_z_axis < 0.8 or torso_z_height < 0.3

def upright_reward(d):
  """
  Calculates a reward for being upright.
  Uses a sigmoid to create a smooth gradient.
  """
  torso_z_axis = d.xmat['torso', 'zz']
  # Sigmoid function to smoothly scale reward between 0 and 1.
  return 1 / (1 + np.exp(-6 * (torso_z_axis - 0.9)))

def velocity_reward(d):
  """
  Calculates a reward for moving forward at a desired velocity.
  """
  # Velocity along the forward (X) axis.
  forward_velocity = d.qvel[0]
  # Clip the velocity to the desired velocity to prevent rewarding excess speed.
  clipped_velocity = np.clip(forward_velocity, 0, DESIRED_VELOCITY)
  return clipped_velocity

def control_cost(d):
  """
  Calculates a penalty for high motor effort.
  """
  # `d.ctrl` contains the torques applied by each actuator.
  # The norm represents the magnitude of the control vector.
  # We square it to penalize large efforts more heavily.
  return np.linalg.norm(d.ctrl) ** 2

def calculate_reward(d):
  """
  Calculates the total shaped reward for the current timestep.

  Args:
    d: MuJoCo data structure.

  Returns:
    A scalar reward value.
  """
  # If the robot has fallen, the episode is effectively over. Return 0.
  if is_fallen(d):
    return 0.0

  # Calculate the individual reward components.
  upright = upright_reward(d)
  velocity = velocity_reward(d)
  control = control_cost(d)

  # Combine them with their respective weights.
  reward = (UPRIGHT_WEIGHT * upright +
            VELOCITY_WEIGHT * velocity +
            CONTROL_COST_WEIGHT * control)

  return reward
