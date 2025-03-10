from typing import Optional, Union

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


@pytest.mark.parametrize(
    "field, expected",
    [
        ("train_test_ratio", 1.0),
        ("input_variance", None),
        ("output_variance", None),
        ("model_type", "SingleTaskGPTorch"),
        ("seed", None),
    ],
)
def test_model_config_optional(
    model_config_data: dict, field: str, expected: Optional[Union[float, str]]
):
    """
    Test that ModelConfig model does not raise an error when missing an optional field.

    Args:
        model_config_data: Some data to define a ModelConfig object
        field: An optional field to remove from the model_config_data
    """

    # Remove an optional field
    del model_config_data[field]

    # Try to instantiate a ModelConfig object with a missing optional field
    model_config = ModelConfig(**model_config_data)

    assert model_config.model_dump()[field] == expected


@pytest.mark.parametrize(
    "field, invalid",
    [
        ("train_test_ratio", "invalid"),
        ("input_variance", "invalid"),
        ("output_variance", "invalid"),
        ("model_type", 0.0),
        ("seed", "invalid"),
    ],
)
def test_model_config_raise_invalid_model_type(
    model_config_data: dict, field: str, invalid: Optional[Union[float, str]]
):
    """
    Test that ModelConfig object raises an error when the model_type field is invalid.

    Args:
        model_config_data: Some data to define a ModelConfig object
    """

    # Change the model_type field to an invalid value
    model_config_data[field] = invalid

    # Try to instantiate a ModelConfig object with an invalid role field
    with pytest.raises(ValidationError):
        ModelConfig(**model_config_data)
