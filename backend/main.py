from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, translation
from app.services import indexing_service # Only for type hinting or initial setup if needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(translation.router)

@app.get("/")
async def root():
    return {"message": "AI Tutor Backend is running!"}

def start_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start_server()
