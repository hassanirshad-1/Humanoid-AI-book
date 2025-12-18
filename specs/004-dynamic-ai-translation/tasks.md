# Task List: Dynamic AI-Powered Content Translation

**Feature**: Dynamic AI-Powered Content Translation
**Branch**: `004-dynamic-ai-translation`
**User Stories**:
-   **US1**: Translate Entire Page to Urdu (P1)
-   **US2**: Translate Selected Text to Urdu (P2)

This plan is organized to deliver the backend API first (as a foundation for both stories), followed by the frontend implementation for each user story.

---

## Phase 1: Backend Setup & Dependencies

**Goal**: Prepare the backend development environment.

-   [x] T001 Add required Python dependencies to the backend project using `uv` in `backend/pyproject.toml`
    -   *Dependencies*: `fastapi`, `uvicorn`, `httpx`, `python-dotenv`

---

## Phase 2: Foundational Backend API (Supports US1 & US2)

**Goal**: Build the core FastAPI translation service that connects to the local LLM.
**Independent Test**: The `/api/translate` endpoint can be tested independently using the auto-generated docs at `http://127.0.0.1:8000/docs` or a tool like `curl`.

-   [x] T002 [P] Create Pydantic models for `TranslationRequest` and `TranslationResponse` in `backend/app/models.py`
-   [x] T003 [P] Create a configuration module to load `OLLAMA_API_BASE_URL` and `API_KEY` from `.env` in `backend/app/config.py`
-   [x] T004 Create a service module for the translation logic in `backend/app/services.py`
    -   *Details*: This service will contain the function that takes text, calls the Ollama API using `httpx`, and returns the translation. It will use the prompt format from `research.md`.
-   [x] T005 Create the API router for the `/api/translate` endpoint in `backend/app/routers/translation.py`
    -   *Details*: This router will use the models and service from the previous steps.
-   [x] T006 Update the main application file to include the translation router and configure CORS in `backend/main.py`

---

## Phase 3: Frontend - Page Translation (US1)

**Goal**: Implement the user interface for translating an entire page.
**Independent Test**: A user can click the "Translate" button on a content page and see the main text replaced with the Urdu translation, and then revert it.

-   [x] T007 [US1] Create a global state management context for translation (e.g., using React Context) to hold the current language and translation status in `frontend/src/context/TranslationContext.tsx`
-   [x] T008 [US1] Create a "Translate to Urdu" / "Show Original" button component in `frontend/src/components/TranslateButton/index.tsx`
-   [x] T009 [US1] Integrate the `TranslateButton` into the Docusaurus layout, making it visible on all content pages (e.g., in `frontend/src/theme/DocItem/Layout/index.tsx`)
-   [x] T010 [US1] Implement the client-side logic to fetch the translation from the `/api/translate` endpoint when the button is clicked.
-   [x] T011 [US1] Implement the logic to traverse the DOM and replace the text content of the main article with the translation, while preserving the original content in the translation context/state.

---

## Phase 4: Frontend - Selected Text Translation (US2)

**Goal**: Implement the UI for translating a snippet of selected text.
**Independent Test**: A user can highlight text, click a "Translate" button in a pop-up, and see the translation in that pop-up.

-   [x] T012 [P] [US2] Create a "Translate Selection" tooltip/popover component in `frontend/src/components/TextSelectionTooltip/index.tsx`
-   [x] T013 [US2] Add a global event listener to `frontend/src/theme/Root.tsx` to detect `mouseup` events and identify selected text.
-   [x] T014 [US2] Implement the logic to show/hide the `TextSelectionTooltip` component near the highlighted text.
-   [x] T015 [US2] When the translate button in the tooltip is clicked, call the `/api/translate` endpoint with the selected text and display the result within the tooltip.

---

## Dependencies & Execution Strategy

-   **Backend First**: Phases 1 and 2 **MUST** be completed first, as they provide the foundational API for both frontend user stories.
-   **MVP Scope (US1)**: The Minimum Viable Product is the completion of **Phases 1, 2, and 3**. This delivers the core page translation feature.
-   **Incremental Enhancement (US2)**: Phase 4 can be worked on after the backend is complete. The frontend work for US1 and US2 can be done in parallel by different developers if desired.

### Parallel Execution Examples:
-   **Within Phase 2**: `T002` (Models) and `T003` (Config) can be done in parallel.
-   **Across Phases (Post-Backend)**: Once Phase 2 is complete and the API contract is stable, a frontend developer can start on **Phase 3 (US1)** while another starts on **Phase 4 (US2)**. For example, `T007` (US1 Context) and `T012` (US2 Tooltip Component) can be developed concurrently.
