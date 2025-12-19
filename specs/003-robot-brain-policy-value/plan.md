# Implementation Plan: Chapter 3 - The Robot's Brain: Policies & Value Functions

## 1. Technical Context

This plan outlines the implementation for creating Chapter 3 of the AI-Native Textbook, "The Robot's Brain: Policies & Value Functions." This chapter acts as the bridge between reward signals (Chapter 2) and learning algorithms (Chapter 4), teaching *how* a robot decides to act and *how* it judges the long-term quality of those decisions.

-   **Files to Create**:
    -   `frontend/docs/chapter-03-policy-and-value/3.1-policy.mdx`
    -   `frontend/docs/chapter-03-policy-and-value/3.2-return.mdx`
    -   `frontend/docs/chapter-03-policy-and-value/3.3-value-function.mdx`
    -   `frontend/docs/chapter-03-policy-and-value/code/lesson_3_1_policy_comparison.py`
    -   `frontend/docs/chapter-03-policy-and-value/code/lesson_3_3_value_heatmap.py`
    -   `tests/test_lesson_3_1.py`

-   **Files to Modify**:
    -   `frontend/sidebars.ts`: To add the new Chapter 3 to the Docusaurus sidebar navigation.

-   **Technology Stack**:
    -   **Content**: Docusaurus, MDX, React (for LaTeX math)
    -   **Code**: Python 3.12+, Numpy, Matplotlib (for heatmaps)
    -   **Testing**: Pytest

-   **Dependencies**:
    -   Depends on `unitree_g1` context from Chapter 1.
    -   Depends on `remark-math` and `rehype-katex` plugins (already installed in Chapter 2).

## 2. Constitution Check & Gate Evaluation

-   **AI Logic Isolation**: Logic for policies and value calculation will be in Python scripts.
-   **RAG Consistency**: MDX headers will follow the "Gold Standard" (Hook, Intuition, Formalism, Code, Sim-to-Real).
-   **Secrets Management**: N/A.

**Gate Evaluation**:
-   Plan complies with project standards. **Proceed.**

## 3. Implementation Phases

### Phase 0: Scaffolding

-   **Task 0.1**: Create directory `frontend/docs/chapter-03-policy-and-value/code`.
-   **Task 0.2**: Update `frontend/sidebars.ts` to include the new chapter structure.

### Phase 1: Content & Code Implementation

-   **Task 1: Lesson 3.1 - The Policy**:
    -   Create `3.1-policy.mdx`.
    -   Create `code/lesson_3_1_policy_comparison.py`: A script comparing a random policy vs. a simple heuristic (e.g., "always move towards target").
    -   Create `tests/test_lesson_3_1.py` to verify the heuristic policy performs better than random.

-   **Task 2: Lesson 3.2 - The Return**:
    -   Create `3.2-return.mdx`.
    -   Focus on the math of Discount Factors ($\gamma$) and cumulative reward.
    -   Include interactive "Do the math" exercises in the text.

-   **Task 3: Lesson 3.3 - The Value Function**:
    -   Create `3.3-value-function.mdx`.
    -   Create `code/lesson_3_3_value_heatmap.py`: A visualization script using Matplotlib to show a "value heatmap" on a simple 2D grid (representing a simplified state space).

### Phase 2: Verification

-   **Verification Steps**:
    -   Run `pytest` for the new test.
    -   Run `npm run build` to ensure no new MDX/LaTeX errors are introduced.
    -   Verify visual rendering of the Matplotlib heatmap code block (ensure code is copy-pasteable).

## 4. Risks & Mitigations

-   **Risk**: LaTeX syntax errors in MDX (as seen in Ch 2).
    -   **Mitigation**: Run `npm run build` frequently during drafting.
-   **Risk**: Matplotlib dependency missing.
    -   **Mitigation**: Check `pyproject.toml` or `requirements.txt` (or just ensure code runs in standard data science envs).
