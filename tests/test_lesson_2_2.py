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
from lesson_2_2_survival_reward import is_fallen, calculate_reward

@pytest.fixture
def mock_data():
    """Pytest fixture to create a mock MuJoCo data object."""
    d = Mock()
    # Mocking numpy array access
    d.xmat = {'torso': np.identity(3).reshape(3, 3)}
    # Mocking direct attribute access that might behave like a numpy array
    d.qpos = np.zeros(10)  # Make it an array
    return d

def test_is_not_fallen_when_upright(mock_data):
    """Test that the robot is not considered fallen when upright."""
    # Standing perfectly straight
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 1.0
    assert not is_fallen(mock_data)
    assert calculate_reward(mock_data) == 1.0

def test_is_fallen_when_tilted(mock_data):
    """Test that the robot is considered fallen when tilted too far."""
    # Tilted significantly
    mock_data.xmat['torso', 'zz'] = 0.7
    mock_data.qpos[2] = 0.8  # Height is still okay
    assert is_fallen(mock_data)
    assert calculate_reward(mock_data) == 0.0

def test_is_fallen_when_too_low(mock_data):
    """Test that the robot is considered fallen when its height is too low."""
    # Orientation is fine
    mock_data.xmat['torso', 'zz'] = 0.9
    mock_data.qpos[2] = 0.2
    assert is_fallen(mock_data)
    assert calculate_reward(mock_data) == 0.0

def test_is_fallen_when_tilted_and_low(mock_data):
    """Test that the robot is considered fallen when both conditions are met."""
    mock_data.xmat['torso', 'zz'] = 0.6
    mock_data.qpos[2] = 0.25
    assert is_fallen(mock_data)
    assert calculate_reward(mock_data) == 0.0

def test_boundary_condition_orientation(mock_data):
    """Test the boundary condition for orientation."""
    # Just at the edge of being fallen
    mock_data.xmat['torso', 'zz'] = 0.79
    mock_data.qpos[2] = 1.0
    assert is_fallen(mock_data)
    assert calculate_reward(mock_data) == 0.0

def test_boundary_condition_height(mock_data):
    """Test the boundary condition for height."""
    # Just at the edge of being fallen
    mock_data.xmat['torso', 'zz'] = 1.0
    mock_data.qpos[2] = 0.29
    assert is_fallen(mock_data)
    assert calculate_reward(mock_data) == 0.0
