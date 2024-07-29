from ..core.dependencies import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class Session(Base):
    """
    Session model representing a chat session.
    """
    __tablename__ = "sessions"

    id = Column(String(36), primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    expires_at = Column(DateTime)

    messages = relationship("Message", back_populates="session")

    def __repr__(self):
        return f"<Session(id={self.id}, expires_at={self.expires_at})>"


class Message(Base):
    """
    Message model representing a chat message.
    """
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), ForeignKey("sessions.id"), nullable=False)
    content = Column(Text, nullable=False)
    is_from_user = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    session = relationship("Session", back_populates="messages")

    def __repr__(self):
        return f"<Message(id={self.id}, session_id={self.session_id}, content={self.content}, is_from_user={self.is_from_user})>"
