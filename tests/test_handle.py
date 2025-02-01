import pytest

from workflow_types import Handle


def test_handle():
    """
    Basic test that Handle class is working as expected
    """

    # Define some arbitrary handle string
    handle_str = "node.handle"

    # Create a Handle object from the handle string
    handle = Handle(handle_str)

    # Check that the node_name and node_handle attributes are as expected
    assert handle.node_name == "node"
    assert handle.node_handle == "handle"
    assert handle.model_dump() == {"node_name": "node", "node_handle": "handle"}


def test_handle_invalid_extra():
    """
    Test that a handle string with extra dots raises a ValueError
    """

    # Define an invalid handle string
    handle_str = "node.handle.extra"

    # Check that creating a Handle object from the invalid handle string raises a ValueError
    with pytest.raises(ValueError):
        Handle(handle_str)


def test_handle_invalid_missing():
    """
    Test that a handle string with missing dots raises a ValueError
    """

    # Define an invalid handle string
    handle_str = "nodehandle"

    # Check that creating a Handle object from the invalid handle string raises a ValueError
    with pytest.raises(ValueError):
        Handle(handle_str)
