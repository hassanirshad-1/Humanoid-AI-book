"""
backend/app/config.py

Configuration module for loading environment variables.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    # Agent configuration (Dynamic switching)
    AGENT_MODEL: str = os.getenv("AGENT_MODEL", "llama3.1:8b")

    # Translation configuration
    TRANSLATION_PROVIDER: str = os.getenv("TRANSLATION_PROVIDER", "ollama")
    TRANSLATION_MODEL: str = os.getenv("TRANSLATION_MODEL", "llama3.1:8b")
    
    
    # Provider-specific Base URLs (loaded from env or defaults)
    GEMINI_BASE_URL: str = os.getenv("GEMINI_API_BASE_URL") or os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_API_BASE_URL", "http://localhost:11434/v1")  # Normalized key name

    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "ollama")

    # CORS settings
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")


settings = Settings()
