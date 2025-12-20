# Quickstart: RAG Pipeline and Student AI Tutor

This guide provides the steps to set up and run the AI Tutor feature.

## Backend Setup

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Install dependencies**:
    Make sure you have `uv` installed.
    ```bash
    uv sync
    ```
    You will need to add the following dependencies for this feature:
    ```bash
    uv add fastapi uvicorn qdrant-client openai
    ```

3.  **Configure environment variables**:
    Create a `.env` file in the `backend` directory and add the following:
    ```
    QDRANT_URL="http://localhost:6333"
    GEMINI_API_KEY="your_gemini_api_key"
    ```

4.  **Run the indexing service**:
    A script will be created to index the content.
    ```bash
    uv run python -m app.services.indexing_service
    ```

5.  **Run the backend server**:
    ```bash
    uv run uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

## Frontend Setup

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Run the frontend development server**:
    ```bash
    npm run start
    ```
    The Docusaurus website will be available at `http://localhost:3000`. The chat component will be visible on all lesson pages.

## Running the full application

1.  Make sure you have both the backend and frontend servers running.
2.  Open your browser and navigate to `http://localhost:3000`.
3.  Navigate to any of the textbook pages.
4.  The floating chat window should be visible.
5.  Try asking a question or highlighting some text to interact with the AI Tutor.
