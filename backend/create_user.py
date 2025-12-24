import asyncio
from app.database import async_session_maker
from app.models import User, UserCreate
from app.users import UserManager
from fastapi_users.db import SQLAlchemyUserDatabase

async def create_user_script():
    async with async_session_maker() as session:
        user_db = SQLAlchemyUserDatabase(session, User)
        user_manager = UserManager(user_db)
        
        print("Attempting to create user...")
        try:
            user = await user_manager.create(
                UserCreate(
                    email="hassanirshad788@gmail.com",
                    password="password123",
                    name="Hassan Irshad",
                    skill_level="Expert",
                    operating_system="Windows",
                    is_active=True,
                    is_verified=True,
                    is_superuser=True
                )
            )
            print(f"User Created Successfully: {user.email}")
        except Exception as e:
            print(f"Error creating user: {e}")

if __name__ == "__main__":
    asyncio.run(create_user_script())
