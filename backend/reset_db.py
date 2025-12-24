import asyncio
from sqlalchemy import text
from app.database import engine
from app.models import SQLModel

async def reset_db():
    async with engine.begin() as conn:
        print("Dropping old tables (including 'session' and 'user')...")
        # Forcefully drop known tables with CASCADE to handle foreign keys
        await conn.execute(text('DROP TABLE IF EXISTS "session" CASCADE'))
        await conn.execute(text('DROP TABLE IF EXISTS "account" CASCADE'))
        await conn.execute(text('DROP TABLE IF EXISTS "verification" CASCADE'))
        await conn.execute(text('DROP TABLE IF EXISTS "user" CASCADE'))
        
        print("Creating new tables...")
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database reset complete.")

if __name__ == "__main__":
    asyncio.run(reset_db())
