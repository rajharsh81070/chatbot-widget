import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from ..controllers import chat_controller
from ..core import get_db

router = APIRouter()


@router.post("/start_session", response_model=uuid.UUID)
async def start_session(db: Session = Depends(get_db)):
    """
    Start a new chat session.

    Args:
        db (Session): Database session dependency.

    Returns:
        uuid.UUID: The newly created session ID.
    """
    return chat_controller.create_session(db)
