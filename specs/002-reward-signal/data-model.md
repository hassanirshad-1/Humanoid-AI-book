# Data Model: Chapter 2 - Reward Signal

## 1. Overview
The implementation of Chapter 2 does not introduce any new persistent data models or complex data structures. The primary data concepts are transient and used for calculation within the simulation loop.

## 2. Key Data Concepts

### Reward
-   **Type**: `float`
-   **Description**: A scalar value representing the feedback from the environment at a given timestep. It is calculated by a reward function based on the robot's state and/or action.
-   **Example**: `1.0` (for maintaining balance), `-0.05` (for energy usage), `0.2` (for forward velocity).

### State
-   **Type**: `object` (MuJoCo data object)
-   **Description**: A collection of data representing the robot's physical state at a single point in time. The reward functions will primarily use subsets of this data.
-   **Relevant Fields for this Chapter**:
    -   `qpos` (generalized positions): Used to determine the robot's orientation (e.g., upright or fallen).
    -   `qvel` (generalized velocities): Used to determine the robot's velocity.
    -   `ctrl` (control signals/torques): Used to calculate energy consumption.

## 3. Relationships
-   The `Reward` is a pure function of the `State`. For a given state `s`, the reward function `R(s)` will always produce the same scalar `Reward` value.

## 4. Schema
No database or API schemas are required for this feature as all data is ephemeral and used within the local Python simulation script.
