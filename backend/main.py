"""
backend/main.py

Main FastAPI application entry point.

Run with: uv run uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import translation

# Create FastAPI application
app = FastAPI(
    title="Robotics Book Backend",
    description="Backend API for the AI-native Robotics Textbook",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_ORIGIN,
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(translation.router)


@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {"status": "ok", "message": "Robotics Book Backend API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
