import pytest
from pydantic import ValidationError

from uncertainty_engine_types import SQLConfig


def test_sql_config(sql_config_data: dict):
    """
    Basic test that SQLConfig model is working as expected.

    Args:
        sql_config_data: Some data to define a SQLConfig object
    """

    # Instantiate a SQLConfig object
    sql_config = SQLConfig(**sql_config_data)

    assert sql_config.model_dump() == sql_config_data


@pytest.mark.parametrize(
    "field", ["kind", "host", "username", "password", "port", "database"]
)
def test_sql_config_raise_missing(sql_config_data: dict, field: str):
    """
    Test that SQLConfig object raises an error when missing a required field.

    Args:
        sql_config_data: Some data to define a SQLConfig object
        field: A field to remove from the sql_config_data
    """

    # Remove a required field
    del sql_config_data[field]

    # Try to instantiate a SQLConfig object with a missing required field
    with pytest.raises(ValidationError):
        SQLConfig(**sql_config_data)
