"""
Lesson 3.1: Policy Comparison - Random vs. Heuristic

This script demonstrates two simple policies for robot control:
1. Random Policy: Selects actions uniformly at random.
2. Heuristic Policy: Uses a proportional controller to counteract tilt.

Usage:
    Run this script to see the cumulative survival reward for each policy.
    Requires a MuJoCo environment with a humanoid robot (e.g., Unitree G1).
"""

import numpy as np

# --- Configuration ---
# Observation indices (adjust based on your robot's observation space)
# These are placeholder indices; adjust to your model's obs structure.
PITCH_INDEX = 1  # Index for pitch (forward/backward tilt) in observation
ROLL_INDEX = 2   # Index for roll (side-to-side tilt) in observation

# Heuristic policy gain
Kp = 1.5  # Proportional gain for corrective torques

# Number of actuators (joints) in the robot
NUM_ACTUATORS = 23  # Adjust to your robot's action space dimension


def random_policy(observation: np.ndarray) -> np.ndarray:
    """
    Random Policy: Ignores observation and returns random actions.
    
    Args:
        observation: The current state observation from the environment.
        
    Returns:
        A random action vector with values in [-1, 1].
    """
    # Completely ignore the observation
    action = np.random.uniform(-1.0, 1.0, size=NUM_ACTUATORS)
    return action


def heuristic_policy(observation: np.ndarray) -> np.ndarray:
    """
    Heuristic Policy: Simple proportional controller to stay upright.
    
    This policy reads the robot's pitch and roll from the observation
    and applies corrective torques to counteract the tilt.
    
    Args:
        observation: The current state observation from the environment.
                     Expected to contain pitch and roll at specified indices.
        
    Returns:
        An action vector with corrective torques applied.
    """
    # Start with zero action
    action = np.zeros(NUM_ACTUATORS)
    
    # Read pitch and roll from observation
    # Pitch > 0 means leaning forward, < 0 means leaning backward
    # Roll > 0 means leaning right, < 0 means leaning left
    pitch = observation[PITCH_INDEX]
    roll = observation[ROLL_INDEX]
    
    # Apply corrective torques
    # If leaning forward (pitch > 0), push hips backward (negative torque)
    # If leaning backward (pitch < 0), push hips forward (positive torque)
    # Similarly for roll affecting ankle/hip abduction
    
    # Simplified: Apply correction to first few actuators (e.g., hip joints)
    # In a real implementation, map these to specific joint indices
    hip_correction = -Kp * pitch
    ankle_correction = -Kp * roll * 0.5  # Smaller gain for roll
    
    # Apply to hip joints (indices 0-5 as a placeholder)
    action[0:6] = hip_correction
    
    # Apply to ankle joints (indices 6-11 as a placeholder)
    action[6:12] = ankle_correction
    
    # Clip to valid range
    action = np.clip(action, -1.0, 1.0)
    
    return action


def compare_policies(env, num_steps: int = 500) -> dict:
    """
    Compare the performance of random vs. heuristic policies.
    
    Args:
        env: A MuJoCo environment with reset() and step() methods.
        num_steps: Number of simulation steps to run.
        
    Returns:
        A dictionary with cumulative rewards for each policy.
    """
    results = {}
    
    policies = {
        "random": random_policy,
        "heuristic": heuristic_policy,
    }
    
    for name, policy_fn in policies.items():
        # Reset environment
        observation = env.reset()
        cumulative_reward = 0.0
        
        for step in range(num_steps):
            # Get action from policy
            action = policy_fn(observation)
            
            # Step the environment
            observation, reward, done, info = env.step(action)
            cumulative_reward += reward
            
            if done:
                print(f"[{name}] Episode ended at step {step}")
                break
        
        results[name] = cumulative_reward
        print(f"[{name}] Cumulative Reward: {cumulative_reward:.2f}")
    
    return results


# --- Standalone Demo (no MuJoCo required) ---
if __name__ == "__main__":
    print("=== Policy Comparison Demo ===")
    print()
    
    # Create a fake observation for demonstration
    fake_observation = np.zeros(50)
    fake_observation[PITCH_INDEX] = 0.1  # Slight forward lean
    fake_observation[ROLL_INDEX] = -0.05  # Slight left lean
    
    print("Fake observation (simulating slight forward-left tilt):")
    print(f"  Pitch: {fake_observation[PITCH_INDEX]:.2f} rad")
    print(f"  Roll: {fake_observation[ROLL_INDEX]:.2f} rad")
    print()
    
    # Get actions from each policy
    random_action = random_policy(fake_observation)
    heuristic_action = heuristic_policy(fake_observation)
    
    print("Random Policy Action (first 12 joints):")
    print(f"  {random_action[:12]}")
    print()
    
    print("Heuristic Policy Action (first 12 joints):")
    print(f"  {heuristic_action[:12]}")
    print()
    
    print("Note: The heuristic policy applies structured corrections,")
    print("      while the random policy outputs arbitrary values.")
    print()
    print("To run the full comparison, integrate with your MuJoCo env:")
    print("  results = compare_policies(your_mujoco_env, num_steps=500)")
