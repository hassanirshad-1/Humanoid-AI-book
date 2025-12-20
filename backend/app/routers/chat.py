from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Any, AsyncGenerator
import json
import re
from agents import Runner

from app.agents.tutor_agent import get_tutor_agent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    context: Dict[str, Any] = {}

class ChatResponse(BaseModel):
    type: str # "data", "error", "end"
    content: str
    session_id: str = None

async def generate_response_stream(session_id: str, message: str, chapter: str = None) -> AsyncGenerator[str, None]:
    try:
        # Initialize the agent with the current chapter context
        agent = get_tutor_agent(current_chapter=chapter)
        
        # Run the agent using the Agents SDK Runner
        # We don't pass chat history explicitly here because the Agents SDK 
        # manages conversation state if we were using a persistent Thread.
        # For this MVP, we treat each request as a new turn (stateless for now, or history could be passed in prompt).
        # To make it truly conversational, we'd typically append history to the prompt 
        # or use the SDK's memory if available. For now, we trust the context window.
        
        # Stream the response
        # The Runner.run method doesn't support streaming natively in the same way for all models yet 
        # in the simplified SDK wrapper, but let's check if we can yield tokens.
        # If strict streaming is needed, we might use the client directly or check Runner capabilities.
        # ALLOWANCE: For this specific hackathon step, we will use the standard Runner 
        # and simulate streaming or yield the final result if "run" is atomic.
        # HOWEVER, to give the "live" feel, let's assume valid atomic streaming is the goal.
        
        # ACTUALLY: The safest path with this specific SDK setup is to await the final response
        # and then stream it out (simulated) OR use the client.stream() method if we want true token-by-token.
        
        result = await Runner.run(agent, message)
        final_text = result.final_output
        
        # Simulate streaming to frontend (since Runner absorbs the stream internally usually)
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
async def chat_endpoint(chat_request: ChatRequest, request: Request):
    session_id = chat_request.context.get("session_id") or "new_session"

    current_url = chat_request.context.get("current_url")
    chapter = None
    if current_url:
        match = re.search(r"/(chapter-\d{2}-[^/]+)", current_url)
        if match:
            chapter = match.group(1)
            print(f"DEBUG: Chat context restricted to {chapter}")

    return StreamingResponse(
        generate_response_stream(session_id, chat_request.message, chapter),
        media_type="text/event-stream"
    )