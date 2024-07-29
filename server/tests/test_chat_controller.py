import pytest
from unittest.mock import Mock
from app.controllers.chat_controller import create_session, create_message
from app.core import InvalidInputException


def test_create_session():
    mock_db = Mock()
    session_id = create_session(mock_db)
    assert session_id is not None
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()


def test_create_message_empty_content():
    mock_db = Mock()
    with pytest.raises(InvalidInputException):
        create_message(mock_db, "test_session_id", "")
