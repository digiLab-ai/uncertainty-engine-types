import pytest
from pydantic import ValidationError

from uncertainty_engine_types.node_query import NodeQueryInput, NodeQueryListInput


def test_node_query_input_str():
    input = NodeQueryInput(node_id="abc123", version="1.0.0")
    assert str(input) == "abc123@1.0.0"


def test_node_query_input_fields():
    input = NodeQueryInput(node_id="nodeX", version="2.1.3")
    assert input.node_id == "nodeX"
    assert input.version == "2.1.3"


def test_node_query_input_validation():
    with pytest.raises(ValidationError):
        NodeQueryInput(node_id=None, version="1.0.0")
    with pytest.raises(ValidationError):
        NodeQueryInput(node_id="abc", version=None)


def test_node_query_list_input():
    nodes = [
        NodeQueryInput(node_id="n1", version="v1"),
        NodeQueryInput(node_id="n2", version="v2"),
    ]
    input = NodeQueryListInput(nodes=nodes)
    assert len(input.nodes) == 2
    assert input.nodes[0].node_id == "n1"
    assert input.nodes[1].version == "v2"


def test_node_query_list_input_empty():
    input = NodeQueryListInput(nodes=[])
    assert input.nodes == []
