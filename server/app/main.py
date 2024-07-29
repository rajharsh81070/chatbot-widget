from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError
from .core import session_validator, Base
from .routes import chat_router
from .core import engine
from .core import ChatbotException, chatbot_exception_handler, validation_exception_handler, generic_exception_handler

# Load environment variables
load_dotenv()

app = FastAPI(title="Chat Widget Backend")

app.add_exception_handler(ChatbotException, chatbot_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Create database tables
Base.metadata.create_all(bind=engine)

app.middleware("http")(session_validator)

app.include_router(chat_router, prefix="/api/v1/chat", tags=["chat"])


@app.get("/")
async def root():
    return {
        "message": "Welcome!!",
        "success": True
    }
