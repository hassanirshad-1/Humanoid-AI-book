# ADR-004: Code-Alongside-Content for Lesson Examples

- **Status:** Accepted
- **Date:** 2025-12-14
- **Feature:** 002-reward-signal
- **Context:** The project requires providing runnable Python code examples for lessons within the Docusaurus-based textbook. We need a consistent and easy-to-access location for these scripts.

## Decision

We will store Python example scripts directly within the `frontend/docs/` directory, adjacent to the `.mdx` lesson files that reference them. The structure will be `frontend/docs/<chapter-name>/code/<script_name>.py`.

## Consequences

### Positive

-   **Self-Contained Chapters**: Each chapter's content and related code are grouped together, making the project structure intuitive for contributors.
-   **Simplified Linking**: It is trivial to link to or embed code snippets from a lesson's corresponding `code` directory.
-   **Easy for Readers**: Learners can easily find the code associated with a lesson without navigating away from the documentation source.

### Negative

-   **Decentralized Code**: The Python code is not part of a single, installable Python package. This could make it slightly more complex to run tests against all lesson code at once.
-   **Potential for Duplication**: If a utility function or class is needed across multiple chapters, it might be duplicated, violating the DRY (Don't Repeat Yourself) principle.

## Alternatives Considered

1.  **A Central `lessons_code` Python Package**:
    -   **Description**: Create a formal Python package in the repository root where all lesson code would reside.
    -   **Why Rejected**: This would add complexity for the reader, requiring them to navigate to a completely different part of the repository to find the code. It also complicates the authoring process, as linking from MDX to a root-level directory is less straightforward. The primary goal is clarity for the learner, which the co-location approach serves better.

## References

- Feature Spec: [specs/002-reward-signal/spec.md](./../../specs/002-reward-signal/spec.md)
- Implementation Plan: [specs/002-reward-signal/plan.md](./../../specs/002-reward-signal/plan.md)
