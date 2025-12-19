"""
Lesson 3.3: Value Function Heatmap Visualization

This script demonstrates how to compute and visualize a value function
for a simple 2D grid world using Value Iteration (Dynamic Programming).

Usage:
    Run this script to see a heatmap of state values.
    Requires: numpy, matplotlib

    pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


def create_grid_world(size: int = 5) -> np.ndarray:
    """
    Create a simple grid world with rewards.
    
    Args:
        size: The size of the grid (size x size).
        
    Returns:
        A 2D numpy array of rewards for each state.
    """
    rewards = np.zeros((size, size))
    
    # Goal state: bottom-right corner (high reward)
    rewards[size - 1, size - 1] = 10.0
    
    # Obstacle: center of the grid (negative reward)
    center = size // 2
    rewards[center, center] = -5.0
    
    # Slightly negative reward for all other states (encourages efficiency)
    for i in range(size):
        for j in range(size):
            if rewards[i, j] == 0:
                rewards[i, j] = -0.1
    
    return rewards


def value_iteration(
    rewards: np.ndarray,
    gamma: float = 0.9,
    threshold: float = 0.001,
    max_iterations: int = 1000
) -> np.ndarray:
    """
    Compute the optimal value function using Value Iteration.
    
    This is a Dynamic Programming algorithm that iteratively updates
    state values until convergence.
    
    Args:
        rewards: 2D array of rewards for each state.
        gamma: Discount factor.
        threshold: Convergence threshold.
        max_iterations: Maximum number of iterations.
        
    Returns:
        2D array of state values V(s).
    """
    size = rewards.shape[0]
    V = np.zeros((size, size))
    
    # Actions: up, down, left, right
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for iteration in range(max_iterations):
        V_new = np.copy(V)
        delta = 0
        
        for i in range(size):
            for j in range(size):
                # Terminal state (goal) has fixed value
                if i == size - 1 and j == size - 1:
                    V_new[i, j] = rewards[i, j]
                    continue
                
                # Compute value for each action and take the max (optimal policy)
                action_values = []
                for di, dj in actions:
                    ni, nj = i + di, j + dj
                    
                    # Check bounds
                    if 0 <= ni < size and 0 <= nj < size:
                        # Value = reward + gamma * V(next_state)
                        value = rewards[i, j] + gamma * V[ni, nj]
                    else:
                        # Can't move out of bounds; stay in place
                        value = rewards[i, j] + gamma * V[i, j]
                    
                    action_values.append(value)
                
                # Bellman optimality: take the max over all actions
                V_new[i, j] = max(action_values)
                delta = max(delta, abs(V_new[i, j] - V[i, j]))
        
        V = V_new
        
        # Check for convergence
        if delta < threshold:
            print(f"Value Iteration converged in {iteration + 1} iterations.")
            break
    else:
        print(f"Value Iteration did not converge in {max_iterations} iterations.")
    
    return V


def plot_value_heatmap(V: np.ndarray, title: str = "State-Value Function V(s)"):
    """
    Plot the value function as a heatmap.
    
    Args:
        V: 2D array of state values.
        title: Title for the plot.
    """
    plt.figure(figsize=(8, 6))
    
    # Use a colormap where higher values are darker/more intense
    plt.imshow(V, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Value V(s)')
    
    # Add value annotations on each cell
    size = V.shape[0]
    for i in range(size):
        for j in range(size):
            plt.text(j, i, f'{V[i, j]:.2f}', ha='center', va='center', 
                     color='white' if V[i, j] < np.mean(V) else 'black',
                     fontsize=10)
    
    plt.title(title)
    plt.xlabel('Column (j)')
    plt.ylabel('Row (i)')
    plt.xticks(range(size))
    plt.yticks(range(size))
    
    # Mark special states
    plt.scatter([size - 1], [size - 1], color='gold', s=200, marker='*', 
                label='Goal', zorder=5)
    plt.scatter([size // 2], [size // 2], color='red', s=200, marker='x', 
                label='Obstacle', zorder=5)
    plt.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('value_heatmap.png', dpi=150)
    print("Saved heatmap to 'value_heatmap.png'")
    plt.show()


def extract_optimal_policy(V: np.ndarray, rewards: np.ndarray, gamma: float = 0.9) -> np.ndarray:
    """
    Extract the optimal policy from the value function.
    
    Args:
        V: 2D array of state values.
        rewards: 2D array of rewards.
        gamma: Discount factor.
        
    Returns:
        2D array of action indices (0=up, 1=down, 2=left, 3=right).
    """
    size = V.shape[0]
    policy = np.zeros((size, size), dtype=int)
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    action_names = ['↑', '↓', '←', '→']
    
    for i in range(size):
        for j in range(size):
            action_values = []
            for di, dj in actions:
                ni, nj = i + di, j + dj
                if 0 <= ni < size and 0 <= nj < size:
                    value = rewards[i, j] + gamma * V[ni, nj]
                else:
                    value = rewards[i, j] + gamma * V[i, j]
                action_values.append(value)
            
            policy[i, j] = np.argmax(action_values)
    
    return policy


def plot_policy(policy: np.ndarray, V: np.ndarray):
    """
    Plot the optimal policy as arrows on the grid.
    """
    size = policy.shape[0]
    action_arrows = ['↑', '↓', '←', '→']
    
    plt.figure(figsize=(8, 6))
    plt.imshow(V, cmap='viridis', interpolation='nearest', alpha=0.5)
    
    for i in range(size):
        for j in range(size):
            arrow = action_arrows[policy[i, j]]
            plt.text(j, i, arrow, ha='center', va='center', fontsize=20, color='black')
    
    plt.title('Optimal Policy π*(s)')
    plt.xlabel('Column (j)')
    plt.ylabel('Row (i)')
    plt.xticks(range(size))
    plt.yticks(range(size))
    plt.tight_layout()
    plt.savefig('optimal_policy.png', dpi=150)
    print("Saved policy to 'optimal_policy.png'")
    plt.show()


# --- Main Demo ---
if __name__ == "__main__":
    print("=== Value Function Heatmap Demo ===")
    print()
    
    # Create a 5x5 grid world
    grid_size = 5
    rewards = create_grid_world(grid_size)
    
    print("Reward Grid:")
    print(rewards)
    print()
    
    # Run Value Iteration
    gamma = 0.9
    V = value_iteration(rewards, gamma=gamma)
    
    print()
    print("Computed Value Function V(s):")
    print(V)
    print()
    
    # Plot the heatmap
    plot_value_heatmap(V, title=f"State-Value Function V(s) with γ={gamma}")
    
    # Extract and plot optimal policy
    policy = extract_optimal_policy(V, rewards, gamma)
    plot_policy(policy, V)
    
    print()
    print("Key Observations:")
    print("  - The goal state (bottom-right) has the highest value.")
    print("  - States near the goal have higher values (gradient towards goal).")
    print("  - The obstacle (center) has negative value and affects neighbors.")
    print("  - The optimal policy points towards the goal from every state.")
