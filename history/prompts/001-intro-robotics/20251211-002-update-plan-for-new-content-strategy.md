---
id: 002
title: Update Plan for New Content Strategy
stage: plan
date: 2025-12-11
surface: CLI
model: gemini
feature: 001-intro-robotics
branch: 001-intro-robotics
user: hassan
command: /sp.plan
labels: [plan, strategy, content]
links:
  spec: specs/001-intro-robotics/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-intro-robotics/plan.md
  - specs/001-intro-robotics/data-model.md
  - GEMINI.md
tests:
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType gemini`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

/sp.plan 001-intro-robotics plz update the plan to our new strategy

## Response snapshot

✅ /sp.plan command complete.

The implementation plan has been updated to reflect the new content strategy.

Branch: 001-intro-robotics
Plan Path: C:\Users\DELL\Documents\projects\Robotics_book\specs\001-intro-robotics\plan.md

Generated/Updated Artifacts:
- specs/001-intro-robotics/plan.md (Updated)
- specs/001-intro-robotics/data-model.md (Created)
- GEMINI.md (Updated by script)

## Outcome

- ✅ Impact: The implementation plan was successfully updated to incorporate the new "Expanded Concrete Sandwich" pedagogical strategy. A data model for content entities was created, and the agent's context was updated.
- 🧪 Tests: No tests were run for this command.
- 📁 Files: `plan.md` was updated, `data-model.md` was created, `GEMINI.md` was updated.
- 🔁 Next prompts: The user should now run `/sp.tasks` to generate the new tasks based on the updated plan.
- 🧠 Reflection: The process of manually creating ADRs and PHRs because the scripts were missing was a good adaptation. The `/sp.plan` command is effective but relies on the existence of specific scripts which should be verified.

## Evaluation notes (flywheel)

- Failure modes observed: The `update-agent-context.ps1` script failed initially because it required a `-FeatureName` parameter, which was not explicitly mentioned in the prompt.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure all scripts in the `.specify` workflow gracefully handle missing feature names or default to a sensible option.
