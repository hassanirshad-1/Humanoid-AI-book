# ADR-007: Switching from Better-Auth to fastapi-users for Authentication

- **Status:** Accepted
- **Date:** 2025-12-20
- **Feature:** 007-auth-personalization
- **Context:** The project requires a robust authentication system for the Python/FastAPI backend. The initial specification designated `Better-Auth` for this purpose. However, research has confirmed that `Better-Auth` is a TypeScript/JavaScript-first framework with no direct, supported integration for Python. The only viable path would be to run it as a separate Node.js service, which would introduce significant architectural complexity, add a new language and runtime to the backend stack, and increase maintenance overhead. This approach conflicts with the goal of maintaining a streamlined and focused technology stack.

## Decision

We will use **`fastapi-users`** as the primary authentication library for the project.

- **Authentication Stack**:
    - **Framework Integration**: `fastapi-users`
    - **Password Hashing**: `passlib` with `bcrypt`
    - **Token Management**: `python-jose` for JWT generation and validation
    - **Database Adapter**: `fastapi-users-db-sqlalchemy` to connect with Neon (Postgres)

This stack is a mature, well-documented, and widely-used solution specifically designed for FastAPI, providing all required functionality including registration, login, password recovery, and secure session management.

## Consequences

### Positive

- **Simplified Architecture**: Avoids the need for a separate microservice for authentication, keeping the backend a single, cohesive Python application.
- **Improved Maintainability**: The backend stack remains unified (Python/FastAPI), reducing cognitive overhead and simplifying development and deployment.
- **Robust and Secure**: `fastapi-users` is a battle-tested library that enforces security best practices for authentication and password management.
- **Excellent Integration**: Natively integrates with FastAPI and SQLAlchemy, fitting perfectly into our existing technology stack.

### Negative

- **Deviation from Spec**: This decision deviates from the `spec.md` and `GEMINI.md`, which initially specified `Better-Auth`. These documents will need to be updated to reflect the change.

## Alternatives Considered

- **Alternative 1: `Better-Auth` as a separate microservice**
  - **Description**: Run `Better-Auth` in a dedicated Node.js container and have the FastAPI application communicate with it via internal API calls.
  - **Why Rejected**: This was rejected due to the significant increase in architectural complexity, the introduction of an entirely new backend language/runtime, and the associated development and operational overhead. It violates the principle of simplicity.

- **Alternative 2: Other Python libraries (e.g., `FastAPI-Auth`, custom implementation)**
  - **Description**: Use a different, less comprehensive Python library or build the authentication logic from scratch.
  - **Why Rejected**: `fastapi-users` is the most feature-complete and actively maintained authentication framework for FastAPI. Competing libraries offer fewer features, and a custom implementation would be time-consuming and more likely to contain security vulnerabilities.

## References

- **Feature Spec**: `specs/007-auth-personalization/spec.md`
- **Implementation Plan**: `specs/007-auth-personalization/plan.md`
- **Related ADRs**: None
- **Evaluator Evidence**: The research findings documented in `specs/007-auth-personalization/research.md`.
