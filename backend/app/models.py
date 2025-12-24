"""
backend/app/models.py

Pydantic and SQLModel definitions for the application.
"""

import uuid
from typing import Optional
from pydantic import BaseModel, Field
from sqlmodel import Field as SQLField, SQLModel
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users import schemas


class TranslationRequest(BaseModel):
    """Request model for translation endpoint."""
    text: str = Field(..., min_length=1, description="The source text to be translated.")
    target_language: str = Field(default="Urdu", min_length=1, description="The target language for translation.")

class TranslationResponse(BaseModel):
    """Response model for translation endpoint."""
    translated_text: str = Field(..., description="The translated text.")
    source_language: str | None = Field(default=None, description="The detected source language (optional).")

class AgentRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="The prompt to send to the AI agent.")

class AgentResponse(BaseModel):
    response: str = Field(..., description="The response from the AI agent.")


# --- Database Models (SQLModel) ---

class User(SQLModel, table=True):
    """User model compatible with fastapi-users."""
    __tablename__ = "user"

    id: uuid.UUID = SQLField(default_factory=uuid.uuid4, primary_key=True)
    email: str = SQLField(unique=True, index=True)
    hashed_password: str
    is_active: bool = SQLField(default=True)
    is_superuser: bool = SQLField(default=False)
    is_verified: bool = SQLField(default=False)

    name: Optional[str] = SQLField(default=None)
    skill_level: Optional[str] = SQLField(default=None)
    operating_system: Optional[str] = SQLField(default=None)


# --- API Schemas (FastAPI Users) ---

class UserRead(schemas.BaseUser[uuid.UUID]):
    name: Optional[str] = None
    skill_level: Optional[str] = None
    operating_system: Optional[str] = None

class UserCreate(schemas.BaseUserCreate):
    name: str
    skill_level: Optional[str] = "Beginner"
    operating_system: Optional[str] = "Windows"

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str] = None
    skill_level: Optional[str] = None
    operating_system: Optional[str] = None