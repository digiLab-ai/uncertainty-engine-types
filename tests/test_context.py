import pytest
from pydantic import ValidationError

from uncertainty_engine_types import Context


def test_context(context_data):
    """
    Basic test that Handle class is working as expected
    """

    # Instantiate a Context object
    context = Context(**context_data)

    assert context.model_dump() == context_data


@pytest.mark.parametrize(
    "field", ["sync", "job_id", "queue_url", "cache_url", "timeout", "nodes"]
)
def test_context_raise_missing(context_data, field):
    """
    Test that Context object raises an error when missing a required field
    """

    # Remove a required field
    del context_data[field]

    # Try to instantiate a Context object with a missing required field
    with pytest.raises(ValidationError):
        Context(**context_data)
