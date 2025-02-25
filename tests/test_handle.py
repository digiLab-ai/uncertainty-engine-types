import pytest

from uncertainty_engine_types import Handle


def test_handle(handle_data: dict):
    """
    Basic test that Handle class is working as expected.
    """

    # Define some arbitrary handle string
    handle_str = f"{handle_data["node_name"]}.{handle_data["node_handle"]}"

    # Create a Handle object from the handle string
    handle = Handle(handle_str)

    # Check that the node_name and node_handle attributes are as expected
    assert handle.node_name == handle_data["node_name"]
    assert handle.node_handle == handle_data["node_handle"]
    assert handle.model_dump() == handle_data


def test_handle_invalid_extra():
    """
    Test that a handle string with extra dots raises a ValueError.
    """

    # Define an invalid handle string
    handle_str = "node.handle.extra"

    # Check that creating a Handle object from the invalid handle string raises a ValueError
    with pytest.raises(ValueError):
        Handle(handle_str)


def test_handle_invalid_missing():
    """
    Test that a handle string with missing dots raises a ValueError.
    """

    # Define an invalid handle string
    handle_str = "nodehandle"

    # Check that creating a Handle object from the invalid handle string raises a ValueError
    with pytest.raises(ValueError):
        Handle(handle_str)


def test_handle_split_init(handle_data: dict):
    """
    Test that a Handle object can be created from a dictionary.
    """

    # Create a Handle object from the handle data dictionary
    handle = Handle(**handle_data)

    assert handle.model_dump() == handle_data


@pytest.mark.parametrize("field", ["node_name", "node_handle"])
def test_handle_raise_missing(handle_data: dict, field: str):
    """
    Test that Context object raises an error when missing a required field.
    """

    # Define an invalid handle string
    del handle_data[field]

    # Check that creating a Handle object from the invalid handle string raises a ValueError
    with pytest.raises(ValueError):
        Handle(**handle_data)
