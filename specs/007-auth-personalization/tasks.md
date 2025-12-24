# Tasks: User Authentication and Personalization (Refined)

**Input**: Design documents from `specs/007-auth-personalization/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization for the new Node.js authentication service and setup for the Python backend.

- [x] T001 Create a new directory for the auth service at `auth-backend/`.
- [x] T002 [P] In `auth-backend/`, initialize a Node.js project with `npm init -y`.
- [x] T003 [P] In `auth-backend/`, install core dependencies: `better-auth`, `typescript`, `ts-node`, `@types/node`, and a `better-auth` database adapter for Neon DB (e.g., Prisma).
- [x] T004 [P] In `auth-backend/`, create a `tsconfig.json` for the TypeScript project.
- [x] T005 [P] In the root `backend/`, install Python dependencies with `uv add asyncpg sqlmodel`.
- [x] T006 [P] In the `frontend/`, install `axios` with `npm install axios`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**Auth Service (Node.js)**
- [x] T007 In `auth-backend/`, create a main server file (e.g., `src/server.ts`) to configure and run the Better-Auth server.
- [x] T008 In `auth-backend/`, configure the Better-Auth database adapter to connect to the Neon DB. Connection string should be managed via environment variables.
- [x] T009 In `auth-backend/`, define the User schema for Better-Auth, including the `skill_level` and `operating_system` fields.
- [x] T010 Run the Better-Auth database migration command to create the `User` and `Session` tables in the Neon DB.

**API Service (Python)**
- [x] T011 [P] In `backend/app/`, create data models in `models.py` for `User` and `Session` to allow read-only access to the tables created by Better-Auth. These will be used for session validation.
- [x] T012 [P] In `backend/app/`, create a new `security.py` file to house the session validation logic.
- [x] T013 In `backend/app/security.py`, implement the `validate_session` dependency which reads the `Authorization` header and queries the database to verify the session token.

**Frontend**
- [x] T014 [P] In `frontend/src/services/`, create an `api.js` file to configure an `axios` instance for the Python backend.
- [x] T015 In `frontend/src/services/api.js`, implement the request interceptor to add the `Authorization` header to all requests.
- [x] T016 [P] In `frontend/src/lib/`, create an `authClient.ts` file to initialize the Better-Auth client, pointing to the Node.js auth service.

---

## Phase 3: User Story 1 - Securely Access Personalized Content (Priority: P1) 🎯 MVP

**Goal**: A user can log in and view personalized content based on their profile.

**Independent Test**: Log in using the frontend UI. Navigate to a page that fetches data from the Python backend. Verify the data is returned successfully and is appropriate for the user's profile settings.

### Implementation for User Story 1

- [x] T017 [P] [US1] In `frontend/src/pages/`, create login and registration pages (e.g., `login.js`, `register.js`).
- [x] T018 [US1] In the frontend login/registration pages, integrate the Better-Auth client to handle user sign-up and sign-in.
- [x] T019 [P] [US1] In the frontend, create a component to display the user's session status using the `useSession` hook from Better-Auth.
- [x] T020 [P] [US1] In `backend/app/routers/`, create a new `users.py` file for user-related endpoints.
- [x] T021 [US1] In `backend/app/routers/users.py`, implement the `GET /users/me` endpoint.
- [x] T022 [US1] In the `GET /users/me` endpoint, use the `validate_session` dependency to secure the endpoint and get the current `user_id`.
- [x] T023 [US1] In the `GET /users/me` endpoint, query the database for the user's profile data (`skill_level`, `operating_system`) and return it.
- [x] T024 [US1] In the frontend, create a component (e.g., `ProfileDisplay.js`) that calls the `GET /users/me` endpoint using the `axios` service and displays the user's personalization settings.

---

## Phase 4: User Story 2 - Manage Personalization Settings (Priority: P2)

**Goal**: A logged-in user can update their personalization settings.

**Independent Test**: Navigate to the profile management page, change the skill level, save, and then refresh the page or view personalized content to verify the change has taken effect.

### Implementation for User Story 2

- [x] T025 [P] [US2] In `backend/app/routers/users.py`, implement the `PATCH /users/me` endpoint.
- [x] T026 [US2] In the `PATCH /users/me` endpoint, use the `validate_session` dependency to secure the endpoint.
- [x] T027 [US2] In the `PATCH /users/me` endpoint, accept the new `skill_level` and/or `operating_system` in the request body and update the user's record in the database.
- [x] T028 [US2] In the `PATCH /users/me` endpoint, return the updated user profile.
- [x] T029 [P] [US2] In the frontend, create a profile management page/component (`ProfileEdit.js`).
- [x] T030 [US2] In `ProfileEdit.js`, create a form that allows users to change their `skill_level` and `operating_system`.
- [x] T031 [US2] On form submission in `ProfileEdit.js`, call the `PATCH /users/me` endpoint with the updated data.

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T032 [P] Add comprehensive error handling to all new frontend components.
- [x] T033 [P] Add logging to the Node.js auth service.
- [x] T034 [P] Add logging to the Python API service's new endpoints and validation logic.
- [x] T035 [P] Update the project's main `README.md` to document the dual-backend setup and how to run both services.
- [x] T036 Validate the entire authentication and personalization flow as described in the `quickstart.md`.
