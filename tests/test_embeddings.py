import pytest
from pydantic import ValidationError

from uncertainty_engine_types import TextEmbeddingsConfig


def test_text_embeddings_config(text_embeddings_config_data):
    """
    Basic test that TextEmbeddingsConfig class is working as expected
    """

    # Instantiate a TextEmbeddingsConfig object
    text_embeddings_config = TextEmbeddingsConfig(**text_embeddings_config_data)

    assert text_embeddings_config.model_dump() == text_embeddings_config_data


def test_text_embeddings_config_raise_missing(text_embeddings_config_data):
    """
    Test that TextEmbeddingsConfig object raises an error when missing a required field
    """

    # Remove a required field
    del text_embeddings_config_data["provider"]

    # Try to instantiate a TextEmbeddingsConfig object with a missing required field
    with pytest.raises(ValidationError):
        TextEmbeddingsConfig(**text_embeddings_config_data)


@pytest.mark.parametrize(
    "provider_field, field",
    [("openai", "model"), ("openai", "ollama_url"), ("ollama", "openai_api_key")],
    indirect=["provider_field"],
)
def test_text_embeddings_config_optional(text_embeddings_config_data, field):
    """
    Test that TextEmbeddingsConfig object does not raise an error when missing an optional field
    """

    # Remove an optional field
    del text_embeddings_config_data[field]

    # Try to instantiate a TextEmbeddingsConfig object with a missing optional field
    text_embeddings_config = TextEmbeddingsConfig(**text_embeddings_config_data)

    assert text_embeddings_config.model_dump()[field] is None


@pytest.mark.parametrize(
    "provider_field, field",
    [("openai", "openai_api_key"), ("ollama", "ollama_url")],
    indirect=["provider_field"],
)
def test_check_provider(text_embeddings_config_data, field):
    """
    Test that check_provider method raises an error when missing a required field
    """

    # Remove a required field
    del text_embeddings_config_data[field]

    # Try to instantiate a TextEmbeddingsConfig object with a missing required field
    with pytest.raises(ValueError):
        TextEmbeddingsConfig.check_provider(text_embeddings_config_data)
