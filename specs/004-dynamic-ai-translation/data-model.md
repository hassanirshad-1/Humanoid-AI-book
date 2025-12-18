# Data Models: Dynamic AI-Powered Content Translation

**Feature**: Dynamic AI-Powered Content Translation
**Version**: 1.0

This document defines the data models used by the backend translation service. These models are implemented using Pydantic for data validation and serialization in the FastAPI application.

## 1. `TranslationRequest`

Represents the data sent from the frontend to the `/api/translate` endpoint.

-   **Description**: A request to translate a piece of text into a target language.
-   **Fields**:
    -   `text` (string, required): The source text to be translated.
        -   *Validation*: Must be a non-empty string.
    -   `target_language` (string, required): The language to translate the text into.
        -   *Validation*: Must be a non-empty string (e.g., "Urdu"). In a future version, this could be an Enum of supported languages.

### Example JSON:
```json
{
  "text": "The quick brown fox jumps over the lazy dog.",
  "target_language": "Urdu"
}
```

## 2. `TranslationResponse`

Represents the data sent from the `/api/translate` endpoint back to the frontend.

-   **Description**: The result of a translation request.
-   **Fields**:
    -   `translated_text` (string, required): The resulting translated text.
    -   `source_language` (string, optional): The detected source language. This is an optional field that may be added in the future.

### Example JSON:
```json
{
  "translated_text": "تیز بھوری لومڑی سست کتے پر چھلانگ لگاتی ہے۔"
}
```

## 3. Internal Models

These models are used internally within the backend service and are not exposed in the API.

### `OllamaChatRequest`

Represents the request sent to the Ollama `/v1/chat/completions` endpoint.

-   **Fields**:
    -   `model` (string)
    -   `messages` (List[Dict[str, str]])
    -   `temperature` (float)
    -   `stream` (bool)

### `OllamaChatResponse`

Represents the expected response from the Ollama `/v1/chat/completions` endpoint.

-   **Fields**:
    -   `choices` (List[Dict[str, Any]])
    -   ... and other fields as per the OpenAI standard.

