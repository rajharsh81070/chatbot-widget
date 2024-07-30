from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..core import GenericResponse
from ..core import get_db
from ..models import Session as DbSession
from datetime import datetime
import uuid


async def session_validator(request: Request, call_next):
    if request.method == "OPTIONS":
        return await call_next(request)

    if request.url.path == "/api/v1/chat/start_session":
        return await call_next(request)

    session_id = request.cookies.get("session_id")
    if not session_id:
        return JSONResponse(
            status_code=401,
            content=GenericResponse(
                status="error", message="No active session. Please start a new session.").dict()
        )

    db: Session = next(get_db())
    db_session = db.query(DbSession).filter(DbSession.id == session_id).first()

    print(f"Session ID from cookie: {session_id}")
    print(f"DB Session: {db_session}")
    print(f"All sessions in DB: {db.query(DbSession).all()}")

    if not db_session:
        return JSONResponse(
            status_code=401,
            content=GenericResponse(
                status="error", message="Session not found. Please start a new session.").dict()
        )

    if db_session.expires_at < datetime.now():
        return JSONResponse(
            status_code=401,
            content=GenericResponse(
                status="error", message="Session has expired. Please start a new session.").dict()
        )

    response = await call_next(request)
    return response
