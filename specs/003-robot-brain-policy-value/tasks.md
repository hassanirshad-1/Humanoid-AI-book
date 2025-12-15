---
description: "Task list for Chapter 3: The Robot's Brain"
---

# Tasks: Chapter 3 - The Robot's Brain

**Input**: `specs/003-robot-brain-policy-value/plan.md`
**Prerequisites**: Chapter 1 completion.

## Phase 1: Setup & Scaffolding

**Purpose**: Initialize directory structure for the new chapter.

- [x] T001 [P] Create directory `frontend/docs/chapter-03-policy-and-value`
- [x] T002 [P] Create directory `frontend/docs/chapter-03-policy-and-value/code`
- [x] T003 Update `frontend/sidebars.ts` to include Chapter 3 items

---

## Phase 2: User Story 1 - Understanding Policy (Priority: P1)

**Goal**: Explain policies (deterministic vs stochastic) and implement the random vs heuristic comparison.

### Implementation for User Story 1

- [x] T004 create `frontend/docs/chapter-03-policy-and-value/3.1-policy.mdx` (Content: Hook, Intuition, Formalism)
- [x] T005 Create `frontend/docs/chapter-03-policy-and-value/code/lesson_3_1_policy_comparison.py` (Random vs Heuristic Logic)
- [x] T006 Create `tests/test_lesson_3_1.py` to verify heuristic outperforms random

---

## Phase 3: User Story 2 - Grasping Return (Priority: P1)

**Goal**: Explain discount factors and cumulative reward calculation.

### Implementation for User Story 2

- [x] T007 Create `frontend/docs/chapter-03-policy-and-value/3.2-return.mdx` (Content: Math of Return, Marshmallow Analogy)

---

## Phase 4: User Story 3 - Visualizing Value Functions (Priority: P1)

**Goal**: Explain V/Q functions and visualize them with a heatmap.

### Implementation for User Story 3

- [x] T008 Create `frontend/docs/chapter-03-policy-and-value/3.3-value-function.mdx` (Content: Map analogy, Bellman Intuition)
- [x] T009 Create `frontend/docs/chapter-03-policy-and-value/code/lesson_3_3_value_heatmap.py` (Matplotlib Visualization)

---

## Phase 5: Verification

**Purpose**: Ensure everything builds and runs correctly.

- [x] T010 [P] Run `pytest tests/test_lesson_3_1.py`
- [x] T011 [P] Run `npm run build` to verify MDX/LaTeX syntax
- [ ] T012 Manual check: Visual inspection of `npm run start` (localhost)
