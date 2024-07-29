from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .exceptions import ChatbotException
from .response_models import GenericResponse


async def chatbot_exception_handler(request: Request, exc: ChatbotException):
    return JSONResponse(
        status_code=exc.status_code,
        content=GenericResponse(status="error", message=exc.detail).dict()
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=GenericResponse(
            status="error", message="Validation error", data=exc.errors()).dict()
    )


async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=GenericResponse(
            status="error", message="An unexpected error occurred").dict()
    )
