# ADR-006: Local LLM Integration via OpenAI-Compatible API

- **Status:** Proposed
- **Date:** 2025-12-16
- **Feature:** 004-dynamic-ai-translation
- **Context:** The dynamic translation feature requires the backend to communicate with a locally running Large Language Model (LLM) provided by Ollama. We need a stable, well-documented, and maintainable method for making these API calls from our Python backend. The chosen method should be robust and, if possible, align with industry standards to allow for future flexibility.

## Decision

We will integrate with the local Ollama instance by using its **OpenAI-compatible API endpoint** (`/v1/chat/completions`).

All communication with the LLM will be standardized through this interface, using a client like `httpx` to send requests that mimic the OpenAI Python client's structure.

## Consequences

### Positive

-   **Standardization**: By using an OpenAI-compatible API, we align with a widely adopted industry standard. This makes the integration logic easier for new developers to understand.
-   **Portability & Flexibility**: This decision decouples us from Ollama-specific implementation details. In the future, we could swap the local Ollama instance for any other OpenAI-compatible service (e.g., a cloud-hosted model, a different local provider) with minimal changes to our backend code (likely just changing the API base URL and key).
-   **Tooling Ecosystem**: We can leverage the vast ecosystem of tools and libraries built for the OpenAI API if needed in the future.

### Negative

-   **Abstraction Layer Risk**: We are dependent on Ollama's implementation and maintenance of this OpenAI-compatible wrapper. If there are bugs or limitations in this wrapper, it could affect our service.
-   **Missed Native Features**: We may not be able to access certain new or experimental features that are only available through Ollama's native API (`/api/generate`).

## Alternatives Considered

-   **Alternative: Use Ollama's Native API**
    -   *Description*: Ollama provides its own native endpoints, such as `/api/generate`, which have a different request/response structure.
    -   *Why Rejected*: This would tightly couple our backend service to Ollama's specific implementation. If we ever wanted to change the LLM provider, it would require a significant refactor of our service layer. The OpenAI-compatible API provides better long-term flexibility and adheres to a more common standard, as documented in our research.

## References

- Research Document: `specs/004-dynamic-ai-translation/research.md`
- Implementation Plan: `specs/004-dynamic-ai-translation/plan.md`
