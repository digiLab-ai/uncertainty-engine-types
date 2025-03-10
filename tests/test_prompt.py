import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Prompt


def test_prompt(prompt_data: dict):
    """
    Basic test that Prompt model is working as expected.

    Args:
        prompt_data: Some data to define a Prompt object
    """

    # Instantiate a Prompt object
    prompt = Prompt(**prompt_data)

    assert prompt.model_dump() == prompt_data


def test_prompt_raise_missing(prompt_data: dict):
    """
    Test that Prompt object raises an error when missing a required field.

    Args:
        prompt_data: Some data to define a Prompt object
    """

    # Remove a required field
    del prompt_data["prompt"]

    # Try to instantiate a Prompt object with a missing required field
    with pytest.raises(ValidationError):
        Prompt(**prompt_data)
