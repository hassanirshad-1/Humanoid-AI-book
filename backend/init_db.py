import asyncio
from app.database import engine
from app.models import SQLModel

async def init_db():
    async with engine.begin() as conn:
        print("Dropping existing tables...")
        await conn.run_sync(SQLModel.metadata.drop_all)
        print("Creating new tables...")
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database initialized.")

if __name__ == "__main__":
    asyncio.run(init_db())
