import pytest
from pydantic import ValidationError
from uncertainty_engine_types import JobInfo


def test_job_info(job_info_data: dict):
    """
    Basic test that JobInfo model is working as expected.

    Args:
        job_info_data: Some data to define a JobInfo object
    """

    # Instantiate a JobInfo object
    job_info = JobInfo(**job_info_data)

    assert job_info.model_dump() == job_info_data


@pytest.mark.parametrize("field", ["status", "inputs"])
def test_job_info_raise_missing(job_info_data: dict, field: str):
    """
    Test that JobInfo model raises an error when missing a required field.

    Args:
        job_info_data: Some data to define a JobInfo object
        field: A required field to remove
    """

    # Remove a required field
    del job_info_data[field]

    # Try to instantiate a JobInfo object with a missing required field
    with pytest.raises(ValidationError):
        JobInfo(**job_info_data)


@pytest.mark.parametrize("field", ["message", "outputs"])
def test_job_info_optional(job_info_data: dict, field: str):
    """
    Test that JobInfo model does not raise an error when missing an optional field.

    Args:
        job_info_data: Some data to define a JobInfo object
    """

    # Remove an optional field
    del job_info_data[field]

    # Try to instantiate a JobInfo object with a missing optional field
    job_info = JobInfo(**job_info_data)

    assert job_info.model_dump()[field] is None
