# Implementation Plan: RAG Pipeline and Student AI Tutor

**Branch**: `006-rag-pipeline-ai-tutor` | **Date**: 2025-12-19 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/006-rag-pipeline-ai-tutor/spec.md`

## Summary

This plan outlines the implementation of a RAG-based AI Student Tutor. The system will feature a Python backend using FastAPI, Qdrant, and the OpenAI Agents SDK to create a `TutorAgent`. The frontend will be a custom floating chat UI built with React/TypeScript within the existing Docusaurus application. The core functionality includes indexing textbook content for retrieval, providing context-aware chat responses, and allowing users to query highlighted text.

**Scale/Scope**: Index all MDX content in the `docs/` directory.

## Phase 0: Research & Refinement (Senior Architect Updates)

### RAG Indexing Strategy
- **Parser**: Use `langchain-text-splitters` (or equivalent logic) with `MarkdownHeaderTextSplitter`.
- **Chunking**: 
    - First, split by H1/H2 headers to preserve structural context.
    - Second, chunk the text into ~500-800 character blocks with 10% overlap using `RecursiveCharacterTextSplitter`.
- **Metadata**: Each chunk MUST carry `chapter`, `lesson`, `heading_path`, and `file_path`.

### Vector Store (Qdrant)
- **Collection Setup**: Name: `textbook_content`. 
- **Vectors**: Size `768` (for Gemini `text-embedding-004`), Distance: `Cosine`.
- **Payload Indexing**: Create payload indexes on `chapter` and `lesson` to support fast metadata pre-filtering.

### Agent Logic (OpenAI Agents SDK)
- **TutorAgent**: Define instructions that enforce "Grounding." 
    - *Constraint*: "Only answer based on the retrieved context. If information is missing, admit it and suggest related textbook sections."
- **Retrieval Tool**: A dedicated tool for the agent to query Qdrant. It should support an optional `filter` for the current chapter to improve accuracy.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **[PASS]** VI. AI-Native Pedagogy: The feature directly supports agent-based augmentation.
- **[PASS]** V. Modularity for RAG: The plan depends on the consistent structure of the content for chunking.
- **[PASS]** I. Academic Accuracy and Verification: The RAG system will cite sources, upholding this principle.
- **[NEEDS REVIEW]** Content and Technical Standards: The user's request specifies `gemini/text-embedding-004`. The constitution doesn't specify an embedding model. This choice needs to be documented.

## Project Structure

### Documentation (this feature)

```text
specs/006-rag-pipeline-ai-tutor/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
backend/
├── app/
│   ├── agents/
│   │   └── tutor_agent.py
│   ├── core/
│   │   └──- config.py
│   ├── routers/
│   │   └── chat.py
│   └── services/
│       ├── indexing_service.py
│       └── retrieval_service.py
└── tests/
    ├── test_chat.py
    └── test_indexing.py

frontend/
├── src/
│   ├── components/
│   │   └── Chat/
│   │       ├── index.tsx
│   │       ├── ChatUI.tsx
│   │       └── styles.module.css
│   └── theme/
│       └── Root.tsx
└── tests/
    └── [NEEDS CLARIFICATION: Frontend testing setup]
```

**Structure Decision**: The feature is split between the existing `frontend` (Docusaurus) and `backend` (Python) directories. New components and services will be added to implement the chat UI, backend API, and RAG pipeline.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| SSE Streaming | UX requirement for live feeling | Long-polling or simple JSON is too slow for LLM response times. |
| Metadata Filtering | Accuracy requirement (Grounding) | Simple vector search often pulls irrelevant info from other chapters. |
| MDX Parsing | Content structure Preservation | Raw text extraction loses the H1/H2 hierarchy vital for citations. |