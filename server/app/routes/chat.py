import uuid
from fastapi import APIRouter, Depends, Cookie, Path, Response
from sqlalchemy.orm import Session
from ..controllers import chat_controller
from ..core import get_db
from ..core import GenericResponse
from ..schemas import MessageResponse, MessageCreate

router = APIRouter()


@router.post("/start_session", response_model=GenericResponse)
async def start_session(response: Response, db: Session = Depends(get_db)):
    """Start a new chat session."""
    session_id = chat_controller.create_session(db)
    response.set_cookie(key="session_id", value=str(session_id), httponly=True)
    return GenericResponse(status="success", message="Session created", data={"session_id": str(session_id)})


@router.post("/create_message", response_model=GenericResponse)
async def create_message(
    message: MessageCreate,
    session_id: uuid.UUID = Cookie(...),
    db: Session = Depends(get_db)
):
    """Create a message in a chat session."""
    response = chat_controller.create_message(
        db, str(session_id), message.content)
    return GenericResponse(status="success", message="Message created.", data=[MessageResponse.from_orm(msg) for msg in response])


@router.patch("/edit_message/{message_id}", response_model=GenericResponse)
async def edit_message(
    message: MessageCreate,
    message_id: int = Path(..., gt=0),
    session_id: uuid.UUID = Cookie(...),
    db: Session = Depends(get_db)
):
    """Edit an existing message."""
    updated_message = chat_controller.edit_message(
        db, str(session_id), message_id, message.content)
    return GenericResponse(status="success", message="Message updated", data=MessageResponse.from_orm(updated_message))


@router.delete("/delete_message/{message_id}", response_model=GenericResponse)
async def delete_message(
    message_id: int = Path(..., gt=0),
    session_id: uuid.UUID = Cookie(...),
    db: Session = Depends(get_db)
):
    """Delete a message."""
    chat_controller.delete_message(db, str(session_id), message_id)
    return GenericResponse(status="success", message="Message deleted successfully")


@router.get("/get_messages", response_model=GenericResponse)
async def get_messages(
    session_id: uuid.UUID = Cookie(...),
    db: Session = Depends(get_db)
):
    """Get all messages for a chat session."""
    messages = chat_controller.get_messages(db, str(session_id))
    return GenericResponse(status="success", message="Messages retrieved", data=[MessageResponse.from_orm(msg) for msg in messages])
