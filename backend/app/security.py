"""
backend/app/security.py

Security dependencies for session validation.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_session
from app.models import Session
import datetime

logger = logging.getLogger(__name__)

bearer_scheme = HTTPBearer()

async def validate_session(
    token: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_session)
) -> str:
    """
    Validates the session token from the Authorization header against the database.
    Returns the user_id if valid.
    """
    session_token = token.credentials
    logger.debug(f"Validating session token: {session_token[:10]}...")
    
    # Query the session table created by Better-Auth
    # The 'token' field contains the actual session secret sent to the client.
    query = select(Session).where(Session.token == session_token)
    result = await db.execute(query)
    session = result.scalar_one_or_none()

    if not session:
        logger.warning(f"Invalid session token attempt: {session_token[:10]}...")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session token",
        )
        
    # Check expiration
    # Ensure both are offset-aware or both offset-naive. 
    # Better-Auth uses UTC.
    if session.expiresAt.replace(tzinfo=datetime.timezone.utc) < datetime.datetime.now(datetime.timezone.utc):
        logger.info(f"Session expired for user_id: {session.userId}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session token expired",
        )
        
    logger.info(f"Session validated successfully for user_id: {session.userId}")
    return session.userId
