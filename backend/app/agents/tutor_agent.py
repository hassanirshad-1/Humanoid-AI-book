import logging
import json
from typing import Dict, Any, List
from agents import Agent, OpenAIChatCompletionsModel, function_tool
import qdrant_client
from qdrant_client import models
from qdrant_client.models import Filter, FieldCondition, MatchValue
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from openai import AsyncOpenAI

from app.config import settings

# Configure logging
logger = logging.getLogger(__name__)

# --- Qdrant & Embedding Setup ---
def get_qdrant_client():
    return qdrant_client.QdrantClient(url=settings.QDRANT_URL)

def get_embedding_model():
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    return GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=settings.GEMINI_API_KEY)

# --- Tool Logic ---

@function_tool
async def qdrant_retrieval_tool(query: str, chapter: str = None) -> str:
    """
    Retrieves relevant textbook content from Qdrant based on a user's query.
    Can be filtered by a specific chapter using the 'chapter' argument (e.g., 'chapter-01-intro').
    """
    try:
        print(f"DEBUG: qdrant_retrieval_tool called with query='{query}', chapter='{chapter}'")
        limit = 5
        client = get_qdrant_client()
        embedding_model = get_embedding_model()

        query_vector = embedding_model.embed_query(query)

        query_filter = None
        if chapter and chapter not in ["None", "Global Search", "all", "unknown"]:
            query_filter = Filter(
                should=[
                    FieldCondition(
                        key="chapter",
                        match=MatchValue(value=chapter),
                    )
                ]
            )

        search_result = client.query_points(
            collection_name=settings.QDRANT_COLLECTION_NAME,
            query=query_vector,
            query_filter=query_filter,
            limit=limit,
        ).points

        print(f"DEBUG: Qdrant found {len(search_result)} points.")
        retrieved_docs = []
        for hit in search_result:
            file_path = hit.payload.get("file_path")
            source_url = settings.get_source_url_from_filepath(file_path) if file_path else ""
            
            doc_info = {
                "content": hit.payload.get("text_content"),
                "metadata": {
                    "source": f"Chapter: {hit.payload.get('chapter')}, Lesson: {hit.payload.get('lesson')}",
                    "heading": hit.payload.get("heading_path"),
                    "url": source_url
                }
            }
            retrieved_docs.append(doc_info)
        
        return json.dumps(retrieved_docs, ensure_ascii=False)

    except Exception as e:
        logger.error(f"Error in qdrant_retrieval_tool: {e}")
        return json.dumps({"error": str(e)})


# --- Agent Factory ---

TUTOR_SYSTEM_PROMPT = """You are a premium AI Tutor for a textbook on Physical AI & Humanoid Robotics.

GOAL: Answer questions precisely using ONLY the provided textbook context.

STYLE & FORMATTING:
1. **Markdown**: Use bolding, bullet points, and headers to make your response easy to read.
2. **Math**: Use LaTeX for all mathematical expressions (e.g., $E = mc^2$).
3. **Citations**: EVERY factual claim must have a clickable citation.
   - **Format**: `[Lesson Title](url)` 
   - **Constraint**: Use the EXACT `/docs/...` URL provided in the tool's metadata. 
   - **Placement**: Place citations immediately after the sentence or paragraph they support.
4. **Tone**: Helpful, academic, and encouraging.
5. **Language**: If the user asks in another language (like Urdu), respond in that language.

USER PERSONALIZATION (CRITICAL):
- **Skill Level**: {skill_level}. 
    - If "Beginner": Focus on intuition, analogies, and foundational concepts. Avoid advanced mathematical derivations unless asked.
    - If "Intermediate": Balance theory and practice.
    - If "Advanced": Be precise, use formal terminology, and feel free to include complex mathematical or architectural details.
- **Operating System**: {operating_system}. 
    - When providing terminal commands, scripts, or installation steps, ONLY provide them for this OS. 
    - If a command is OS-specific (e.g., `apt-get` vs `brew`), clarify that you are tailoring it for their system.

PROCESS:
1. Use `qdrant_retrieval_tool` for EVERY user query.
2. If the tool returns no relevant content, respond with: "I'm sorry, I couldn't find specific information on that in the current textbook chapters."

CONTEXT:
- Current Chapter Context: {chapter} (Search for this if relevant, but provide global info if needed).
"""

def get_tutor_agent(
    current_chapter: str = None, 
    skill_level: str = "Beginner", 
    operating_system: str = "Linux"
) -> Agent:
    """
    Creates and returns a Tutor Agent equipped with the retrieval tool and personalization context.
    """
    
    # Configure Client (Reusing Translation Logic Pattern)
    provider = settings.TRANSLATION_PROVIDER.lower()
    
    # Logic to pick base URL/Model based on provider
    if provider == 'gemini':
         base_url = settings.GEMINI_BASE_URL
         api_key = settings.GEMINI_API_KEY
         model_id = settings.TRANSLATION_MODEL
    else:
         base_url = settings.OLLAMA_BASE_URL
         api_key = settings.OLLAMA_API_KEY
         model_id = settings.TRANSLATION_MODEL

    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    
    model = OpenAIChatCompletionsModel(model=model_id, openai_client=client)
    
    formatted_prompt = TUTOR_SYSTEM_PROMPT.format(
        chapter=current_chapter if current_chapter else "Global Search",
        skill_level=skill_level,
        operating_system=operating_system
    )

    return Agent(
        model=model,
        name="Robotics AI Tutor",
        instructions=formatted_prompt,
        tools=[qdrant_retrieval_tool],
    )
