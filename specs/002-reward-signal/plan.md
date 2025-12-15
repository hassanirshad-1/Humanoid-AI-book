# Implementation Plan: Chapter 2 - Reward Signal

## 1. Technical Context

This plan outlines the implementation for creating Chapter 2 of the AI-Native Textbook, focusing on "The Reward Signal." The implementation involves creating five new MDX content pages, two Python script examples, and corresponding unit tests.

-   **Files to Create**:
    -   `frontend/docs/chapter-02-reward-signal/2.1-what-is-a-reward.mdx`
    -   `frontend/docs/chapter-02-reward-signal/2.2-first-reward.mdx`
    -   `frontend/docs/chapter-02-reward-signal/2.3-reward-shaping.mdx`
    -   `frontend/docs/chapter-02-reward-signal/2.4-reward-hacking.mdx`
    -   `frontend/docs/chapter-02-reward-signal/2.5-sparse-vs-dense.mdx`
    -   `frontend/docs/chapter-02-reward-signal/code/lesson_2_2_survival_reward.py`
    -   `frontend/docs/chapter-02-reward-signal/code/lesson_2_3_shaped_reward.py`
    -   `tests/test_lesson_2_2.py`
    -   `tests/test_lesson_2_3.py`

-   **Files to Modify**:
    -   `frontend/sidebars.ts`: To add the new Chapter 2 to the Docusaurus sidebar navigation.

-   **Technology Stack**:
    -   **Content**: Docusaurus, MDX, React
    -   **Code**: Python 3.12+, Numpy, MuJoCo
    -   **Testing**: Pytest

-   **Dependencies**:
    -   This work is dependent on the completion of Chapter 1, specifically the `unitree_g1` simulation environment and the `action_loop.py` script structure.

-   **Clarifications**:
    -   No outstanding clarifications are needed. The feature specification is clear and detailed.

## 2. Constitution Check & Gate Evaluation

-   **AI Logic Isolation**: The plan adheres to this principle. All reward calculation logic will be in Python scripts, with the MDX files serving as the presentation layer.
-   **RAG Consistency**: The MDX heading structure will follow the established pattern from Chapter 1 to ensure consistency for the RAG pipeline.
-   **Secrets Management**: Not applicable for this feature, as no secrets are involved.

**Gate Evaluation**:
-   The plan is in full compliance with the project's constitution and the feature specification. There are no violations. **Proceed.**

## 3. Implementation Phases

### Phase 0: Research & Scaffolding

-   **Research**: The technical approach is straightforward and builds upon existing patterns. No specific research is required. The `research.md` document will confirm the use of existing technologies.
-   **Scaffolding**:
    1.  Create the directory `frontend/docs/chapter-02-reward-signal/code`.
    2.  Update `frontend/sidebars.ts` to include entries for the five new lessons in Chapter 2, ensuring they are ordered correctly.

### Phase 1: Content & Code Implementation

-   **Task 1: Lesson 2.1**: Create `2.1-what-is-a-reward.mdx`. This file is content-only and will introduce the core concepts of reward signals.
-   **Task 2: Lesson 2.2**:
    -   Create `2.2-first-reward.mdx`.
    -   Create the example script `code/lesson_2_2_survival_reward.py`, which includes the `calculate_reward` function for standing.
    -   Create the test file `tests/test_lesson_2_2.py` to validate the reward function's logic.
-   **Task 3: Lesson 2.3**:
    -   Create `2.3-reward-shaping.mdx`.
    -   Create the example script `code/lesson_2_3_shaped_reward.py` demonstrating reward shaping with velocity and energy components.
    -   Create the test file `tests/test_lesson_2_3.py` to validate the shaped reward function.
-   **Task 4: Lesson 2.4**: Create `2.4-reward-hacking.mdx`. This content-focused lesson will explain the pitfalls of reward design.
-   **Task 5: Lesson 2.5**: Create `2.5-sparse-vs-dense.mdx`. This lesson will discuss the trade-offs between different reward structures.

### Phase 2: Verification & Review

-   **Verification**:
    -   Run all Pytest tests to ensure the new reward function tests pass.
    -   Run the Docusaurus frontend (`npm run start`) and visually inspect all five new lesson pages to ensure they render correctly, code snippets are readable, and navigation works.
    -   Manually verify that the code snippets from Lessons 2.2 and 2.3 can be integrated into the main `action_loop.py` from Chapter 1 and run as expected.
-   **Review**: The feature will be ready for a pull request and peer review upon completion of the verification steps.
