import pytest
from pydantic import ValidationError

from uncertainty_engine_types import MachineLearningModel


def test_machine_learning_model(machine_learning_model_data: dict):
    """
    Basic test that MachineLearningModel model is working as expected.

    Args:
        machine_learning_model_data: Some data to define a MachineLearningModel object
    """

    # Instantiate a MachineLearningModel object
    machine_learning_model = MachineLearningModel(**machine_learning_model_data)

    assert machine_learning_model.model_dump() == machine_learning_model_data


@pytest.mark.parametrize("field", ["model_type", "config", "metadata"])
def test_machine_learning_model_raise_missing(machine_learning_model_data: dict, field: str):
    """
    Test that MachineLearningModel object raises an error when missing a required field.

    Args:
        machine_learning_model_data: Some data to define a MachineLearningModel object
        field: A field to remove from the machine_learning_model_data
    """

    # Remove a required field
    del machine_learning_model_data[field]

    # Try to instantiate a MachineLearningModel object with a missing required field
    with pytest.raises(ValidationError):
        MachineLearningModel(**machine_learning_model_data)
