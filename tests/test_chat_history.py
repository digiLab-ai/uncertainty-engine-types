import pytest
from pydantic import ValidationError

from uncertainty_engine_types import ChatHistory


def test_chat_history(chat_history_data: dict):
    """
    Basic test that ChatHistory class is working as expected.

    Args:
        chat_history_data: Some data to define a ChatHistory object
    """

    # Instantiate a ChatHistory object
    chat_history = ChatHistory(**chat_history_data)

    assert chat_history.model_dump() == chat_history_data


def test_chat_history_raise_missing(chat_history_data: dict):
    """
    Test that ChatHistory object raises an error when missing a required field.

    Args:
        chat_history_data: Some data to define a ChatHistory object
    """

    # Remove a required field
    del chat_history_data["messages"]

    # Try to instantiate a ChatHistory object with a missing required field
    with pytest.raises(ValidationError):
        ChatHistory(**chat_history_data)
