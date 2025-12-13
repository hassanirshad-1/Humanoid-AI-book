# Tasks: Introduction to Robotics & Physical AI

**Input**: Design documents from `/specs/001-intro-robotics/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This feature uses a TDD approach for runnable code snippets.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `frontend/` for Docusaurus, Python code in `frontend/docs/chapter-01-intro/code/`, tests in root `tests/`
- Paths shown below adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create the directory `frontend/docs/chapter-01-intro/code/`
- [x] T002 Create the directory `frontend/docs/chapter-01-intro/include/assets/`
- [x] T003 Initialize Docusaurus project in `frontend/` directory with classic template and TypeScript (`npx create-docusaurus@latest frontend --template classic --typescript`)
- [x] T004 Move existing content from root `docs/chapter-01-intro` to `frontend/docs/chapter-01-intro`
- [x] T005 Remove the original empty `docs/` directory
- [x] T006 Correct image path in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx` (change `.gif` to `.png`)
- [x] T007 Update `frontend/docusaurus.config.ts` with project details, routing, navbar, and footer links
- [x] T008 Update `frontend/sidebars.ts` with manual sidebar for Chapter 1
- [x] T009 Fix `frontend/docusaurus.config.ts` syntax error (if any from previous attempts)
- [x] T010 Install `black` and `flake8` using `uv add black flake8`
- [x] T011 Configure `flake8` to ignore `E501` by creating a `.flake8` file
- [x] T012 Format Python code with `black` in `frontend/docs/chapter-01-intro/code/` and `tests/`
- [x] T013 Lint Python code with `flake8` in `frontend/docs/chapter-01-intro/code/` and `tests/`
- [x] T014 Install `pytest` and `pytest-xdist` using `uv add pytest pytest-xdist`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

---

## Phase 3: User Story 1 - Lesson 1.1: Philosophy (Priority: P1) 🎯 MVP

**Goal**: A student wants to understand the shift from "Classical Robotics" to "Physical AI" so they know why learning modern methods matters.

**Independent Test**: Student can explain the difference between a scripted policy and a learned policy.

### Implementation for User Story 1

- [x] T015 [US1] Create the file `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`.
- [x] T016 [US1] Write "The Concrete Hook" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`.
- [x] T017 [US1] Write "The Core Intuition" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`.
- [x] T018 [US1] Write "The Analogy" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`, explaining the shift from classical to physical AI with a relatable analogy.
- [x] T019 [US1] Write "The Formalism" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`.
- [x] T020 [US1] Write "Code Representation" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`, showing conceptual Python for policy `π(a|s)`.
- [x] T021 [US1] Write "Gotchas / Key Insights" section in `frontend/docs/chapter-01-intro/1.1-philosophy.mdx`, highlighting challenges in real-world policy application.
- [x] T022 [P] [US1] Create a placeholder image `frontend/docs/chapter-01-intro/include/assets/falling_robot_compilation.png`.

---

## Phase 4: User Story 2 - Lesson 1.2: The Hardware (Priority: P1)

**Goal**: A student needs to know the anatomy of the "Hero Robot" (Unitree G1) to understand what they are controlling.

**Independent Test**: Student can label the joint motors on a G1 diagram.

### Implementation for User Story 2

- [x] T023 [US2] Create the file `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`.
- [x] T024 [US2] Write "The Concrete Hook" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`.
- [x] T025 [US2] Write "The Core Intuition" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`.
- [x] T026 [US2] Write "The Analogy" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`, relating robot anatomy to human body parts.
- [x] T027 [US2] Write "The Formalism" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`.
- [x] T028 [US2] Write "Code Representation" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`, showing conceptual Python for state/action vectors.
- [x] T029 [US2] Write "Gotchas / Key Insights" section in `frontend/docs/chapter-01-intro/1.2-hardware-anatomy.mdx`, discussing motor limits or sensor noise.
- [x] T030 [P] [US2] Create a placeholder image `frontend/docs/chapter-01-intro/include/assets/unitree_g1_diagram.png`.

---

## Phase 5: User Story 3 - Lesson 1.3: The "Matrix" (Simulation) (Priority: P1)

**Goal**: A student wants to run their first simulation in MuJoCo to verify their environment is ready.

