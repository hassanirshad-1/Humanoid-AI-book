"""
Test for Lesson 3.1: Policy Comparison

This test verifies that the heuristic policy produces more structured
(and presumably better) actions than the random policy.
"""

import pytest
import numpy as np
import sys
import os

# Add the code directory to path for imports
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), 
    '..', 'frontend', 'docs', 'chapter-03-policy-and-value', 'code'
))

from lesson_3_1_policy_comparison import random_policy, heuristic_policy, NUM_ACTUATORS


class TestPolicyComparison:
    """Test suite for Lesson 3.1 policy functions."""
    
    def test_random_policy_returns_correct_shape(self):
        """Random policy should return an action of correct dimension."""
        obs = np.zeros(50)
        action = random_policy(obs)
        
        assert action.shape == (NUM_ACTUATORS,), \
            f"Expected shape ({NUM_ACTUATORS},), got {action.shape}"
    
    def test_random_policy_values_in_range(self):
        """Random policy actions should be in [-1, 1]."""
        obs = np.zeros(50)
        action = random_policy(obs)
        
        assert np.all(action >= -1.0) and np.all(action <= 1.0), \
            "Random policy actions should be in range [-1, 1]"
    
    def test_heuristic_policy_returns_correct_shape(self):
        """Heuristic policy should return an action of correct dimension."""
        obs = np.zeros(50)
        action = heuristic_policy(obs)
        
        assert action.shape == (NUM_ACTUATORS,), \
            f"Expected shape ({NUM_ACTUATORS},), got {action.shape}"
    
    def test_heuristic_policy_values_in_range(self):
        """Heuristic policy actions should be in [-1, 1]."""
        obs = np.zeros(50)
        obs[1] = 0.5  # Set some pitch
        obs[2] = 0.3  # Set some roll
        action = heuristic_policy(obs)
        
        assert np.all(action >= -1.0) and np.all(action <= 1.0), \
            "Heuristic policy actions should be clipped to range [-1, 1]"
    
    def test_heuristic_responds_to_pitch(self):
        """Heuristic policy should respond to pitch changes."""
        obs_neutral = np.zeros(50)
        obs_forward = np.zeros(50)
        obs_forward[1] = 0.3  # Forward lean
        
        action_neutral = heuristic_policy(obs_neutral)
        action_forward = heuristic_policy(obs_forward)
        
        # Actions should differ when pitch is non-zero
        assert not np.allclose(action_neutral, action_forward), \
            "Heuristic policy should respond to pitch changes"
    
    def test_heuristic_responds_to_roll(self):
        """Heuristic policy should respond to roll changes."""
        obs_neutral = np.zeros(50)
        obs_tilted = np.zeros(50)
        obs_tilted[2] = 0.2  # Side lean
        
        action_neutral = heuristic_policy(obs_neutral)
        action_tilted = heuristic_policy(obs_tilted)
        
        # Actions should differ when roll is non-zero
        assert not np.allclose(action_neutral, action_tilted), \
            "Heuristic policy should respond to roll changes"
    
    def test_random_policy_is_stochastic(self):
        """Random policy should produce different actions on each call."""
        obs = np.zeros(50)
        
        actions = [random_policy(obs) for _ in range(10)]
        
        # Check that not all actions are identical
        all_same = all(np.allclose(actions[0], a) for a in actions[1:])
        assert not all_same, \
            "Random policy should produce different actions on each call"
    
    def test_heuristic_policy_is_deterministic(self):
        """Heuristic policy should produce the same action for the same input."""
        obs = np.zeros(50)
        obs[1] = 0.1
        obs[2] = 0.05
        
        action1 = heuristic_policy(obs)
        action2 = heuristic_policy(obs)
        
        assert np.allclose(action1, action2), \
            "Heuristic policy should be deterministic"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
