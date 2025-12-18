---
id: 20251216-001
title: create-dynamic-ai-translation-spec
stage: spec
date: 2025-12-16
surface: cli
model: Gemini
feature: 004-dynamic-ai-translation
branch: 004-dynamic-ai-translation
user: Hassan
command: /sp.specify "Dynamic AI Translation Backend Service"
labels: []
links:
  spec: specs/004-dynamic-ai-translation/spec.md
  ticket:
  adr:
  pr:
files:
  - GEMINI.md
  - backend/.env
  - specs/004-dynamic-ai-translation/spec.md
  - specs/004-dynamic-ai-translation/checklists/requirements.md
tests:
---

## Prompt

The user's initial request that lead to the specification creation:
"ok so now lets make the specs first for this translation and remember we have to have a button of urder which will generate the urdu for that page and yes you are right some text can also be converted into urdu this is also a very good idea a very good feature"

Followed by the clarification and approval of the streamlined, local LLM based plan:
"Okay, this is a fantastic pivot, Hassan! Using a locally hosted LLM for the hackathon is a brilliant move. It massively simplifies our architecture, reduces external dependencies for the demo, and lets us focus on building the core features without worrying about backend deployment. I'm fully on board.

You are absolutely right. The backend doesn't need to be a production-grade deployed service; it just needs to work on our local machine to power the frontend during the presentation.

Let's refine the plan with this lean, local-first approach.

### The Focused Backend Plan: Local LLM Translation

We will focus on building **one thing** first: the backend service that powers the dynamic translation, but using your local Llama 3.1 8B model instead of a cloud API.

Here is the proposed final draft of the plan:

1.  **Project Scaffolding (in `backend/` directory):**
    *   Initialize a self-contained Python project using `uv` inside the `backend/` folder to keep dependencies isolated.
    *   Add the necessary packages: `fastapi`, `uvicorn` (for the server), and `httpx` (to make asynchronous requests to your local LLM).

2.  **API Structure:**
    *   Create a `routers` subdirectory within `backend` for clean organization (e.g., `backend/routers/`).
    *   Inside `routers`, create a `translation.py` file to handle all translation-related logic.

3.  **Implement the Translation Endpoint (`/api/translate`):**
    *   This endpoint will accept a JSON request from the frontend containing the `text` to be translated and the `target_language`.
    *   It will then construct a precise prompt for Llama 3.1 (e.g., *"Translate the following English text to Urdu: [text from frontend]"*).
    *   Using `httpx`, it will send this prompt in a POST request to your local Llama 3.1 API endpoint.
    *   Finally, it will parse the JSON response from the local LLM, extract the translated text, and send it back to our Docusaurus frontend.

This plan is focused, leverages your local setup perfectly, and gets us a key AI feature up and running quickly.

To make the specification perfect, I'll need to know the API endpoint for your local Llama 3.1 model. Is it running via Ollama, for instance, at an address like `http://localhost:11434/api/generate`?

Let me know if this final plan gets your approval. Once you confirm, I'll be ready for your `/sp.specify` command"

User's response for endpoint: "OLLAMA_API_BASE_URL=http://localhost:11434/v1
API_KEY=ollama these are the credentials brother and i have started the server and if it doesnt work thena ask me again and tell me if you need any other thing you can save these into and .env file"

## Response snapshot

Successfully processed the `/sp.specify` command after resolving issues with the `create-new-feature.ps1` script and clarifying user requirements.

- Created new Git branch: `004-dynamic-ai-translation`.
- Generated `specs/004-dynamic-ai-translation/spec.md` including detailed user scenarios, functional requirements, and success criteria.
- Generated `specs/004-dynamic-ai-translation/checklists/requirements.md` with quality validation items.
- Updated `GEMINI.md` to reflect new project features.
- Created `backend/.env` with local LLM credentials.
- All `[NEEDS CLARIFICATION]` markers in `spec.md` have been resolved based on user input and reasonable defaults.

## Outcome

- ✅ Impact: Specification for `Dynamic AI Translation` created, detailed, and approved. It now fully incorporates the local LLM approach and user-specific details.
- 🧪 Tests: No automated tests for spec creation.
- 📁 Files: `specs/004-dynamic-ai-translation/spec.md` and `specs/004-dynamic-ai-translation/checklists/requirements.md` created; `GEMINI.md` updated; `backend/.env` created.
- 🔁 Next prompts: Proceed to planning the implementation (`/sp.plan`).
- 🧠 Reflection: Successfully navigated a complex `sp.specify` command execution path including script debugging and iterative clarification. Highlighted the importance of robust tooling and clear argument parsing for internal scripts. Ensure local LLM endpoint is properly configured in implementation.
