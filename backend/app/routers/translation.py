"""
backend/app/routers/translation.py

API router for the translation endpoint.
"""

from fastapi import APIRouter, HTTPException
import httpx

from ..models import TranslationRequest, TranslationResponse
from ..services.translation import translate_text


router = APIRouter(prefix="/api", tags=["translation"])


@router.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest) -> TranslationResponse:
    """
    Translate text to a target language using the local LLM.
    
    Args:
        request: TranslationRequest containing the text and target language.
        
    Returns:
        TranslationResponse with the translated text.
    """
    try:
        translated_text = await translate_text(
            text=request.text,
            target_language=request.target_language,
        )
        
        return TranslationResponse(
            translated_text=translated_text,
            source_language="English",  # Assuming English source for now
        )

    except httpx.HTTPStatusError as e:
        # Pass through the error details from the translation service
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error from translation service: {e.response.text}",
        )
    except httpx.RequestError as e:
        # Could not connect to the service
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail=f"Unable to connect to translation service: {str(e)}",
        )
    except (KeyError, IndexError) as e:
        # The service response was not in the expected format
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected response format from translation service: {str(e)}",
        )
    except Exception as e:
        # Catch-all for any other unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred during translation: {str(e)}",
        )
