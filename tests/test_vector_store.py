import pytest
from pydantic import ValidationError

from uncertainty_engine_types import VectorStoreConfig


def test_vector_store_config(vector_store_config_data: dict):
    """
    Basic test that VectorStoreConfig model is working as expected.

    Args:
        vector_store_config_data: Some data to define a VectorStoreConfig object
    """

    # Instantiate a VectorStoreConfig object
    vector_store_config = VectorStoreConfig(**vector_store_config_data)

    assert vector_store_config.model_dump() == vector_store_config_data


@pytest.mark.parametrize(
    "field",
    ["provider", "host", "embedding_type", "embedding_model", "embedding_api_key"],
)
def test_vector_store_config_raise_missing(vector_store_config_data: dict, field: str):
    """
    Test that VectorStoreConfig object raises an error when missing a required field.

    Args:
        vector_store_config_data: Some data to define a VectorStoreConfig object
        field: A field to remove from the vector_store_config_data
    """

    # Remove a required field
    del vector_store_config_data[field]

    # Try to instantiate a VectorStoreConfig object with a missing required field
    with pytest.raises(ValidationError):
        VectorStoreConfig(**vector_store_config_data)


@pytest.mark.parametrize(
    "field, expected", [("port", "8080"), ("collection", "DefaultCollection")]
)
def test_vector_store_optional(
    vector_store_config_data: dict, field: str, expected: str
):
    """
    Test that VectorStoreConfig object does not raise an error when missing an optional field.

    Args:
        vector_store_data: Some data to define a VectorStore object
        field: An optional field to remove from the vector_store_data
        expected: The expected value of the field
    """

    # Remove an optional field
    del vector_store_config_data[field]

    # Try to instantiate a VectorStore object with a missing optional field
    vector_store = VectorStoreConfig(**vector_store_config_data)

    assert vector_store.model_dump()[field] == expected
