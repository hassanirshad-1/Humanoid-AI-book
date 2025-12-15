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
This script contains the first reward function for our humanoid robot.
The goal is a simple "survival" bonus: reward the robot for not falling.
"""

def is_fallen(d):
  """
  Checks if the robot has fallen based on its torso orientation and height.

  Args:
    d: MuJoCo data structure.

  Returns:
    A boolean indicating if the robot has fallen.
  """
  # The Z-axis of the torso's rotation matrix. 1.0 is perfectly upright.
  torso_z_axis = d.xmat['torso', 'zz']
  # The Z-height of the torso's center of mass.
  torso_z_height = d.qpos[2]

  # We consider the robot "fallen" if its torso is too tilted or too low.
  return torso_z_axis < 0.8 or torso_z_height < 0.3

def calculate_reward(d):
  """
  Calculates the reward for the current timestep.

  Args:
    d: MuJoCo data structure.

  Returns:
    A scalar reward value.
  """
  # A simple survival reward: +1 for being upright, 0 for being fallen.
  if is_fallen(d):
    return 0.0
  else:
    return 1.0
