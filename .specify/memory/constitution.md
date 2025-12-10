<!--
Sync Impact Report

- Version change: 0.0.0 -> 1.0.0
- Description: Initial constitution established from user-provided principles.
- Added sections:
  - Core Principles
  - Content and Technical Standards
  - Interaction and Success Criteria
  - Governance
- Templates requiring updates:
  - .specify/templates/plan-template.md (⚠ pending)
  - .specify/templates/spec-template.md (⚠ pending)
  - .specify/templates/tasks-template.md (⚠ pending)
- Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics – AI-Native Textbook Constitution

## Core Principles

### I. Academic Accuracy and Verification
Content MUST be verified using recent (2023–2025) peer-reviewed research. All technical claims MUST be supported by verifiable primary sources.

### II. Robotics-First Correctness
There MUST be no hallucinated models, sensors, actuators, or robot capabilities. When referencing real robots, specifications MUST be verified from official sources.

### III. Clarity and Reproducibility
Content MUST be clear for upper-undergraduate and graduate-level CS/AI/Robotics students. Diagrams, algorithms, and pseudo-code MUST be replicable.

### IV. Neutral, Objective Technical Tone
The textbook MUST maintain a neutral, objective technical tone, free from speculation beyond current research unless clearly stated as future work.

### V. Modularity for RAG
All chapters MUST follow a consistent structure to be easily chunkable for RAG. Sentences MUST be short, clear, and non-ambiguous for embedding systems.

### VI. AI-Native Pedagogy
Each chapter MUST be optimized for personalization (e.g., beginner/intermediate/advanced toggles), multilingual translation, and agent-based augmentation.

### VII. Pedagogical Strategy ("The Concrete Sandwich")
To maximize engagement, content MUST follow this flow:
1.  **Concrete Hook**: Real-world relevance (why do we care?).
2.  **Intuition**: Visual/Mental model (no math yet).
3.  **Formalism**: The rigorous theory/math.
4.  **Code**: The implementation.
5.  **Simulation**: Verification in a virtual environment.

## Content and Technical Standards

### Standards
- **Citation Style**: IEEE or APA (to be chosen consistently per chapter).
- **Reference Quality**: Minimum 60% of references must be peer-reviewed papers or formal technical reports.
- **Reference Freshness**: Prefer latest research (2023–2025) from top-tier robotics conferences (ICRA, IROS, CoRL) and archives (arXiv Robotics).
- **Formatting**: Use clean Markdown with clear headings (H1–H4), lists, tables, and Mermaid diagrams. All code must be in fenced blocks.
- **Algorithms**: Include steps, complexity analysis, and assumptions.

### Content Constraints
- **No Speculation**: Avoid speculation beyond current research unless explicitly marked as future work.
- **No Hallucinated Citations**: All references must be real and verifiable.
- **Verifiable Claims**: No unverified claims about robot capabilities.
- **Concrete Descriptions**: Be specific about models, sensors, datasets, and architectures.
- **Chapter Length**: Chapters must be 1,500–2,500 words unless otherwise specified.

### Technical Constraints for AI-Native Book
- **RAG Optimization**: Every chapter must be easily chunkable.
- **Embedding-Friendly**: Sentences must be short, clear, and non-ambiguous.
- **Simple Structure**: Avoid excessive nested dependencies and prefer simple section headers for reliable RAG retrieval.

## Standard Chapter Structure
Every chapter MUST typically follow this outline:
1.  **The Hook (Real-World Problem)**: A concrete scenario where this concept fails or succeeds. (e.g., "Why did the robot fall?")
2.  **The Intuition (Mental Model)**: A high-level explanation without Greek letters.
3.  **The Mathematics (Formal Definition)**: Rigorous derivation (collapsible/blocked).
4.  **The Code (Implementation)**: Python/C++ code, runnable and clear.
5.  **The Simulation (Verification)**: How to run it in ROS/Gazebo.
6.  **The "Gotchas" (Industry Insight)**: Real-world edge cases.

## Engagement Rules
- **"The 3-Paragraph Rule"**: No more than 3 paragraphs of text without a visual, code block, or call-out diagram.
- **Visual-First**: Introduce concepts with a diagram before the equation.
- **Active Tone**: Use "We will build..." instead of "The chapter discusses...".

## Interaction and Success Criteria

### Interaction Constraints
- All output MUST follow this constitution unless overridden by a more specific spec.
- If a user request violates the constitution, respond with a corrected alternative that complies.

### Success Criteria
- **Verifiability**: All technical claims are supported by primary sources.
- **Zero Hallucinations**: No fabricated content regarding robot capabilities, models, or citations.
- **Readability**: Accessible to the target audience of undergraduate and graduate students.
- **RAG-Ready**: Directly embeddable into a RAG system without reformatting.
- **Translation-Friendly**: Written in a neutral academic tone suitable for translation (Urdu + English).
- **Personalization-Ready**: Structured to support beginner/intermediate/advanced content toggles.
- **Correctness**: Code examples must be logically correct or compile successfully.
- **Review**: Must pass academic fact-checking and internal consistency reviews.

## Governance

This constitution is the source of truth for all content generation. Amendments require review and approval to ensure they do not compromise the core principles. All work must verify compliance with this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-11-29
