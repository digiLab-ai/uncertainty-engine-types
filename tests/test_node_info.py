from typing import Optional

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import NodeInfo, NodeInputInfo, NodeOutputInfo
from uncertainty_engine_types.version import __version__


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


def test_node_output_info(node_output_info_data: dict):
    """
    Basic test that NodeOutputInfo model is working as expected.

    Args:
        node_output_info_data: Some data to define a NodeOutputInfo object
    """

    # Instantiate a NodeOutputInfo object
    node_output_info = NodeOutputInfo(**node_output_info_data)

    assert node_output_info.model_dump() == node_output_info_data


@pytest.mark.parametrize("field", ["type", "label", "description"])
def test_node_output_info_raise_missing(node_output_info_data: dict, field: str):
    """
    Test that NodeOutputInfo object raises an error when missing a required field.

    Args:
        node_output_info_data: Some data to define a NodeOutputInfo object
        field: A field to remove from the node_output_info_data
    """

    # Remove a required field
    del node_output_info_data[field]

    # Try to instantiate a NodeOutputInfo object with a missing required field
    with pytest.raises(ValidationError):
        NodeOutputInfo(**node_output_info_data)


def test_node_info(node_info_data: dict):
    """
    Basic test that NodeInfo model is working as expected.

    Args:
        node_info_data: Some data to define a NodeInfo object
    """

    # Instantiate a NodeInfo object
    node_info = NodeInfo(**node_info_data)

    assert node_info.model_dump() == node_info_data


@pytest.mark.parametrize(
    "field",
    [
        "id",
        "label",
        "category",
        "description",
        "long_description",
        "image_name",
        "cost",
        "inputs",
        "version_base_image",
        "version_node",
    ],
)
def test_node_info_raise_missing(node_info_data: dict, field: str):
    """
    Test that NodeInfo object raises an error when missing a required field.

    Args:
        node_info_data: Some data to define a NodeInfo object
        field: A field to remove from the node_info_data
    """

    # Remove a required field
    del node_info_data[field]

    # Try to instantiate a NodeInfo object with a missing required field
    with pytest.raises(ValidationError):
        NodeInfo(**node_info_data)


@pytest.mark.parametrize(
    "field, expected",
    [
        ("outputs", {}),
        ("load_balancer_url", None),
        ("queue_url", None),
        ("cache_url", None),
        ("version_types_lib", __version__),
    ],
)
def test_node_info_optional(node_info_data: dict, field: str, expected):
    """
    Test that NodeInfo object does not raise an error when missing an optional field.

    Args:
        node_info_data: Some data to define a NodeInfo object
        field: An optional field to remove from the node_info_data
        expected: The expected value of the field
    """

    # Remove an optional field
    del node_info_data[field]

    # Try to instantiate a NodeInfo object with a missing optional field
    node_info = NodeInfo(**node_info_data)

    assert node_info.model_dump()[field] == expected
