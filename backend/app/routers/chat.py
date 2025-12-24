from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Any, AsyncGenerator, Optional
import json
import re
from agents import Runner
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.agents.tutor_agent import get_tutor_agent
from app.database import get_session
from app.models import User
from app.users import current_active_user

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    context: Dict[str, Any] = {}

class ChatResponse(BaseModel):
    type: str # "data", "error", "end"
    content: str
    session_id: str = None

async def generate_response_stream(
    session_id: str, 
    message: str, 
    chapter: str = None,
    skill_level: str = "Beginner",
    operating_system: str = "Linux"
) -> AsyncGenerator[str, None]:
    try:
        # Initialize the agent with the current chapter context and personalization
        agent = get_tutor_agent(
            current_chapter=chapter,
            skill_level=skill_level,
            operating_system=operating_system
        )
        
        result = await Runner.run(agent, message)
        final_text = result.final_output
        
        # Simulate streaming to frontend
        chunk_size = 10 
        for i in range(0, len(final_text), chunk_size):
            chunk = final_text[i:i+chunk_size]
            yield json.dumps({"type": "data", "content": chunk}) + "\n"
            import asyncio
            await asyncio.sleep(0.01) # fast typewriter effect
            
    except Exception as e:
        yield json.dumps({"type": "error", "content": f"Agent error: {str(e)}"}) + "\n"
        print(f"Error during agent response generation: {e}")
    finally:
        yield json.dumps({"type": "end", "content": "", "session_id": session_id}) + "\n"


@router.post("/chat")
async def chat_endpoint(
    chat_request: ChatRequest, 
    request: Request,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_session)
):
    session_id = chat_request.context.get("session_id") or "new_session"

    current_url = chat_request.context.get("current_url")
    chapter = None
    if current_url:
        match = re.search(r"/(chapter-\d{2}-[^/]+)", current_url)
        if match:
            chapter = match.group(1)
            print(f"DEBUG: Chat context restricted to {chapter}")

    # Use authenticated user's profile
    skill_level = user.skill_level or "Beginner"
    operating_system = user.operating_system or "Linux"
    print(f"DEBUG: Personalized chat for {user.email}: {skill_level}, {operating_system}")

    return StreamingResponse(
        generate_response_stream(
            session_id, 
            chat_request.message, 
            chapter,
            skill_level,
            operating_system
        ),
        media_type="text/event-stream"
    )