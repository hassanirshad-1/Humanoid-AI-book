# GEMINI.md - Master Reference for the AI-Native Textbook Project

## Agent Identity

**Role**: Educational System Architect

As the lead architect for this project, my purpose is to guide the development of a robust, scalable, and pedagogically sound AI-native educational platform. I specialize in integrating AI systems, content delivery pipelines, and interactive learning experiences. I will ensure all development aligns with the project's constitution and architectural principles.

---

## 1. Project Overview

This project is creating an AI-native textbook on Physical AI & Humanoid Robotics, delivered through a Docusaurus frontend and powered by a Python backend. The system includes a RAG chatbot, personalization features, multilingual translation, and autonomous agents to provide an interactive and adaptive learning experience. The backend manages all AI logic, data processing, and agent orchestration, while the frontend is responsible for rendering the textbook content and user interface.

## 2. Technology Stack

- **Frontend**: Docusaurus, TypeScript, React, MDX
- **Backend**: Python 3.12+, FastAPI, Uvicorn (`uv`)
- **AI Agents**: OpenAI Agents SDK
- **RAG Engine**: Qdrant (Vector Database)
- **Metadata Database**: Neon (Serverless Postgres)
- **Authentication**: Better-Auth
- **Development Workflow**: SpecKit Plus, Gemini CLI (Antigravity)

## 3. Directory Structure

```
.
├── .specify/              # SpecKit Plus configuration and templates
│   ├── memory/
│   │   └── constitution.md
│   ├── scripts/
│   └── templates/
├── history/                # SpecKit Plus generated history
│   └── prompts/            # Prompt History Records (PHRs)
│       └── constitution/
├── GEMINI.md               # This master reference file
```

## 4. Coding Conventions
(Refer to the project constitution at `.specify/memory/constitution.md` for detailed coding standards, including Python backend, TypeScript frontend, and MDX content conventions. `constitution.md` is the source of truth for coding standards.)

## 5. Versioning & Release Strategy

- **Semantic Versioning**:
  - `0.x.x`: Active development, potentially breaking changes.
  - `1.0.0+`: Stable releases.
- **Content Chapter Tags (Optional)**:
  - `chapter-1-draft`
  - `chapter-1-stable`

## 6. Contribution Guidelines

### Humans
- Follow MDX content structure and layout conventions for textbook content.
- Pull Requests (PRs) must pass all formatting and linting checks.

### Agents
- Must update `GEMINI.md` when making structural changes to the project.
- Must strictly follow specifications before writing code.
- Must update router memory (if relevant to the task).
- Must not create folders without updating project documentation.
- Must summarize their intent clearly in Pull Request descriptions.

## 7. Definition of Done (for Specifications)

A specification is considered "Done" when:
- Its scope, constraints, and acceptance criteria are clearly defined.
- It references or creates Architecture Decision Records (ADRs) if architecturally significant decisions are made.
- It enables the production of code or content that aligns perfectly with the specified requirements.
- No ambiguity remains regarding its implementation.
- It receives approval from the designated reviewer (human or agent).
- `GEMINI.md` and other relevant documentation are updated if structural changes are introduced.

## 8. Key Commands

### SpecKit Plus
- `/sp.constitution`: View or amend the project constitution.
- `/sp.specify <feature>`: Create a feature specification.
- `/sp.plan <feature>`: Create an implementation plan.
- `/sp.tasks <feature>`: Generate tasks from a plan.
- `/sp.adr <title>`: Create an Architecture Decision Record.
- `/sp.phr`: Create a Prompt History Record.

### Backend (Python, uv)
- Initialize project: `uv init backend`
- Add package: `uv add <package>`
- Remove package: `uv remove <package>`
- Run backend: `uv run <command>`
- Sync environment: `uv sync`

### Frontend (Docusaurus)
(Docusaurus is already installed)
- `npm install`: Install dependencies.
- `npm run start`: Start the development server.
- `npm run build`: Build the static site.

## 9. Important Notes & Gotchas

- **AI Logic Isolation**: ALL AI and business logic MUST reside in the Python backend. The frontend is strictly for presentation.
- **RAG Consistency**: MDX heading structure and style MUST remain consistent across all documents to ensure reliable RAG embedding and retrieval.
- **Vector Model Alignment**: Ensure the embedding model used for Qdrant is consistent across all services.
- **Secrets Management**: All secrets (API keys, database URLs) MUST be managed via a `.env` file and never committed to source control.
- **Master Reference**: This `GEMINI.md` file is the master reference. It MUST be updated as the project evolves.

## Roadmap / Future Work

- Create backend folder and initialize uv project
- Set up RAG pipeline (Qdrant integration)
- Integrate Neon (Serverless Postgres) for metadata database
- Implement Better-Auth for authentication
- Define autonomous AI agents (`agents/` folder)
- Develop Docusaurus MDX textbook content (`docs/` folder)
- Expand frontend application (`frontend/` folder)
- Establish Architecture Decision Records (`history/adr/` folder)
- Create helper and automation scripts (`scripts/` folder)
- Create `.env.example` file

