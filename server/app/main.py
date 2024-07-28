from fastapi import FastAPI
from dotenv import load_dotenv
from .routes import chat_router
from .models import Base
from .core import engine

# Load environment variables
load_dotenv()

app = FastAPI(title="Chat Widget Backend")

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(chat_router, prefix="/chat", tags=["chat"])


@app.get("/")
async def root():
    return {
        "message": "Welcome!!",
        "success": True
    }
