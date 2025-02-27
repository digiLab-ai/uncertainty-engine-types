import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Graph, NodeElement


def test_graph(graph_data: dict):
    """
    Basic test that Graph model is working as expected.

    Args:
        graph_data: Some data to define a Graph object
    """

    # Instantiate a Graph object
    graph = Graph(**graph_data)

    assert graph.model_dump() == graph_data


def test_graph_raise_missing(graph_data: dict):
    """
    Test that Graph model raises an error when missing a required field.

    Args:
        graph_data: Some data to define a Graph object
    """

    # Remove a required field
    del graph_data["nodes"]

    # Try to instantiate a Graph object with a missing required field
    with pytest.raises(ValidationError):
        Graph(**graph_data)


def test_node_element(node_element_data: dict):
    """
    Basic test that NodeElement model is working as expected.

    Args:
        node_element_data: Some data to define a NodeElement object
    """

    # Instantiate a NodeElement object
    node_element = NodeElement(**node_element_data)

    assert node_element.model_dump() == node_element_data


def test_node_element_raise_missing(node_element_data: dict):
    """
    Test that NodeElement model raises an error when missing a required field.

    Args:
        node_element_data: Some data to define a NodeElement object
    """

    # Remove a required field
    del node_element_data["type"]

    # Try to instantiate a NodeElement object with a missing required field
    with pytest.raises(ValidationError):
        NodeElement(**node_element_data)


def test_node_element_optional(node_element_data: dict):
    """
    Test that NodeElement model does not raise an error when missing an optional field.

    Args:
        node_element_data: Some data to define a NodeElement object
    """

    # Remove an optional field
    del node_element_data["inputs"]

    # Try to instantiate a NodeElement object with a missing optional field
    node_element = NodeElement(**node_element_data)

    assert node_element.model_dump()["inputs"] == {}