**Independent Test**: Student successfully executes `python load_sim.py` and sees a robot.

### Implementation for User Story 3

- [x] T031 [US3] Create the file `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`.
- [x] T032 [US3] Write "The Concrete Hook" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`.
- [x] T033 [US3] Write "The Core Intuition" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`.
- [x] T034 [US3] Write "The Analogy" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`, comparing simulation to video games for scientific accuracy.
- [x] T035 [US3] Write "The Formalism" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`.
- [x] T036 [US3] Write "Code Representation" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`, providing the basic MuJoCo setup code.
- [x] T037 [US3] Write "Gotchas / Key Insights" section in `frontend/docs/chapter-01-intro/1.3-simulation-setup.mdx`, regarding simulation vs. reality gaps.
- [x] T038 [P] [US3] Implement the script `frontend/docs/chapter-01-intro/code/lesson_1_3_hello_mujoco.py` to load and visualize the Unitree G1 model.
- [x] T039 [P] [US3] Create a test `tests/test_lesson_1_3.py` to verify that `lesson_1_3_hello_mujoco.py` runs without errors.

---

## Phase 6: User Story 4 - Lesson 1.4: First Policy (Priority: P2)

**Goal**: A student wants to send a command to the robot and see it move (even if it falls).

**Independent Test**: Student writes a loop sending random actions to the robot.

### Implementation for User Story 4

- [x] T040 [US4] Create the file `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`.
- [x] T041 [US4] Write "The Concrete Hook" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`.
- [x] T042 [US4] Write "The Core Intuition" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`.
- [x] T043 [US4] Write "The Analogy" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`, comparing the action loop to human reflexes.
- [x] T044 [US4] Write "The Formalism" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`.
- [x] T045 [US4] Write "Code Representation" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`, providing the basic action loop code.
- [x] T046 [US4] Write "Gotchas / Key Insights" section in `frontend/docs/chapter-01-intro/1.4-first-policy.mdx`, discussing the limitations of random policies.
- [x] T047 [P] [US4] Implement the script `frontend/docs/chapter-01-intro/code/lesson_1_4_action_loop.py` that sends random actions to the robot's joints.
- [x] T048 [P] [US4] Create a test `tests/test_lesson_1_4.py` to verify that `lesson_1_4_action_loop.py` runs without errors.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T049 Review all `.mdx` files for grammar, clarity, and adherence to the "Expanded Concrete Sandwich" rule.
- [x] T050 [P] Verify all citations are correctly formatted in APA style.
- [x] T051 [P] Replace placeholder assets in `frontend/docs/chapter-01-intro/include/assets/` with final versions.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **US3 (Simulation)** depends on **US1 (Philosophy)** for context but can be worked on in parallel.
- **US4 (First Policy)** depends on **US3 (Simulation)**.

### Within Each User Story

- Content tasks within each lesson can generally be done in any order, but it's recommended to follow the pedagogical structure (Hook -> Intuition -> Analogy -> Formalism -> Code -> Gotchas).
- Implementation tasks (Python scripts, tests) should ideally follow a TDD approach (write tests that fail, then implement code to make them pass).

### Parallel Opportunities

- All Setup tasks marked [x] are completed.
- Content writing tasks for different lessons can be parallelized.
- Asset creation (T022, T030) can be parallelized.
- Script implementation and testing (e.g., T038-T039, T047-T048) can be parallelized with content writing.
- Tasks marked with **[P]** can be parallelized.

---

## Implementation Strategy

### MVP First (User Stories 1, 2, and 3 Only)

1. Complete Phase 1: Setup (ALREADY COMPLETED)
2. Complete Phase 2: Foundational (ALREADY COMPLETED)
3. Complete remaining content tasks for User Stories 1, 2, and 3.
4. **STOP and VALIDATE**: Ensure all content for the first three lessons is complete and flows well.
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready (ALREADY COMPLETED)
2. Add User Story 1 expanded content → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 expanded content → Test independently → Deploy/Demo
4. Add User Story 3 expanded content → Test independently → Deploy/Demo
5. Add User Story 4 expanded content → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (ALREADY COMPLETED)
2. Once Foundational is done:
   - Developer A: User Story 1 content expansion
   - Developer B: User Story 2 content expansion
   - Developer C: User Story 3 content expansion
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence