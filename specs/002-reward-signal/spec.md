# Specification: Chapter 2 - The Reward Signal

## 1. Feature Description
This feature introduces the concept of reward signals in reinforcement learning. The primary goal is to teach the reader how to design and implement mathematically sound and practically effective reward functions for a humanoid robot. By the end of this chapter, the reader will be able to write a Python function that correctly incentivizes a robot to stand upright and move, while understanding the potential pitfalls of poorly designed rewards.

## 2. User Stories
- **As a robotics student**, I want to understand what a reward signal is and why it's important so that I can define the goals for my robot's behavior.
- **As a learner**, I want to implement a simple reward function in code to see how it works in a simulation.
- **As a future RL practitioner**, I want to learn about reward shaping and its common pitfalls so that I can design more effective reward functions for complex tasks.
- **As a student**, I want to understand the difference between sparse and dense rewards to make informed decisions when setting up RL problems.

## 3. Functional Requirements
- **FR-1:** A new markdown file for **Lesson 2.1: What is a Reward?** must be created. It will introduce the fundamental concept of the scalar reward signal, using analogies and establishing the formal Reward Hypothesis.
- **FR-2:** A new markdown file for **Lesson 2.2: Your First Reward: Don't Fall Down** must be created. It will provide a Python code snippet to implement a basic survival reward (standing upright). The code must be runnable within the `action_loop.py` file from Chapter 1.
- **FR-3:** A new markdown file for **Lesson 2.3: Reward Shaping** must be created. It will explain how to craft rewards to guide behavior, with runnable code examples for a velocity reward and an energy penalty.
- **FR-4:** A new markdown file for **Lesson 2.4: The Pitfalls: Reward Hacking** must be created. It will explain common failure modes of reward design, like "reward hacking," using classic examples.
- **FR-5:** A new markdown file for **Lesson 2.5: Sparse vs. Dense Rewards** must be created. It will explain the trade-offs between these two types of reward structures.
- **FR-6:** Each lesson file (FR-1 to FR-5) must adhere to the "Gold Standard" structure: Hook, Intuition, Formalism, Code, Sim-to-Real, and a 3-question Knowledge Check.
- **FR-7:** The total cumulative reward must be printed to the console during the simulation loop to give the user immediate feedback.

## 4. Non-Functional Requirements
- **NFR-1 (Tone):** The instructional tone must be that of a "Collaborative Peer" – knowledgeable, encouraging, and friendly.
- **NFR-2 (Context):** All code and concepts must build directly upon the `unitree_g1` simulation environment and code established in Chapter 1.
- **NFR-3 (Clarity):** The text must explicitly state that this chapter only covers *calculating* rewards and that no agent *training* or *optimization* will occur. The robot will continue to act using random or fixed policies.

## 5. Success Criteria
- **SC-1:** Five complete MDX files corresponding to the lessons are successfully created and merged into the main branch.
- **SC-2:** A reader can copy and paste the code snippets from Lessons 2.2 and 2.3 into their existing `action_loop.py` and run the simulation without errors.
- **SC-3:** When the simulation is run with the new code, a "Score" or "Cumulative Reward" is visibly printed and updated on the console.
- **SC-4:** A reader can correctly answer the "Knowledge Check" questions at the end of each lesson, demonstrating their understanding of the concepts.

## 6. Assumptions & Dependencies
- **Dependency:** The reader has access to and has completed Chapter 1 of the textbook.
- **Assumption:** The reader has a working simulation environment with the `unitree_g1` robot model as configured in Chapter 1.
- **Assumption:** The reader is familiar with the `action_loop.py` script from Chapter 1 and its structure.

## 7. Out of Scope
- **RL Algorithms:** This chapter will not cover any RL training algorithms (e.g., PPO, Q-Learning). The agent's policy will remain random.
- **Value Functions:** Value functions, the Bellman equation, and the concept of discounted future rewards (gamma) are not included. The focus is solely on the immediate reward $R_t$.
- **Advanced State/Action Spaces:** The rewards will be based on simple, low-dimensional state information (e.g., torso orientation, velocity). Complex state from cameras or other sensors is not in scope.