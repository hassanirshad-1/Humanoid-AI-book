# Research Phase 0: Introduction to Physical AI & Humanoid Robotics
**Date**: 2025-12-10
**Status**: Verified (2023-2025 Sources)

## 1. Simulator Landscape (2025 Decision Matrix)

For a "Physical AI" textbook, the simulator choice is critical. The 2024/2025 landscape has shifted heavily towards GPU-accelerated physics.

| Simulator | Type | Best For | Pros | Cons |
| :--- | :--- | :--- | :--- | :--- |
| **NVIDIA Isaac Lab** | GPU-Parallel | **RL & Sim-to-Real** | Masses of environments (4000+), Photorealistic (RTX), used by Unitree/GR00T. | High GPU VRAM req. Steep learning curve (USD/Omniverse). |
| **MuJoCo (MJX)** | CPU/TPU | **Contact Physics** | Gold standard accuracy. Google DeepMind backed. Runs on Colab (Free). | Rendering is basic. Slower for massive visuals. |
| **Gazebo** | ROS-Native | **Navigation** | standard ROS integration. | Too slow for modern RL walking policies. Legacy architecture. |

**Recommendation for Chapter 1**:
*   **Primary**: **MuJoCo** (via Python bindings).
    *   *Reason*: It is accessible to students (runs on CPU/Colab), mathematically rigorous, and now supports GPU acceleration via MJX for advanced chapters.
*   **Advanced**: **Isaac Lab** (for Chapter 10+ Sim-to-Real).

## 2. State-of-the-Art Control Archtectures (2024)

The "Classical Control" pipeline is being replaced by "AI-Native" pipelines.

### The Shift
*   **Old**: Perception -> State Estimation -> Planning (MPC) -> Whole Body Control (WBC) -> Torque.
*   **New (Physical AI)**: Vision + Proprioception -> **Neural Policy (Transformer/Diffusion)** -> Joint Positions/Torques.

### Key Technologies to Cover
1.  **VLA (Vision-Language-Action) Models**:
    *   Models like **Octo** and **RT-2** allow robots to understand "Pick up the red apple" directly from pixels.
2.  **Diffusion Policies**:
    *   Replacing traditional trajectory optimization. Handles multimodal distributions better (e.g., "go left or right" vs "go average").
3.  **Sim-to-Real & Domain Randomization**:
    *   The secret sauce of 2024 humanoids (Unitree, Tesla). Training in simulation with randomized friction/mass/latency to survive the real world.

## 3. Key Hardware References (The "Hero" Robots)

This book should reference accessible/standard hardware:
1.  **Unitree G1 ($16k)**: The current academic standard for accessible humanoids.
2.  **Tesla Optimus Gen 2**: The industrial benchmark (proprietary, but architecture is widely discussed).
3.  **Fourier GR-1**: A common competitor in the mid-range.

## 4. Required Citations (APA Style)

These papers form the backbone of the "AI-Native" claim:

*   **Octo Model Team et al. (2023).** *Octo: An Open-Source General-Purpose Robot Policy.* arXiv preprint arXiv:2310.08864.
*   **Brohan, A., et al. (2023).** *RT-2: Vision-Language-Action Models with Web-Scale Knowledge.* Conference on Robot Learning (CoRL).
*   **Todorov, E., Erez, T., & Tassa, Y. (2012).** *MuJoCo: A physics engine for model-based control.* IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). (Classic, but essential).
*   **Miki, T., et al. (2022).** *Learning robust perceptive locomotion for quadrupedal robots in the wild.* Science Robotics, 7(62). (The "Learned Locomotion" bible).

## 5. Pedagogical "Hook" for Chapter 1
*   **Concept**: "The Falling Robot".
*   **Visual**: Show a compilation of DARPA Robotics Challenge (2015) failures vs. Unitree H1 backflipping (2024).
*   **Lesson**: "What changed? Not the physics (F=ma), but the **Policy** (Code vs. Neural Net)."
