from typing import Any

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Message


@pytest.mark.parametrize(
    "role_field", ["instruction", "user", "engine"], indirect=["role_field"]
)
def test_message(message_data: dict):
    """
    Basic test that Message model is working as expected.

    Args:
        message_data: Some data to define a Message object
    """

    # Instantiate a Message object
    message = Message(**message_data)

    assert message.model_dump() == message_data


@pytest.mark.parametrize("field", ["role", "content"])
def test_message_raise_missing(message_data: dict, field: str):
    """
    Test that Message object raises an error when missing a required field.

    Args:
        message_data: Some data to define a Message object
        field: A field to remove from the message_data
    """

    # Remove a required field
    del message_data[field]

    # Try to instantiate a Message object with a missing required field
    with pytest.raises(ValidationError):
        Message(**message_data)


def test_message_raise_invalid_role(message_data: dict):
    """
    Test that Message object raises an error when the role field is invalid.

    Args:
        message_data: Some data to define a Message object
    """

    # Change the role field to an invalid value
    message_data["role"] = "invalid"

    # Try to instantiate a Message object with an invalid role field
    with pytest.raises(ValidationError):
        Message(**message_data)


@pytest.mark.parametrize("new_content", [1, 1.0, True, {"valid": "content"}])
def test_content_validator(message_data: dict, new_content: Any):
    """
    Test that the content field is converted to a string if it is not already.

    Args:
        message_data: Some data to define a Message object
        new_content: A new content value to test
    """

    # Change the content field
    message_data["content"] = new_content

    # Instantiate a Message object
    message = Message(**message_data)

    assert message.content == str(new_content)
