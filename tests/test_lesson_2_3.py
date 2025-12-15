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

import numpy as np
import pytest
from unittest.mock import Mock

# This is a bit of a hack to import a file from a non-package directory.
# In a real project, you'd structure this as a proper Python package.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend/docs/chapter-02-reward-signal/code')))
from lesson_2_3_shaped_reward import calculate_reward, UPRIGHT_WEIGHT, VELOCITY_WEIGHT, CONTROL_COST_WEIGHT, DESIRED_VELOCITY

@pytest.fixture
def mock_data():
    """Pytest fixture to create a mock MuJoCo data object."""
    d = Mock()
    # Mocking numpy array access for matrices and vectors
    d.xmat = {'torso': np.identity(3).reshape(3, 3)}
    d.qpos = np.zeros(10)
    d.qvel = np.zeros(10)
    d.ctrl = np.zeros(10)
    return d

def test_fallen_reward_is_zero(mock_data):
    """Test that the reward is zero if the robot has fallen."""
    # Condition for being fallen (torso too tilted)
    mock_data.xmat['torso', 'zz'] = 0.7
    mock_data.qpos[2] = 1.0
    assert calculate_reward(mock_data) == 0.0

def test_standing_still_reward(mock_data):
    """Test the reward for standing perfectly still and upright."""
    # Perfectly upright
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 1.0
    # No velocity
    mock_data.qvel[0] = 0.0
    # No control cost
    mock_data.ctrl.fill(0)

    reward = calculate_reward(mock_data)

    # Expected: should get a high upright reward, no velocity, no control cost
    # The sigmoid for upright_reward with zz=1.0 is 1 / (1 + exp(-6 * (1.0 - 0.9))) ~= 0.645
    expected_upright = 1 / (1 + np.exp(-6 * (1.0 - 0.9)))
    expected_reward = UPRIGHT_WEIGHT * expected_upright
    assert np.isclose(reward, expected_reward)

def test_moving_forward_reward(mock_data):
    """Test that moving forward increases the reward."""
    # Perfectly upright
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 1.0
    # Moving forward at desired velocity
    mock_data.qvel[0] = DESIRED_VELOCITY
    # No control cost
    mock_data.ctrl.fill(0)

    reward = calculate_reward(mock_data)

    # Expected: upright reward + full velocity reward
    expected_upright = 1 / (1 + np.exp(-6 * (1.0 - 0.9)))
    expected_velocity = DESIRED_VELOCITY
    expected_reward = (UPRIGHT_WEIGHT * expected_upright) + (VELOCITY_WEIGHT * expected_velocity)
    assert np.isclose(reward, expected_reward)

def test_control_cost_penalty(mock_data):
    """Test that applying controls reduces the reward."""
    # Perfectly upright and still
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 1.0
    mock_data.qvel[0] = 0.0
    # Apply some control effort
    mock_data.ctrl = np.ones(10) * 0.5  # 10 motors, 0.5 torque each

    reward = calculate_reward(mock_data)

    # Expected: upright reward - control cost
    expected_upright = 1 / (1 + np.exp(-6 * (1.0 - 0.9)))
    control_norm_sq = np.linalg.norm(np.ones(10) * 0.5) ** 2
    expected_control_cost = control_norm_sq
    expected_reward = (UPRIGHT_WEIGHT * expected_upright) + (CONTROL_COST_WEIGHT * expected_control_cost)
    assert np.isclose(reward, expected_reward)

def test_full_reward_calculation(mock_data):
    """Test all components of the reward function together."""
    # Upright
    mock_data.xmat['torso', 'zz'] = 0.95
    mock_data.qpos[2] = 0.9
    # Moving forward, but not at max desired speed
    mock_data.qvel[0] = 0.5
    # Some control effort
    mock_data.ctrl = np.ones(10) * 0.2

    reward = calculate_reward(mock_data)

    # Expected: combination of all three
    expected_upright = 1 / (1 + np.exp(-6 * (0.95 - 0.9)))
    expected_velocity = 0.5
    control_norm_sq = np.linalg.norm(np.ones(10) * 0.2) ** 2
    expected_control_cost = control_norm_sq

    expected_reward = (UPRIGHT_WEIGHT * expected_upright +
                       VELOCITY_WEIGHT * expected_velocity +
                       CONTROL_COST_WEIGHT * expected_control_cost)

    assert np.isclose(reward, expected_reward)

def test_velocity_clipping(mock_data):
    """Test that velocity reward is clipped at the desired velocity."""
    # Upright and still
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 1.0
    mock_data.ctrl.fill(0)
    # Moving forward much faster than desired
    mock_data.qvel[0] = DESIRED_VELOCITY + 2.0

    reward = calculate_reward(mock_data)

    # Expected: velocity component should be clipped to DESIRED_VELOCITY
    expected_upright = 1 / (1 + np.exp(-6 * (1.0 - 0.9)))
    expected_velocity = DESIRED_VELOCITY  # Not DESIRED_VELOCITY + 2.0
    expected_reward = (UPRIGHT_WEIGHT * expected_upright) + (VELOCITY_WEIGHT * expected_velocity)
    assert np.isclose(reward, expected_reward)
