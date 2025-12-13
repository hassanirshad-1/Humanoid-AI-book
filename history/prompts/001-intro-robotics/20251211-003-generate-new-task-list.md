---
id: 003
title: Generate New Task List
stage: tasks
date: 2025-12-11
surface: CLI
model: gemini
feature: 001-intro-robotics
branch: 001-intro-robotics
user: hassan
command: /sp.tasks
labels: [tasks, content]
links:
  spec: specs/001-intro-robotics/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-intro-robotics/tasks.md
tests:
---

## Prompt

---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation:

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/[entity1].py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/[service].py (depends on T012, T013)`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

## Response snapshot

✅ /sp.tasks command complete.

The new task list for the '001-intro-robotics' feature has been generated and reflects the updated content strategy.
Path: C:\Users\DELL\Documents\projects\Robotics_book\specs\001-intro-robotics\tasks.md

Summary:
- Total tasks: 51
- Pending tasks: 13 (all related to expanding content sections and final review)

Pending tasks per User Story (new content sections):
  - US1 (Lesson 1.1 - Philosophy): 3 tasks (Analogy, Code Representation, Gotchas)
  - US2 (Lesson 1.2 - Hardware Anatomy): 3 tasks (Analogy, Code Representation, Gotchas)
  - US3 (Lesson 1.3 - The 'Matrix' Simulation): 3 tasks (Analogy, Code Representation, Gotchas)
  - US4 (Lesson 1.4 - First Policy): 3 tasks (Analogy, Code Representation, Gotchas)
  - Polish & Cross-Cutting Concerns: 1 task (Review all .mdx files)

Parallel opportunities identified: Yes, content writing for different lessons, and tasks marked [P].
Independent test criteria for each story: Clearly defined in tasks.md.
Suggested MVP scope: User Stories 1, 2, and 3 (to provide foundational knowledge and a working simulation environment).
Format validation: All tasks conform to the required checklist format.

## Outcome

- ✅ Impact: The task list was successfully regenerated to reflect the updated content strategy ("Expanded Concrete Sandwich") from the spec. It now includes explicit tasks for adding the new sections (Analogy, Code Representation, Gotchas) for each lesson.
- 🧪 Tests: No tests were run for this command.
- 📁 Files: `tasks.md` was overwritten with the new task list.
- 🔁 Next prompts: The user should now execute the implementation plan by working through the pending tasks in `tasks.md`.
- 🧠 Reflection: Successfully parsed and integrated information from `spec.md`, `plan.md`, and `data-model.md` to generate a comprehensive and properly formatted task list.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
