from typing import List
from ..core import MessageNotFoundException, UnauthorizedOperationException, InvalidInputException
from ..services import generate_response
from ..models import Session as DbSession, Message
import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..models import Session as DbSession


def create_session(db: Session) -> uuid.UUID:
    """
    Create a new chat session.

    Args:
        db (Session): Database session.

    Returns:
        str: The newly created session ID.
    """
    session_id = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(hours=365*24)
    db_session = DbSession(id=session_id, expires_at=expires_at)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    print(f"Created session: {db_session.id}")
    return session_id


def create_message(db: Session, session_id: uuid.UUID, content: str) -> List[Message]:
    """
    Create a message in a chat session and return all messages for the session.

    Args:
        db (Session): Database session.
        session_id (str): The session ID.
        content (str): The message content.

    Returns:
        List[Message]: All messages for the session, including the new ones.
    """
    if not content.strip():
        raise InvalidInputException("Message content cannot be empty")

    previous_messages = db.query(Message).filter(
        Message.session_id == session_id).order_by(Message.created_at.desc()).limit(5).all()
    previous_messages.reverse()
    user_message = Message(session_id=session_id,
                           content=content, is_from_user=True)
    print(f"User message: {user_message.__repr__()}")
    db.add(user_message)

    bot_response = generate_response(content, previous_messages)
    print(f"Bot response: {bot_response}")
    bot_message = Message(session_id=session_id,
                          content=bot_response, is_from_user=False)
    db.add(bot_message)

    db.commit()
    db.refresh(bot_message)
    all_messages = db.query(Message).filter(
        Message.session_id == session_id).order_by(Message.created_at).all()
    print(
        f"All messages for session: {[msg.__repr__() for msg in all_messages]}")

    return all_messages


def edit_message(db: Session, session_id: uuid.UUID, message_id: int, new_content: str) -> Message:
    """
    Edit a message in a chat session.

    Args:
        db (Session): Database session.
        session_id (str): The session ID.
        message_id (int): The message ID.
        new_content (str): The new message content.

    Returns:
        Message: The updated message
    """
    if not new_content.strip():
        raise InvalidInputException("Message content cannot be empty")

    message = db.query(Message).filter(
        Message.id == message_id, Message.session_id == session_id).first()
    if not message:
        raise MessageNotFoundException("Message not found")
    if not message.is_from_user:
        raise UnauthorizedOperationException("Cannot edit bot messages")

    message.content = new_content
    message.updated_at = datetime.now()
    db.commit()
    db.refresh(message)
    return message


def delete_message(db: Session, session_id: uuid.UUID, message_id: int) -> None:
    """
    Delete a message in a chat session.

    Args:
        db (Session): Database session.
        session_id (str): The session ID.
        message_id (int): The message ID.
    """
    message = db.query(Message).filter(
        Message.id == message_id, Message.session_id == session_id).first()
    if not message:
        raise MessageNotFoundException("Message not found")
    if not message.is_from_user:
        raise UnauthorizedOperationException("Cannot delete bot messages")

    db.delete(message)
    db.commit()


def get_messages(db: Session, session_id: uuid.UUID) -> List[Message]:
    """
    Get all messages for a chat session.

    Args:
        db (Session): Database session.
        session_id (str): The session ID.

    Returns:
        List[Message]: All messages for the session.
    """
    all_messages = db.query(Message).filter(
        Message.session_id == session_id).order_by(Message.created_at).all()
    return all_messages
