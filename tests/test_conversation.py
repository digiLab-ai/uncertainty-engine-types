import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Conversation


def test_conversation(conversation_data):
    """
    Basic test that Conversation class is working as expected
    """

    # Instantiate a Conversation object
    conversation = Conversation(**conversation_data)

    assert conversation.model_dump() == conversation_data


def test_conversation_raise_missing(conversation_data):
    """
    Test that Conversation object raises an error when missing a required field
    """

    # Remove a required field
    del conversation_data["messages"]

    # Try to instantiate a Conversation object with a missing required field
    with pytest.raises(ValidationError):
        Conversation(**conversation_data)
