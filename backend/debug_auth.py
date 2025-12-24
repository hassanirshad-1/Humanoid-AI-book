import asyncio
from sqlalchemy import select
from app.models import User
from app.database import async_session_maker

async def check_user():
    email = "hassanirshad788@gmail.com"
    output = []
    async with async_session_maker() as session:
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalars().first()
        
        if user:
            output.append(f"User FOUND: {user.email}")
            output.append(f"ID: {user.id}")
            output.append(f"Active: {user.is_active}")
            output.append(f"Verified: {user.is_verified}")
            output.append(f"Superuser: {user.is_superuser}")
            output.append(f"Hashed Password (prefix): {user.hashed_password[:15] if user.hashed_password else 'None'}")
        else:
            output.append(f"User NOT FOUND: {email}")

    with open("debug_output.txt", "w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    asyncio.run(check_user())
