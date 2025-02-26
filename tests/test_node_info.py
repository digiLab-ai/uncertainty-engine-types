from typing import Optional

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import NodeInfo, NodeInputInfo, NodeOutputInfo


def test_machine_learning_model(node_input_info_data: dict):
    """
    Basic test that NodeInputInfo model is working as expected.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
    """

    # Instantiate a NodeInputInfo object
    machine_learning_model = NodeInputInfo(**node_input_info_data)

    assert machine_learning_model.model_dump() == node_input_info_data


@pytest.mark.parametrize("field", ["type", "label", "description"])
def test_machine_learning_model_raise_missing(node_input_info_data: dict, field: str):
    """
    Test that NodeInputInfo object raises an error when missing a required field.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
        field: A field to remove from the node_input_info_data
    """

    # Remove a required field
    del node_input_info_data[field]

    # Try to instantiate a NodeInputInfo object with a missing required field
    with pytest.raises(ValidationError):
        NodeInputInfo(**node_input_info_data)


@pytest.mark.parametrize(
    "field, expected", [("required", True), ("set_in_node", True), ("default", None)]
)
def test_node_input_info_optional(
    node_input_info_data: dict, field: str, expected: Optional[bool]
):
    """
    Test that NodeInputInfo object does not raise an error when missing an optional field.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
        field: An optional field to remove from the node_input_info_data
        expected: The expected value of the field
    """

    # Remove an optional field
    del node_input_info_data[field]

    # Try to instantiate a NodeInputInfo object with a missing optional field
    node_input_info = NodeInputInfo(**node_input_info_data)

    assert node_input_info.model_dump()[field] == expected
