# ADR-002: Simulation and Coding Environment Stack

- **Status:** Accepted
- **Date:** 2025-12-11
- **Feature:** 001-intro-robotics
- **Context:** To provide hands-on, interactive coding lessons for robotics, the textbook requires a standard programming environment and a physics simulator. The simulator must be scientifically accurate, performant, and, most importantly, accessible to students who may not have high-end hardware. The chosen language must be relevant to the modern AI and robotics fields.

## Decision

The project will use the following stack for the simulation and coding environment:
- **Programming Language**: Python 3.12+, which is the de facto standard for AI and robotics research and development.
- **Physics Simulator**: MuJoCo (Multi-Joint dynamics with Contact), used via its official Python bindings.
- **Testing Framework**: Pytest, for creating and running tests against the example code to ensure correctness.

## Consequences

### Positive

- **Industry Standard**: Python and MuJoCo are widely used in top AI research labs (including DeepMind, which maintains MuJoCo) and academia.
- **Accessibility**: MuJoCo can run efficiently on standard CPUs, making it accessible to students without expensive, high-end GPUs. It runs easily in free environments like Google Colab.
- **Accuracy & Speed**: MuJoCo is renowned for its fast and accurate handling of contact physics, which is critical for robotics simulation.
- **Mature Ecosystem**: Python has a vast ecosystem of libraries (`numpy`, `matplotlib`, etc.) that are essential for scientific computing. Pytest is a robust and feature-rich testing solution.

### Negative

- **Basic Rendering**: MuJoCo's rendering is functional but not photorealistic compared to game-engine-based simulators. This might be less visually engaging for some students.
- **Setup Hurdle**: Setting up a local Python environment and dependencies can be a barrier for absolute beginners, requiring clear instructions.

## Alternatives Considered

- **Alternative A: NVIDIA Isaac Lab**
  - **Description**: A photorealistic, GPU-parallel simulator built on Omniverse.
  - **Why Rejected**: It has a very high barrier to entry, requiring a powerful NVIDIA GPU and a steep learning curve associated with the Omniverse platform. This makes it unsuitable for an introductory chapter. It is noted in `research.md` as a potential tool for advanced, sim-to-real focused chapters.

- **Alternative B: Gazebo**
  - **Description**: A simulator that is native to the Robot Operating System (ROS) ecosystem.
  - **Why Rejected**: Gazebo is generally considered too slow for the type of rapid, parallelized policy training that is central to modern physical AI. Its architecture is not optimized for this domain compared to MuJoCo or Isaac Lab.

## References

- **Implementation Plan**: `specs/001-intro-robotics/plan.md`
- **Research**: `specs/001-intro-robotics/research.md`
