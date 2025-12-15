# ADR 003: Introduction of "Chapter 0" for Beginner Accessibility

## Context
The current textbook (Chapter 1 onwards) assumes a certain level of technical fluency—specifically with Python, terminal commands, and basic math notation (MDPs). While the content is structured progressively, completely new beginners might find the initial jump into robotics philosophy and Simulation setup overwhelming without a proper "warm-up."

## Decision
We will introduce a new **Chapter 0: Welcome & Prerequisites** to serve as an on-ramp for absolute beginners.

This chapter will cover:
1.  **Welcome**: Setting the stage, defining the goal ("Becoming a Robot Engineer"), and building confidence.
2.  **Prerequisites**: A crash course in the essential tools required for the book:
    *   Python installation and basics.
    *   Command Line Interface (CLI) basics.
    *   Code editor setup (VS Code).
    *   Mental preparation for the math/physics to come.

## Consequences

### Positive
*   **Lower Entry Barrier**: Users with zero coding experience can start the book.
*   **Better Retention**: Reduces early drop-off caused by environment setup frustration.
*   **Separation of Concerns**: Chapter 1 can remain focused on Robotics/AI concepts without getting bogged down in "how to install Python" tutorials.

### Negative
*   **Maintenance**: Pre-requisite guides (installing Python, VS Code) can go out of date faster than conceptual content. We will need to keep these generic and standard-compliant.

## Status
Accepted
