from typing import Optional

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import LLMConfig


def test_llm_config(llm_config_data: dict):
    """
    Basic test that LLMConfig class is working as expected.

    Args:
        llm_config_data: Some data to define a LLMConfig object
    """

    # Instantiate a LLMConfig object
    llm_config = LLMConfig(**llm_config_data)

    assert llm_config.model_dump() == llm_config_data


@pytest.mark.parametrize(
    "llm_provider_field, field, expected",
    [
        ("openai", "ollama_url", None),
        ("ollama", "openai_api_key", None),
        ("ollama", "temperature", 0.0),
    ],
    indirect=["llm_provider_field"],
)
def test_llm_config_optional(
    llm_config_data: dict, field: str, expected: Optional[float]
):
    """
    Test that LLMConfig object does not raise an error when missing an optional field.

    Args:
        llm_config_data: Some data to define a LLMConfig object
        field: An optional field to remove from the LLM_config_data
    """

    # Remove an optional field
    del llm_config_data[field]

    # Try to instantiate a LLMConfig object with a missing optional field
    llm_config = LLMConfig(**llm_config_data)

    assert llm_config.model_dump()[field] == expected


@pytest.mark.parametrize("field", ["provider", "model"])
def test_llm_config_raise_missing(llm_config_data: dict, field: str):
    """
    Test that the LLMConfig model raises an error when missing a required field.

    Args:
        llm_config_data: Some data to define an LLMConfig object
        field: A field to remove from the llm_config_data
    """

    # Remove a required field
    del llm_config_data[field]

    # Try to instantiate an LLMConfig object with a missing required field
    with pytest.raises(ValidationError):
        LLMConfig(**llm_config_data)


@pytest.mark.parametrize(
    "llm_provider_field, field",
    [("openai", "openai_api_key"), ("ollama", "ollama_url")],
    indirect=["llm_provider_field"],
)
def test_check_provider(llm_config_data: dict, field: str):
    """
    Test that check_provider method raises an error when missing a required field.

    Args:
        llm_config_data: Some data to define a LLMConfig object
        field: A field to remove from the llm_config_data
    """

    # Remove a required field
    del llm_config_data[field]

    # Try to instantiate a LLMConfig object with a missing required field
    with pytest.raises(ValueError):
        LLMConfig.check_provider(llm_config_data)
