# Feature Specification: Introduction to Robotics & Physical AI

**Feature Branch**: `001-intro-robotics`
**Created**: 2025-12-10
**Status**: Draft
**Input**: User description: "introduction-to-robotics"

## User Scenarios & Testing

### User Story 1 - Lesson 1.1: Philosophy (Priority: P1)
A student wants to understand the shift from "Classical Robotics" to "Physical AI" so they know why learning modern methods matters.
**Why this priority**: Sets the pedagogical hook ("The Falling Robot") required by the Constitution.
**Independent Test**: Student can explain the difference between a scripted policy and a learned policy.
**Acceptance Scenarios**:
1. **Given** the "Falling Robot" comparison video, **When** asked "Why did the 2015 robot fall?", **Then** the student answers "Rigid programming inability to adapt" (not physics).
2. **Given** the term "Physical AI", **When** queried, **Then** student defines it as "Embodied intelligence learning from interaction."

### User Story 2 - Lesson 1.2: The Hardware (Priority: P1)
A student needs to know the anatomy of the "Hero Robot" (Unitree G1) to understand what they are controlling.
**Why this priority**: Connects code to physical reality (Actuators, IMUs).
**Independent Test**: Student can label the joint motors on a G1 diagram.
**Acceptance Scenarios**:
1. **Given** a diagram of the G1, **When** asked to point to the actuator, **Then** student identifies the joint motor.
2. **Given** a sensor list, **When** asked "What is Proprioception?", **Then** student identifies IMU/Joint Encoders.

### User Story 3 - Lesson 1.3: The "Matrix" (Simulation) (Priority: P1)
A student wants to run their first simulation in MuJoCo to verify their environment is ready.
**Why this priority**: Gatekeeper for all future coding tasks.
**Independent Test**: Student successfully executes `python load_sim.py` and sees a robot.
**Acceptance Scenarios**:
1. **Given** a standard local Python environment, **When** student runs the setup script, **Then** a MuJoCo window opens with a loaded MJCF model.

### User Story 4 - Lesson 1.4: First Policy (Priority: P2)
A student wants to send a command to the robot and see it move (even if it falls).
**Why this priority**: closes the "Pixels-to-Torque" loop.
**Independent Test**: Student writes a loop sending random actions to the robot.
**Acceptance Scenarios**:
1. **Given** the simulation is running, **When** the student sends a `d_pos` command, **Then** the robot's leg moves in the visualization.

## Requirements

### Functional Requirements
- **FR-001**: The feature MUST deliver 4 distinct lessons: 1.1 Philosophy, 1.2 Hardware, 1.3 Sim Setup, 1.4 First Policy.
- **FR-002**: Lesson 1.1 MUST include the "Falling Robot" narrative/visuals.
- **FR-003**: Lesson 1.2 MUST use Unitree G1 specifications (23-35 Degrees of Freedom) as the reference model.
- **FR-004**: Lesson 1.3 MUST provide a copy-paste runnable Python script using `mujoco` bindings.
- **FR-005**: Lesson 1.4 MUST demonstrate the "Action Loop" (Observation -> Policy -> Action).
- **FR-006**: All code snippets MUST be compatible with Python 3.12+.
- **FR-007**: The content MUST strictly follow the "Expanded Concrete Sandwich" pedagogical structure, designed to be more accessible for beginners. Each lesson should contain the following sections in order:
    1.  **The Concrete Hook**: A compelling, real-world example or visual.
    2.  **The Core Intuition**: A high-level, non-technical explanation.
    3.  **The Analogy**: A simple, non-technical analogy to make the concept more relatable.
    4.  **The Formalism**: The introduction to the technical terms and notation.
    5.  **Code Representation**: A simple code block showing how the formal concept is represented in code.
    6.  **"Gotchas" / Key Insights**: A section for common pitfalls or key takeaways.

### Key Entities
- **Lesson**: A distinct MDX file representing a unit of learning.
- **Asset**: A diagram, GIF, or MJCF model file.
- **CodeSnippet**: A precise block of Python code to be embedded.

## Success Criteria

### Measurable Outcomes
- **SC-001**: 100% of code snippets in Lesson 1.3 and 1.4 run without errors in a fresh python environment.
- **SC-002**: The "Falling Robot" hook is present in the first 300 words of Lesson 1.1.
- **SC-003**: Lesson 1.2 diagram accurately reflects the Unitree G1 kinematics.
- **SC-004**: RAG chunking successful (each lesson has clear H2 headers).
