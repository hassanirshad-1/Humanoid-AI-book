"""
backend/app/database.py

Database connection and session management.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import make_url
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
import ssl
from app.config import settings

# Parse the URL to handle sslmode for asyncpg
url = make_url(settings.DATABASE_URL)
connect_args = {}

# asyncpg does not support sslmode in the connection URL query parameters
if "sslmode" in url.query:
    ssl_mode = url.query["sslmode"]
    
    # Remove sslmode from query parameters to avoid TypeError in connect()
    new_query = {k: v for k, v in url.query.items() if k != "sslmode"}
    url = url._replace(query=new_query)
    
    # Configure SSL context for asyncpg based on sslmode
    # 'require' generally means encryption is required. 
    # For compatibility with typical cloud setups (like Neon), we'll use a basic SSL context.
    if ssl_mode == "require":
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        connect_args["ssl"] = ctx

# Create async engine
engine = create_async_engine(
    url, 
    echo=True, 
    future=True,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_recycle=300,
)

# Async session factory
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncSession:
    """Dependency for getting a database session."""
    async with async_session_maker() as session:
        yield session

from app.models import User

async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)

