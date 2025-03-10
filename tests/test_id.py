import pytest
from pydantic import ValidationError

from uncertainty_engine_types import ResourceID


def test_resource_id(resource_id_data: dict):
    """
    Basic test that ResourceID model is working as expected.

    Args:
        resource_id_data: Some data to define a ResourceID object
    """

    # Instantiate a ResourceID object
    resource_id = ResourceID(**resource_id_data)

    assert resource_id.model_dump() == resource_id_data


def test_resource_id_raise_missing(resource_id_data: dict):
    """
    Test that ResourceID object raises an error when missing a required field.

    Args:
        resource_id_data: Some data to define a ResourceID object
    """

    # Remove a required field
    del resource_id_data["id"]

    # Try to instantiate a ResourceID object with a missing required field
    with pytest.raises(ValidationError):
        ResourceID(**resource_id_data)
