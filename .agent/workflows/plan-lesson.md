---
description: Create a new textbook lesson using the Gold Standard structure
---

Input:
  chapter:
    type: string
    description: Chapter number (e.g., "01")
  lesson:
    type: string
    description: Lesson number (e.g., "1.5")
  title:
    type: string
    description: Title of the lesson
  description:
    type: string
    description: Brief description of what the lesson covers

Steps:
  1.  **Read Context**:
      - Read `c:\Users\DELL\Documents\projects\Robotics_book\.specify\memory\constitution.md` to understand the writing style and rules.
      - Read `c:\Users\DELL\Documents\projects\Robotics_book\.specify\templates\lesson-template.md` to get the structure.

  2.  **Generate Content**:
      - Use an LLM to generate the full lesson content in MDX format.
      - **Prompt**:
        > You are writing a lesson for the "Physical AI & Humanoid Robotics" textbook.
        > Target Audience: CS/Robotics students.
        > Tone: Engaging, "Concrete Sandwich" pedagogy.
        >
        > Task: Write **Lesson {{lesson}}: {{title}}**.
        > Description: {{description}}
        >
        > STRICTLY follow the structure in `lesson-template.md`.
        > STRICTLY follow the rules in `constitution.md` (especially Sim-to-Real and Knowledge Checks).
        >
        > output the full MDX content.

  3.  **Save File**:
      - Determine the filename: `{{lesson}}-{{title | slugify}}.mdx`
      - Save the content to `c:\Users\DELL\Documents\projects\Robotics_book\frontend\docs\chapter-{{chapter}}-xxxx/{{filename}}` (User will need to verify the exact path).
