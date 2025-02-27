import pytest
from pydantic import ValidationError

from uncertainty_engine_types import SensorDesigner


def test_sensor_designer(sensor_designer_data: dict):
    """
    Basic test that SensorDesigner model is working as expected.

    Args:
        sensor_designer_data: Some data to define a SensorDesigner object
    """

    # Instantiate a SensorDesigner object
    sensor_designer = SensorDesigner(**sensor_designer_data)

    assert sensor_designer.model_dump() == sensor_designer_data


def test_sensor_designer_raise_missing(sensor_designer_data: dict):
    """
    Test that SensorDesigner object raises an error when missing a required field.

    Args:
        sensor_designer_data: Some data to define a SensorDesigner object
    """

    # Remove a required field
    del sensor_designer_data["bed"]

    # Try to instantiate a SensorDesigner object with a missing required field
    with pytest.raises(ValidationError):
        SensorDesigner(**sensor_designer_data)
