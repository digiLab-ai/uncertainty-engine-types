import pytest
from pydantic import ValidationError

from uncertainty_engine_types import ModelConfig


def test_model_config(model_config_data: dict):
    """
    Basic test that ModelConfig model is working as expected.

    Args:
        model_config_data: Some data to define a ModelConfig object
    """

    # Instantiate a ModelConfig object
    model_config = ModelConfig(**model_config_data)

    assert model_config.model_dump() == model_config_data


def test_model_config_raise_invalid_role(model_config_data: dict):
    """
    Test that ModelConfig object raises an error when the role field is invalid.

    Args:
        model_config_data: Some data to define a ModelConfig object
    """

    # Change the role field to an invalid value
    model_config_data["model_type"] = "invalid"

    # Try to instantiate a ModelConfig object with an invalid role field
    with pytest.raises(ValidationError):
        ModelConfig(**model_config_data)
