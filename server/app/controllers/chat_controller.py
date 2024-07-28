import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..models.models import Session as DbSession


def create_session(db: Session) -> str:
    """
    Create a new chat session.

    Args:
        db (Session): Database session.

    Returns:
        str: The newly created session ID.
    """
    session_id = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(hours=1)
    db_session = DbSession(id=session_id, expires_at=expires_at)
    db.add(db_session)
    db.commit()
    return session_id
