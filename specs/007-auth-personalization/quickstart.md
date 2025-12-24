# Quickstart: User Authentication and Personalization (Refined)

This guide provides a quick overview of the refined authentication architecture, which uses a dedicated Better-Auth service for authentication and a Python backend for personalized content.

## Architecture Overview

This feature operates with two backend services:
1.  **Auth Service (Node.js)**: Runs the `Better-Auth` server. It handles all user registration, login, and session creation. It connects to the Neon DB to store user and session data.
2.  **API Service (Python/FastAPI)**: The main application backend. It validates session tokens from the frontend by querying the DB and serves personalized content.

## Auth Service (Node.js) Setup

### 1. Create a new Node.js project

```bash
mkdir auth-backend
cd auth-backend
npm init -y
npm install typescript ts-node @types/node --save-dev
# Add other Better-Auth dependencies (e.g., better-auth, better-auth database adapter)
```

### 2. Configure Better-Auth

Create a `better-auth` server instance, connect it to the Neon DB using the appropriate adapter, and expose the auth endpoints. This service must be running for the frontend to work.

*(Note: The detailed setup for the Better-Auth server is outside the scope of this quickstart and should follow the official Better-Auth documentation.)*

## API Service (Python) Setup

### 1. Dependencies

Ensure your Python environment has a database driver:

```bash
uv add asyncpg
uv add sqlmodel
```

### 2. Session Validation Logic

The backend will need a service to read the `Authorization` header and validate the session token against the database.

```python
# app/security.py

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import sqlalchemy
import datetime

# Assume a db session dependency 'get_db_session' exists
# Assume a Session model exists that maps to the Better-Auth session table

bearer_scheme = HTTPBearer()

async def validate_session(token: HTTPAuthorizationCredentials = Depends(bearer_scheme), db = Depends(get_db_session)):
    session_token = token.credentials
    query = sqlalchemy.select(Session).where(Session.id == session_token)
    result = await db.execute(query)
    session = result.scalar_one_or_none()

    if not session or session.expires_at < datetime.datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token",
        )
    return session.user_id # Return the user_id for use in the endpoint
```

This `validate_session` dependency can then be used on protected endpoints.

## Frontend Setup

### 1. Installation

Install the `better-auth` client and `axios`:

```bash
npm install better-auth axios
```

### 2. Configuration

Configure the `better-auth/react` client to point to your running **Auth Service (Node.js)**.

### 3. API Service with Interceptor

The frontend's `axios` instance for the **API Service (Python)** should be configured with an interceptor to send the session token.

```javascript
// src/services/api.js
import axios from 'axios';
import { useAuth } from 'better-auth/react'; // Or however the token is accessed

const api = axios.create({
  baseURL: 'http://localhost:8000', // Your Python backend URL
});

api.interceptors.request.use(
  (config) => {
    // This is a conceptual example. The actual method to get the token
    // will depend on the Better-Auth client library.
    const { getSessionToken } = useAuth(); 
    const token = getSessionToken(); 

    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
```