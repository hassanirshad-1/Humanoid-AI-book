# Feature Specification: The Robot's Brain: Policies & Value Functions

**Feature Branch**: `003-robot-brain-policy-value`  
**Created**: December 15, 2025  
**Status**: Draft  
**Input**: User description: "Proposed Chapter 3: The Robot's Brain: Policies & Value Functions. Lesson 3.1: The Policy (The Strategy) - Concrete Hook: Comparing a "reflex" (interactive code: simple if-then logic) vs. a "strategy" (stochastic/probabilistic choice). Concept: Deterministic vs. Stochastic Policies. Mapping States -> Actions. Sim/Code: Implementing a simple random walk vs. a heuristic policy for our robot. Lesson 3.2: The Return (The Long Game) - Concrete Hook: "Marshmallow Test" for robots. $100 now vs $1000 later. Concept: Discount Factors ($\gamma$), Cumulative Reward, and Finite vs. Infinite Horizons. Sim/Code: Calculating returns for different sample trajectories. Lesson 3.3: The Value Function (The Map) - Concrete Hook: A treasure map where every spot tells you "how close" you are to the gold, not just the gold itself. Concept: State-Value $V(s)$ and Action-Value $Q(s,a)$. The Bellman Intuition (recursive definition). Sim/Code: Visualizing a "Value Heatmap" on a simple Gridworld or MuJoCo terrain"

## User Scenarios & Testing

### User Story 1 - Understanding Policy (Priority: P1)

A student wants to understand what a policy is and how it dictates a robot's actions in a given environment.

**Why this priority**: Fundamental concept for understanding how robots make decisions. Without this, subsequent topics about learning policies are difficult to grasp.

**Independent Test**: Student can correctly answer questions or complete exercises that require identifying and explaining different types of policies and their implications for robot behavior.

**Acceptance Scenarios**:

1.  **Given** a description of a robot's behavior, **When** asked to identify the underlying policy type (deterministic/stochastic), **Then** the student can correctly classify it.
2.  **Given** a simple state, **When** presented with a policy, **Then** the student can predict the action(s) the robot would take.

---

### User Story 2 - Grasping Return (Priority: P1)

A student wants to understand how a robot evaluates long-term rewards and the concept of "the long game" in reinforcement learning.

**Why this priority**: Crucial for comprehending how immediate rewards contribute to future goals and how the robot optimizes for cumulative success.

**Independent Test**: Student can correctly calculate or estimate the return for various robot trajectories, demonstrating an understanding of discount factors.

**Acceptance Scenarios**:

1.  **Given** a sequence of rewards and a discount factor, **When** asked to calculate the cumulative discounted return for a trajectory, **Then** the student can perform the calculation accurately.
2.  **Given** two different trajectories with varying immediate and future rewards, **When** asked to compare their long-term value, **Then** the student can justify their comparison using the concept of discount factors.

---

### User Story 3 - Visualizing Value Functions (Priority: P1)

A student wants to comprehend how value functions represent the desirability of states and actions, acting as a "map" for optimal behavior.

**Why this priority**: Provides the framework for understanding how an agent learns to assess the "goodness" of being in a particular state or taking a particular action, leading towards optimal behavior.

**Independent Test**: Student can interpret a visual representation of a value function (e.g., a heatmap) and explain what high or low values signify for the robot's decision-making.

**Acceptance Scenarios**:

1.  **Given** a simple environment and its state-value function V(s), **When** presented with a state, **Then** the student can explain the expected long-term reward from that state.
2.  **Given** a simple environment and its action-value function Q(s,a), **When** presented with a state-action pair, **Then** the student can explain the expected long-term reward from taking that action in that state.
3.  **Given** a "Value Heatmap" visualization, **When** asked to identify the most desirable or least desirable regions/actions, **Then** the student can do so correctly.

---

### Edge Cases

-   What happens when a robot's policy leads to a terminal state with no further rewards?
-   How are returns handled in continuous versus episodic tasks?
-   How do different discount factors (e.g., $\gamma = 0$ vs. $\gamma = 0.99$) influence the robot's "long-term thinking"?

## Requirements

### Functional Requirements

-   **FR-001**: The chapter MUST clearly define "policy" and its role in robot decision-making, differentiating between a "reflex" and a "strategy."
-   **FR-002**: The chapter MUST explain the concepts of deterministic vs. stochastic policies with illustrative examples and interactive elements.
-   **FR-003**: The chapter MUST provide a simple simulation/code example demonstrating a random walk vs. a heuristic policy for a robot, allowing students to run and modify it.
-   **FR-004**: The chapter MUST introduce the concept of "return" in reinforcement learning, including cumulative reward, discount factors ($\gamma$), and finite vs. infinite horizons.
-   **FR-005**: The chapter MUST include interactive examples or exercises for calculating returns for different sample trajectories, possibly using a "Marshmallow Test" analogy.
-   **FR-006**: The chapter MUST define state-value $V(s)$ and action-value $Q(s,a)$ functions, explaining their purpose as "scorecards" or "maps."
-   **FR-007**: The chapter MUST explain the Bellman Intuition (recursive definition) for value functions.
-   **FR-008**: The chapter MUST provide a visual representation (e.g., an interactive heatmap) of a value function in a simple environment (e.g., Gridworld or MuJoCo terrain), allowing exploration of different states/actions.

### Key Entities

-   **Policy**: The strategy that determines the agent's actions based on the current state.
-   **Return**: The total discounted sum of rewards received from a given time step onwards.
-   **Value Function**: A function that estimates how good it is for the agent to be in a given state or to perform a given action in a given state.
-   **State-Value Function ($V(s)$)**: The expected return starting from state `s` and following a policy.
-   **Action-Value Function ($Q(s,a)$)**: The expected return starting from state `s`, taking action `a`, and then following a policy.
-   **Discount Factor ($\gamma$)**: A parameter between 0 and 1 that discounts future rewards.

## Success Criteria

### Measurable Outcomes

-   **SC-001**: 90% of students can correctly identify and explain the purpose of a policy and distinguish between deterministic and stochastic policies in a robot's decision-making process after completing Lesson 3.1.
-   **SC-002**: 85% of students can accurately calculate the return for a given trajectory and discount factor, and explain the implications of different discount rates, after completing Lesson 3.2.
-   **SC-003**: 80% of students can correctly interpret an interactive visual representation of a value function (e.g., heatmap) and explain what state-value $V(s)$ and action-value $Q(s,a)$ signify in the context of robot decision-making after completing Lesson 3.3.
-   **SC-004**: Student engagement with the interactive code examples and visualizations (e.g., random walk vs. heuristic policy, trajectory returns calculator, value heatmap explorer) is recorded as above 75% for unique user interactions.