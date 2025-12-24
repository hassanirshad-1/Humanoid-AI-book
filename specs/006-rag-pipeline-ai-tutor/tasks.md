# Task List: RAG Pipeline and Student AI Tutor

This file outlines the implementation tasks for the AI Tutor feature, organized by priority.

## Phase 1: Project Setup

- [X] T001 Create the backend directory structure in `backend/app/` as defined in `plan.md`.
- [X] T002 Create the frontend directory structure in `frontend/src/` as defined in `plan.md`.
- [X] T003 [P] Add required dependencies to the backend: `uv add fastapi uvicorn qdrant-client openai langchain-text-splitters`.
- [X] T004 [P] Add required dependencies to the frontend: `npm install --save-dev jest @testing-library/react`.
- [X] T005 Create a `.env.example` file in the `backend/` directory with `QDRANT_URL` and `GEMINI_API_KEY`.

## Phase 2: Foundational Backend & Indexing

- [X] T006 Implement the Qdrant collection setup logic in `backend/app/services/indexing_service.py` as per `plan.md`.
- [X] T007 Implement the MDX content parser and chunking logic in `backend/app/services/indexing_service.py`.
- [X] T008 Create the embedding generation logic using `gemini/text-embedding-004` in `backend/app/services/indexing_service.py`.
- [X] T009 Implement the main indexing pipeline that reads from `docs/`, processes, and uploads chunks to Qdrant in `backend/app/services/indexing_service.py`.
- [X] T010 Create a runnable script or CLI command to trigger the indexing process.

## Phase 3: User Story 1 - Ask a question in the chat (P1)

**Goal**: A user can ask a question in a floating chat window and receive a streamed, contextually relevant answer.

- [X] T011 [US1] Create the basic floating chat button and window component in `frontend/src/components/Chat/index.tsx`.
- [X] T012 [US1] Implement the main chat UI, including message display and input form, in `frontend/src/components/Chat/ChatUI.tsx`.
- [X] T013 [US1] Add the global chat provider to the Docusaurus root in `frontend/src/theme/Root.tsx` to make the chat available on all pages.
- [X] T014 [US1] Implement the backend retrieval tool for the `TutorAgent` in `backend/app/agents/tutor_agent.py`.
- [X] T015 [US1] Define the `TutorAgent` with its grounding-focused instructions in `backend/app/agents/tutor_agent.py`.
- [X] T016 [US1] Create the `POST /chat` endpoint in `backend/app/routers/chat.py` to handle chat messages.
- [X] T017 [US1] Implement the Server-Sent Events (SSE) streaming logic in the `/chat` endpoint.
- [X] T018 [US1] Connect the frontend chat UI to the `/chat` backend endpoint to send messages and receive streamed responses.

## Phase 4: User Story 2 - Highlight text to ask a question (P2)

**Goal**: A user can highlight text on the page to pre-fill the chat input and ask a question.

- [X] T019 [US2] Implement the logic to detect text selection on the page in `frontend/src/components/Chat/index.tsx`.
- [X] T020 [US2] Create the "Ask Tutor" pop-up button that appears on text selection.
- [X] T021 [US2] Implement the functionality to pass the highlighted text to the chat input when the "Ask Tutor" button is clicked.

## Phase 5: User Story 3 - Chat is aware of the current lesson (P3)

**Goal**: The AI Tutor's answers are more relevant because it knows which lesson the user is viewing.

- [X] T022 [US3] Implement logic in the frontend to track the user's current page URL and send it as context to the backend.
- [X] T023 [US3] Modify the backend retrieval tool in `backend/app/agents/tutor_agent.py` to use the `current_url` to pre-filter Qdrant search results by `chapter` or `lesson`.
- [X] T024 [US3] Update the `TutorAgent`'s prompt to leverage the improved contextual relevance.

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T025 Implement the glassmorphic theme for the chat UI in `frontend/src/components/Chat/styles.module.css`.
- [X] T026 [P] Ensure the chat UI is responsive and works well on mobile, tablet, and desktop screens.
- [X] T027 [P] Add error handling to the frontend for when the backend is unavailable or returns an error.
- [X] T028 Implement Markdown and LaTeX rendering in the chat UI.
- [X] T029 Implement clickable citations in the AI's responses that link back to the source in the textbook.
- [ ] T030 [Multilingual] Ensure the `TutorAgent` can understand and respond in Urdu, matching the user's current reading language.

## Dependencies

- **User Story 1** is the core MVP and has no dependencies on other stories.
- **User Story 2** depends on User Story 1 (the chat UI must exist).
- **User Story 3** depends on User Story 1 (the chat and backend must exist).

## Parallel Execution

- **Backend vs. Frontend**: Most backend (Phase 2, agent/router implementation) and frontend (UI components) tasks can be worked on in parallel.
- **Within Stories**:
  - In US1, `T011`-`T013` (frontend UI) can be parallelized with `T014`-`T017` (backend logic).
  - Polish tasks (`T025`-`T029`) can often be done in parallel with feature development.

## Implementation Strategy

The feature will be delivered incrementally, following the user story priorities.
1.  **MVP**: The initial delivery will focus on completing **User Story 1**, providing the core chat functionality.
2.  **Iteration 2**: Deliver **User Story 2**, the highlight-to-ask feature.
3.  **Iteration 3**: Deliver **User Story 3**, the context-aware filtering.
4.  **Polish**: The final polish tasks will be addressed throughout the process and before final release.
