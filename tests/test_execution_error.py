import pytest

from uncertainty_engine_types import ExecutionError


def test_execution_error():
    with pytest.raises(ExecutionError) as e:
        raise ExecutionError("Test message")

    assert str(e.value) == "Test message"
    assert isinstance(e.value, ExecutionError)
