import pytest
from pydantic import ValidationError

from uncertainty_engine_types.node_query import NodeQuery, NodeQueryRequest


def test_node_query_str():
    node_query = NodeQuery(node_id="abc123", version="1.0.0")
    assert str(node_query) == "abc123@1.0.0"
    node_query2 = NodeQuery(node_id="abc123", version=42)
    assert str(node_query2) == "abc123@42"


def test_node_query_fields():
    node_query = NodeQuery(node_id="nodeX", version=2)
    assert node_query.node_id == "nodeX"
    assert node_query.version == 2
    node_query2 = NodeQuery(node_id="nodeY", version="v3")
    assert node_query2.version == "v3"


def test_node_query_version_type():
    # Accepts both str and int
    NodeQuery(node_id="n", version="v1")
    NodeQuery(node_id="n", version=1)
    with pytest.raises(ValidationError):
        NodeQuery(node_id="n", version=None)


def test_node_query_validation():
    with pytest.raises(ValidationError):
        NodeQuery(node_id=None, version="1.0.0")
    with pytest.raises(ValidationError):
        NodeQuery(node_id="abc", version=None)


def test_node_query_request():
    nodes = [
        NodeQuery(node_id="n1", version="v1"),
        NodeQuery(node_id="n2", version=2),
    ]
    node_query_request = NodeQueryRequest(nodes=nodes)
    assert len(node_query_request.nodes) == 2
    assert node_query_request.nodes[0].node_id == "n1"
    assert node_query_request.nodes[1].version == 2


def test_node_query_request_empty():
    node_query_request = NodeQueryRequest(nodes=[])
    assert node_query_request.nodes == []
