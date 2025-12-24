"""
backend/app/routers/users.py

User-related endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_session
from app.security import validate_session
from app.models import User, UserRead, UserUpdate

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserRead)
async def get_me(
    user_id: str = Depends(validate_session),
    db: AsyncSession = Depends(get_session)
):
    """Retrieves the current user's profile based on session validation."""
    logger.info(f"Fetching profile for user: {user_id}")
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        logger.warning(f"User profile not found in database for user_id: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
        
    return user

@router.patch("/me", response_model=UserRead)
async def update_me(
    update_data: UserUpdate,
    user_id: str = Depends(validate_session),
    db: AsyncSession = Depends(get_session)
):
    """Updates the current user's personalization settings."""
    logger.info(f"Updating profile for user: {user_id} with data: {update_data.model_dump(exclude_unset=True)}")
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        logger.warning(f"User profile not found for update, user_id: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
        
    # Update fields if provided
    if update_data.skill_level is not None:
        user.skill_level = update_data.skill_level
    if update_data.operating_system is not None:
        user.operating_system = update_data.operating_system
        
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    logger.info(f"Successfully updated profile for user: {user_id}")
    return user
