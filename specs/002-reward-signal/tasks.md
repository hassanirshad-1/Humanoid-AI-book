# Actionable Tasks: Chapter 2 - Reward Signal

This document outlines the SMART tasks required to implement the "Reward Signal" feature, as detailed in the implementation plan.

## Phase 1: Setup & Scaffolding

-   [X] T001 Create the directory for code examples at `frontend/docs/chapter-02-reward-signal/code`.
-   [X] T002 Update `frontend/sidebars.ts` to add a new category for "Chapter 2: The Reward Signal" with placeholders for the five upcoming lessons.

## Phase 2: Content Implementation (Conceptual Lessons)

This phase focuses on the lessons that are primarily text and concepts. These tasks can be worked on in parallel.

-   [X] T003 [P] [US1] Create the content for **Lesson 2.1** in `frontend/docs/chapter-02-reward-signal/2.1-what-is-a-reward.mdx`.
-   [X] T004 [P] [US1] Create the content for **Lesson 2.4** in `frontend/docs/chapter-02-reward-signal/2.4-reward-hacking.mdx`.
-   [X] T005 [P] [US1] Create the content for **Lesson 2.5** in `frontend/docs/chapter-02-reward-signal/2.5-sparse-vs-dense.mdx`.

## Phase 3: Implementation of User Story 2 (Your First Reward)

-   **User Story**: As a learner, I want to implement a simple reward function in code to see how it works in a simulation.
-   **Independent Test Criteria**: A user can run `tests/test_lesson_2_2.py` successfully. The `lesson_2_2_survival_reward.py` script can be integrated into the main simulation loop from Ch. 1, and a reward value is printed to the console.

-   [X] T006 [US2] Create the content and embed the code for **Lesson 2.2** in `frontend/docs/chapter-02-reward-signal/2.2-first-reward.mdx`.
-   [X] T007 [US2] Implement the Python reward function in `frontend/docs/chapter-02-reward-signal/code/lesson_2_2_survival_reward.py`.
-   [X] T008 [US2] Create unit tests for the survival reward function in `tests/test_lesson_2_2.py`.

## Phase 4: Implementation of User Story 4 (Reward Shaping)

-   **User Story**: As a future RL practitioner, I want to learn about reward shaping so that I can design more effective reward functions.
-   **Independent Test Criteria**: A user can run `tests/test_lesson_2_3.py` successfully. The `lesson_2_3_shaped_reward.py` script can be integrated into the main simulation loop, and a shaped reward value is printed.

-   [X] T009 [US3] Create the content and embed the code for **Lesson 2.3** in `frontend/docs/chapter-02-reward-signal/2.3-reward-shaping.mdx`.
-   [X] T010 [US3] Implement the shaped reward function in `frontend/docs/chapter-02-reward-signal/code/lesson_2_3_shaped_reward.py`.
-   [X] T011 [US3] Create unit tests for the shaped reward function in `tests/test_lesson_2_3.py`.

## Phase 5: Verification & Polish

-   [X] T012 Run the full test suite with `pytest` to ensure all new and existing tests pass.
-   [ ] T013 Start the frontend server with `npm run start` and visually inspect all five new lesson pages for correct rendering, formatting, and navigation.
-   [ ] T014 Manually verify that the code snippets from `T007` and `T010` are runnable in the context of the main simulation loop from Chapter 1.

## Dependencies & Parallel Execution

-   **Dependencies**: Phase 2, 3, and 4 can commence after Phase 1 is complete. Phase 5 depends on all other phases.
-   **Parallel Opportunities**:
    -   Tasks within Phase 2 (T003, T004, T005) are independent and can be executed in parallel.
    -   Phase 3 (US2) and Phase 4 (US3) are independent of each other and can be worked on in parallel.

## Implementation Strategy
The suggested MVP (Minimum Viable Product) for this feature would be the completion of **Phase 1 and Phase 2**, which delivers the foundational concepts of reward signals. Phase 3 and 4 deliver the practical coding exercises and can be implemented next.
