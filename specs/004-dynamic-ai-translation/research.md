# Research: Ollama OpenAI-Compatible API for Translation

**Date**: 2025-12-16
**Feature**: Dynamic AI-Powered Content Translation
**Author**: Gemini Agent

## 1. Research Goal

The primary goal of this research was to determine the exact JSON structure and API endpoint details required to perform a translation task using the local Ollama instance, which provides an OpenAI-compatible API. This is necessary to resolve the `[NEEDS CLARIFICATION]` marker in the implementation plan.

## 2. Findings

The web search confirmed that Ollama exposes an OpenAI-compatible endpoint at `/v1/chat/completions`. This allows us to use the same request format as the OpenAI Chat Completions API.

### Key Details:
-   **Endpoint**: `POST {OLLAMA_API_BASE_URL}/chat/completions`
    -   Resolved URL: `http://localhost:11434/v1/chat/completions`
-   **Headers**:
    -   `Content-Type: application/json`
    -   `Authorization: Bearer {API_KEY}` (The API key is `ollama` as per user confirmation)
-   **Request Body (JSON)**: The request body should follow the OpenAI `ChatCompletion` model.

### Sample Request Body for Translation:

```json
{
  "model": "llama3.1:8b",
  "messages": [
    {
      "role": "system",
      "content": "You are an expert translator. Translate the provided text from English to Urdu. Do not include any other explanatory text in your response, only the translated text."
    },
    {
      "role": "user",
      "content": "The quick brown fox jumps over the lazy dog."
    }
  ],
  "temperature": 0.7,
  "stream": false
}
```

### Key Decisions Based on Research:

-   **Model**: We will use the `llama3.1:8b` model name in the API request, as specified by the user.
-   **Prompting Strategy**: A `system` message will be used to instruct the model to act as a translator and to only return the translated text. The user's text will be passed in a `user` message.
-   **Streaming**: For this initial implementation, we will set `stream: false` to receive the full translation in a single response, which is simpler to handle.

## 3. Alternatives Considered

-   **Using Ollama's Native API**: Ollama also has a native API (e.g., `/api/generate`). We could have used this, but it has a different, non-standard request/response format.
-   **Decision**: We will use the OpenAI-compatible API (`/v1/chat/completions`) because it's a widely-adopted standard, allowing for potential future flexibility (e.g., swapping the backend to a different OpenAI-compatible service) and easier use with existing client libraries.

This research resolves the final unknown in the technical context of the implementation plan.