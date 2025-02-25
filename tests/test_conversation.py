import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Conversation


def test_conversation(conversation_data: dict):
    """
    Basic test that Conversation class is working as expected.

    Args:
        conversation_data: Some data to define a Conversation object
    """

    # Instantiate a Conversation object
    conversation = Conversation(**conversation_data)

    assert conversation.model_dump() == conversation_data


def test_conversation_raise_missing(conversation_data: dict):
    """
    Test that Conversation object raises an error when missing a required field.

    Args:
        conversation_data: Some data to define a Conversation object
    """

    # Remove a required field
    del conversation_data["messages"]

    # Try to instantiate a Conversation object with a missing required field
    with pytest.raises(ValidationError):
        Conversation(**conversation_data)
