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

    # RAG Configuration
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_COLLECTION_NAME: str = "textbook_content"
    # Resolve MDX path absolute to project root (2 levels up from backend/app/config.py)
    MDX_DOCS_PATH: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend/docs"))

    # CORS settings
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

    def get_source_url_from_filepath(self, file_path: str) -> str:
        """Converts a file path to a Docusaurus-compatible URL."""
        # Example: "frontend/docs/chapter-01-intro/1.1-philosophy.mdx"
        # Becomes: "/docs/chapter-01-intro/1.1-philosophy"
        
        # Remove "frontend/" prefix if it exists
        if file_path.startswith("frontend/"):
            file_path = file_path[len("frontend/"):]
        
        # Remove .mdx extension
        if file_path.endswith(".mdx"):
            file_path = file_path[:-len(".mdx")]
        
        # Ensure it starts with /
        if not file_path.startswith("/"):
            file_path = "/" + file_path
            
        return file_path


settings = Settings()
