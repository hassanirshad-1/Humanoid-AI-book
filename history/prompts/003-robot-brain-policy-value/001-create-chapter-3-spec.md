---
id: 001-create-chapter-3-spec
title: Create Chapter 3 Spec
stage: spec
date: 2025-12-15
surface: cli
model: gemini-1.5-flash
feature: 003-robot-brain-policy-value
branch: 003-robot-brain-policy-value
user: hassanirshad-1
command: /sp.specify
labels: [chapter-content, specification]
links:
  spec: specs/003-robot-brain-policy-value/spec.md
  ticket: 
  adr: 
  pr: 
files:
- specs/003-robot-brain-policy-value/spec.md
- specs/003-robot-brain-policy-value/checklists/requirements.md
tests:
---

## Prompt

"Based on our curriculum so far (Chapter 1: Intro & Chapter 2: Reward Signal), the most logical next step is to define how the robot actually makes decisions and how it judges its long-term prospects.

In Reinforcement Learning, once you have the Goal (Reward), you need the Brain (Policy) and the Scorecard (Value Function).

I recommend Chapter 3: The Robot's Brain: Policies & Value Functions.

Proposed Structure (The Concrete Sandwich)
Lesson 3.1: The Policy (The Strategy)
Concrete Hook: Comparing a "reflex" (interactive code: simple if-then logic) vs. a "strategy" (stochastic/probabilistic choice).
Concept: Deterministic vs. Stochastic Policies. Mapping States -> Actions.
Sim/Code: Implementing a simple random walk vs. a heuristic policy for our robot.
Lesson 3.2: The Return (The Long Game)
Concrete Hook: "Marshmallow Test" for robots. $100 now vs $1000 later.
Concept: Discount Factors ($\gamma$), Cumulative Reward, and Finite vs. Infinite Horizons.
Sim/Code: Calculating returns for different sample trajectories.
Lesson 3.3: The Value Function (The Map)
Concrete Hook: A treasure map where every spot tells you "how close" you are to the gold, not just the gold itself.
Concept: State-Value $V(s)$ and Action-Value $Q(s,a)$. The Bellman Intuition (recursive definition).
Sim/Code: Visualizing a "Value Heatmap" on a simple Gridworld or MuJoCo terrain"

## Response snapshot

Created the feature specification for Chapter 3: "The Robot's Brain: Policies & Value Functions" based on the user's proposed structure, now correctly numbered as 003. The spec includes user scenarios, functional requirements, key entities, and measurable success criteria. A corresponding quality checklist was also generated and validated.

## Outcome

- ✅ Impact: spec-created
- 🧪 Tests: N/A
- 📁 Files: spec.md and checklists/requirements.md created and populated.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Corrected feature numbering issue. Manually created spec and checklist files after script failed. Confirmed correct numbering (003).

## Evaluation notes (flywheel)

- Failure modes observed: Parameter binding issues with create-new-feature.ps1 script persisted. Manual file creation was necessary.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Investigate create-new-feature.ps1 script for robust argument parsing across different shell environments.
