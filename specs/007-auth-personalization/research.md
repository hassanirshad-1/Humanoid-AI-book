# Research: User Authentication and Personalization (Refined)

This document captures the research findings for the refined implementation of feature `007-auth-personalization`, focusing on a frontend-led authentication model with Better-Auth.

## 1. Better-Auth Frontend Integration & Architecture

**Question**: What is the standard way to integrate Better-Auth into a React (Docusaurus) application, and what is the overall architecture?

**Findings**:
- `better-auth` is a full-stack, client-server authentication framework. It is not just a frontend library.
- The standard architecture consists of:
    1.  A **`Better-Auth` server** running on a **Node.js environment**. This server handles all core logic: user registration, login, password hashing, social logins, and creating/managing sessions in the database.
    2.  A **`Better-Auth` client** (e.g., `better-auth/react`) integrated into the frontend application. This client provides hooks (`useSession`) and methods (`signIn`, `signOut`) to interact with the `Better-Auth` server.
- This means to use `better-auth` as requested, the project will require **two backend services**:
    1.  The existing **Python/FastAPI** application backend.
    2.  A new **Node.js** backend service dedicated to running the `Better-Auth` server.
- The frontend will primarily interact with the `Better-Auth` Node.js server for all authentication operations.

**Decision**:
- We will proceed with this dual-backend architecture.
- The frontend will be configured to communicate with a new Node.js `Better-Auth` service.
- The `better-auth-ui` library will be considered to accelerate frontend component development.
- Testing will involve mocking the `useSession` hook and the other client methods provided by `better-auth/react`. Libraries like Jest and React Testing Library are suitable for this.

## 2. Backend Session Validation Strategy

**Question**: How can a Python backend validate a session token created by a separate `Better-Auth` Node.js service?

**Findings**:
- The user's request specifies that the Python backend should validate the session by "checking the Neon DB session table."
- This is a viable, "decoupled" validation strategy. The process would be:
    1.  The `Better-Auth` Node.js server creates a session upon user login and stores the session details in a dedicated table in the Neon DB. The schema for this table is defined by `Better-Auth`'s database adapter (e.g., for Prisma or Drizzle). We will need to obtain this schema.
    2.  The React frontend receives a session token from the `Better-Auth` server.
    3.  For requests to the Python backend, the frontend must send this session token (e.g., in an `Authorization` header).
    4.  The Python backend receives the token, connects to the Neon DB, and executes a direct database query on the `Better-Auth` session table to check if the token exists, is valid, and has not expired.
- This approach avoids direct HTTP communication between the Python and Node.js backends for validation, relying instead on a shared database.

**Decision**:
- The Python backend will implement a dependency-injected service to handle session validation.
- This service will use SQLAlchemy (or a similar async DB driver like `asyncpg` directly) to connect to the Neon DB.
- It will query the session table created by `Better-Auth` to validate incoming session tokens.
- **Crucial Prerequisite**: We must obtain the exact schema of the `Better-Auth` session table to write the correct validation queries. This will be a primary task in the implementation phase.

## 3. Secure Token Handling between Frontend and Backend

**Question**: What is the secure method for passing the session token from the Better-Auth-powered frontend to the Python backend for validation?

**Findings**:
- The standard and secure method is to send the session token from the frontend to the backend in the `Authorization` header of every HTTP request.
- The header should be formatted as `Authorization: Bearer <session_token>`.
- The frontend client (`Better-Auth`'s client) will be responsible for storing the session token it receives from the `Better-Auth` server. It should then attach this token to all API calls made to the Python backend.
- **Frontend Implementation**:
    - Use an HTTP client like `axios`.
    - Create an `axios` interceptor that automatically retrieves the session token from wherever `Better-Auth`'s client stores it and adds the `Authorization` header to every outgoing request to the Python backend.
- **Backend Implementation**:
    - The Python/FastAPI backend will have a dependency that reads the `Authorization` header from incoming requests.
    - This dependency will extract the token and pass it to the session validation service.

**Decision**:
- The frontend will use an `axios` interceptor to automatically send the `Better-Auth` session token in the `Authorization: Bearer <token>` header for all requests to the Python backend.
- The Python backend will read this header to get the token for validation.