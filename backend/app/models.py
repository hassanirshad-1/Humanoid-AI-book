"""
backend/app/models.py

Pydantic models for the translation API.
"""

from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    """Request model for translation endpoint."""
    
    text: str = Field(
        ...,
        min_length=1,
        description="The source text to be translated."
    )
    target_language: str = Field(
        default="Urdu",
        min_length=1,
        description="The target language for translation."
    )


class TranslationResponse(BaseModel):
    """Response model for translation endpoint."""
    
    translated_text: str = Field(
        ...,
        description="The translated text."
    )
    source_language: str | None = Field(
        default=None,
        description="The detected source language (optional)."
    )

class AgentRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="The prompt to send to the AI agent."
    )

class AgentResponse(BaseModel):
    response: str = Field(
        ...,
        description="The response from the AI agent."
    )
