from pydantic import BaseModel
from datetime import datetime
import uuid

class MessageCreate(BaseModel):
    """
    Schema for creating a new message.
    """
    content: str

class MessageResponse(BaseModel):
    """
    Schema for message responses.
    """
    id: int
    session_id: uuid.UUID
    content: str
    is_from_user: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True