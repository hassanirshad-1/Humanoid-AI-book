# ADR-005: Backend API Stack for Dynamic Features

- **Status:** Proposed
- **Date:** 2025-12-16
- **Feature:** 004-dynamic-ai-translation
- **Context:** The project requires a backend service to power AI-native features, starting with dynamic content translation. The service must be performant, easy to develop and maintain, and provide a clear, modern interface for the Docusaurus frontend. Key requirements include handling asynchronous operations (like calling an LLM) and providing automatic API documentation to facilitate frontend integration.

## Decision

We will adopt the following stack for our Python backend services:
-   **Web Framework**: **FastAPI** for its high performance and modern Python features.
-   **ASGI Server**: **Uvicorn** as the standard, high-performance server for FastAPI.
-   **Architecture**: A modular, service-based architecture separating concerns into `routers` (API endpoints), `services` (business logic), and `models` (data structures using Pydantic).

## Consequences

### Positive

-   **High Performance**: FastAPI (built on Starlette and Pydantic) is one of the fastest Python frameworks available, suitable for I/O-bound operations like API calls.
-   **Automatic Interactive Docs**: FastAPI auto-generates OpenAPI-compliant documentation (Swagger UI), which is crucial for efficient frontend development and testing.
-   **Data Validation**: Pydantic enforces strict data validation for requests and responses, reducing bugs and improving API robustness.
-   **Developer Experience**: Modern Python type hints improve code clarity and editor support.

### Negative

-   **Async Complexity**: The `async`/`await` paradigm can introduce a learning curve for developers not yet comfortable with asynchronous programming.
-   **Less "Batteries-Included"**: Compared to Django, FastAPI is a micro-framework and requires developers to make more choices about libraries for tasks like ORM.

## Alternatives Considered

-   **Alternative: Flask**
    -   *Description*: A popular, lightweight, and highly flexible Python micro-framework.
    -   *Why Rejected*: While flexible, Flask does not offer built-in async support or automatic data validation and API documentation. Adding these features requires third-party libraries, resulting in more manual setup and a less integrated experience compared to FastAPI.

-   **Alternative: Django / Django Rest Framework (DRF)**
    -   *Description*: A full-featured, "batteries-included" framework ideal for large, monolithic applications.
    -   *Why Rejected*: Django is more heavyweight and opinionated than necessary for our microservice-oriented goals. Its primary strength is its integrated ORM, which is not a core requirement for our initial AI services. The setup is more complex for a simple API.

## References

- Implementation Plan: `specs/004-dynamic-ai-translation/plan.md`
- API Contract: `specs/004-dynamic-ai-translation/contracts/openapi.json`
