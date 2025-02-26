import pytest
from pydantic import ValidationError

from uncertainty_engine_types import TextEmbeddingsConfig


def test_text_embeddings_config(text_embeddings_config_data: dict):
    """
    Basic test that TextEmbeddingsConfig class is working as expected.

    Args:
        text_embeddings_config_data: Some data to define a TextEmbeddingsConfig object
    """

    # Instantiate a TextEmbeddingsConfig object
    text_embeddings_config = TextEmbeddingsConfig(**text_embeddings_config_data)

    assert text_embeddings_config.model_dump() == text_embeddings_config_data


def test_text_embeddings_config_raise_missing(text_embeddings_config_data: dict):
    """
    Test that TextEmbeddingsConfig object raises an error when missing a required field.

    Args:
        text_embeddings_config_data: Some data to define a TextEmbeddingsConfig object
    """

    # Remove a required field
    del text_embeddings_config_data["provider"]

    # Try to instantiate a TextEmbeddingsConfig object with a missing required field
    with pytest.raises(ValidationError):
        TextEmbeddingsConfig(**text_embeddings_config_data)


@pytest.mark.parametrize(
    "embeddings_provider_field, field",
    [("openai", "model"), ("openai", "ollama_url"), ("ollama", "openai_api_key")],
    indirect=["embeddings_provider_field"],
)
def test_text_embeddings_config_optional(text_embeddings_config_data: dict, field: str):
    """
    Test that TextEmbeddingsConfig object does not raise an error when missing an optional field.

    Args:
        text_embeddings_config_data: Some data to define a TextEmbeddingsConfig object
        field: An optional field to remove from the text_embeddings_config_data
    """

    # Remove an optional field
    del text_embeddings_config_data[field]

    # Try to instantiate a TextEmbeddingsConfig object with a missing optional field
    text_embeddings_config = TextEmbeddingsConfig(**text_embeddings_config_data)

    assert text_embeddings_config.model_dump()[field] is None


@pytest.mark.parametrize(
    "embeddings_provider_field, field",
    [("openai", "openai_api_key"), ("ollama", "ollama_url")],
    indirect=["embeddings_provider_field"],
)
def test_check_provider(text_embeddings_config_data: dict, field: str):
    """
    Test that check_provider method raises an error when missing a required field.

    Args:
        text_embeddings_config_data: Some data to define a TextEmbeddingsConfig object
        field: A field to remove from the text_embeddings_config_data
    """

    # Remove a required field
    del text_embeddings_config_data[field]

    # Try to instantiate a TextEmbeddingsConfig object with a missing required field
    with pytest.raises(ValueError):
        TextEmbeddingsConfig.check_provider(text_embeddings_config_data)
