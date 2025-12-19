# Quickstart: Translation Backend Service

This guide explains how to run the FastAPI-based translation service locally.

## 1. Prerequisites

-   Python 3.12+
-   `uv` installed (`pip install uv`)
-   A running Ollama instance.
-   The required Ollama model pulled, e.g., `ollama pull llama3.1:8b`.

## 2. Setup

### Step 1: Install Dependencies

Navigate to the `backend` directory and install the Python dependencies.

```bash
cd backend
uv sync
```

### Step 2: Configure Environment

The backend service requires credentials to connect to the local Ollama instance. These are stored in a `.env` file in the `backend/` directory.

Ensure your `backend/.env` file contains the following, matching your local Ollama setup:

```env
OLLAMA_API_BASE_URL=http://localhost:11434/v1
API_KEY=ollama
```

## 3. Running the Service

Once the setup is complete, you can run the FastAPI server from within the `backend/` directory.

```bash
uv run uvicorn main:app --reload
```

-   `main`: Refers to the `main.py` file.
-   `app`: Refers to the `FastAPI` app instance inside `main.py`.
-   `--reload`: Enables hot-reloading for development, so the server restarts on code changes.

The service will be available at `http://127.0.0.1:8000`.

## 4. API Documentation

Once the server is running, interactive API documentation (provided by Swagger UI) will be automatically available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can use this interface to test the `/api/translate` endpoint directly from your browser.
