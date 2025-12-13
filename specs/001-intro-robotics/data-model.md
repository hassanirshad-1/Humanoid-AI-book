# Data Model: Content Entities

This document defines the key entities used in the textbook content.

## Lesson

- **Description**: A `Lesson` is a distinct unit of learning, represented as a single `.mdx` file.
- **Fields**:
  - `title`: The main heading (H1) of the document.
  - `content`: The body of the lesson, structured according to the "Expanded Concrete Sandwich" model.
- **Relationships**:
  - A `Lesson` contains one or more `CodeSnippet` entities.
  - A `Lesson` can reference one or more `Asset` entities.

## Asset

- **Description**: An `Asset` is a non-textual piece of content used to support a lesson.
- **Types**:
  - Image (e.g., `.png`, `.jpg`)
  - GIF
  - Simulation Model (e.g., `.xml`, `.mjcf`)
- **Relationships**:
  - An `Asset` is referenced by one or more `Lesson` files.

## CodeSnippet

- **Description**: A `CodeSnippet` is a block of runnable or illustrative code.
- **Fields**:
  - `language`: The programming language of the snippet (e.g., Python, Bash).
  - `code`: The verbatim code content.
- **Validation**:
  - All Python `CodeSnippet` entities intended for execution MUST be tested and compatible with the project's Python version.
- **Relationships**:
  - A `CodeSnippet` is embedded within a `Lesson`.
