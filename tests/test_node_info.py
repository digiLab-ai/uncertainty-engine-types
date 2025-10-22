from typing import Any, Optional
from uuid import uuid4

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import (
    NodeInfo,
    NodeInputInfo,
    NodeOutputInfo,
    NodeRequirementsInfo,
    ScalingInfo,
)
from uncertainty_engine_types.version import __version__


def test_node_input_info_model(node_input_info_data: dict):
    """
    Basic test that NodeInputInfo model is working as expected.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
    """

    # Instantiate a NodeInputInfo object
    node_input_info = NodeInputInfo(**node_input_info_data)

    assert node_input_info.model_dump() == node_input_info_data


@pytest.mark.parametrize("field", ["type", "label", "description"])
def test_node_input_info_raise_missing(node_input_info_data: dict, field: str):
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


def test_node_info_allows_extras(node_info_data: dict[str, Any]) -> None:
    """
    Adds an unexpected key to a serialised `NodeInfo` and expects the key to be
    present in the deserialised model.
    """

    node_info_data[str(uuid4())] = "foo"
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
        ("queue_name", None),
        ("queue_url", None),
        ("service_arn", None),
        ("cache_url", None),
        ("requirements", None),
        ("scaling", ScalingInfo().model_dump()),
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


def test_node_requirements_info(node_requirements_info_data: dict):
    """
    Basic test that NodeRequirementsInfo model is working as expected.

    Args:
        node_requirements_info_data: Some data to define a NodeRequirementsInfo object
    """

    # Instantiate a NodeRequirementsInfo object
    node_requirements_info = NodeRequirementsInfo(**node_requirements_info_data)

    assert node_requirements_info.model_dump() == node_requirements_info_data


@pytest.mark.parametrize("field", ["cpu", "gpu", "memory", "timeout"])
def test_node_requirements_info_raise_missing(
    node_requirements_info_data: dict, field: str
):
    """
    Test that NodeRequirementsInfo object raises an error when missing a required field.

    Args:
        node_requirements_info_data: Some data to define a NodeRequirementsInfo object
        field: A field to remove from the node_requirements_info_data
    """

    # Remove a required field
    del node_requirements_info_data[field]

    # Try to instantiate a NodeRequirementsInfo object with a missing required field
    with pytest.raises(ValidationError):
        NodeRequirementsInfo(**node_requirements_info_data)


def test_scaling_info(scaling_info_data: dict[str, int]) -> None:
    """
    Assert that a fully-populated `ScalingInfo` can be initialised.
    """
    scaling_info = ScalingInfo(**scaling_info_data)
    assert scaling_info.model_dump() == scaling_info_data


@pytest.mark.parametrize(
    "field, expected",
    [
        ("max", 1),
        ("min", 0),
    ],
)
def test_scaling_info_optional(
    scaling_info_data: dict[str, int],
    field: str,
    expected: int,
) -> None:
    """
    Assert that `ScalingInfo` returns the expected default values when
    initialised with missing values.
    """
    del scaling_info_data[field]
    scaling_info = ScalingInfo(**scaling_info_data)
    assert scaling_info.model_dump()[field] == expected
