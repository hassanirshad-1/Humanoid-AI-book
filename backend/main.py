from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, translation
from app.users import auth_backend, fastapi_users
from app.models import UserRead, UserCreate, UserUpdate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Authentication Routers (FastAPI Users)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# Feature Routers
app.include_router(chat.router)
app.include_router(translation.router)
# Old users router replaced by fastapi-users
# app.include_router(users.router) 

@app.get("/")
async def root():
    return {"message": "AI Tutor Backend is running!"}

def start_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start_server()
