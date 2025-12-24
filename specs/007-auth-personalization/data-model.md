# Data Model: User Authentication and Personalization (Refined)

This document defines the data models for the refined user personalization feature. The authentication flow is managed by a dedicated `Better-Auth` service, which owns the `User` and `Session` tables in the database. The Python backend reads from these tables for session validation and to retrieve user data.

## User Model (as managed by Better-Auth)

This model represents an individual learner.

### Assumed SQLModel Definition

```python
import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    # Other fields managed by Better-Auth (e.g., password hash) are omitted for brevity

    # Personalization fields
    skill_level: Optional[str] = Field(default=None)
    operating_system: Optional[str] = Field(default=None)
```

### Fields

-   **id**: A unique identifier for the user.
-   **email**: The user's email address.
-   **skill_level**: An optional string to store the user's self-assessed skill level.
-   **operating_system**: An optional string to store the user's primary operating system.

## Session Model (as managed by Better-Auth)

This model represents a user's authenticated session. The Python backend will query this table to validate session tokens.

### Assumed SQLModel Definition

```python
import uuid
import datetime
from sqlmodel import Field, SQLModel

class Session(SQLModel, table=True):
    id: str = Field(primary_key=True) # The session token itself
    user_id: uuid.UUID = Field(foreign_key="user.id")
    expires_at: datetime.datetime
```

### Fields

-   **id**: The unique session token string.
-   **user_id**: A foreign key linking to the `User` table.
-   **expires_at**: A timestamp indicating when the session is no longer valid.

**Note**: The exact schema of these tables is determined by the `Better-Auth` database adapter. The definitions above are assumptions for planning purposes. Verifying the actual schema will be a key task during implementation.