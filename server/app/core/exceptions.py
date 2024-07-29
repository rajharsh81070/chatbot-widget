from fastapi import HTTPException, status


class ChatbotException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class SessionNotFoundException(ChatbotException):
    def __init__(self, detail: str = "Session not found or invalid"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class MessageNotFoundException(ChatbotException):
    def __init__(self, detail: str = "Message not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnauthorizedOperationException(ChatbotException):
    def __init__(self, detail: str = "Unauthorized operation"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class InvalidInputException(ChatbotException):
    def __init__(self, detail: str = "Invalid input data"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
