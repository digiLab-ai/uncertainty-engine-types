import pytest
from pydantic import BaseModel, ValidationError

from uncertainty_engine_types.utils import format_pydantic_errors


def test_format_pydantic_errors():
    """
    Verify that the format_pydantic_errors function formats pydantic validation errors correctly
    """

    # Define a sample Pydantic model
    class SampleModel(BaseModel):
        name: str
        age: int

    # Create invalid data to trigger validation errors
    invalid_data = {"name": 123, "age": "twenty"}  # Wrong types

    # Try to create an instance of the model with invalid data
    with pytest.raises(ValidationError) as e:
        SampleModel(**invalid_data)

    # Format the error
    formatted_error = format_pydantic_errors(e.value)

    # Verify that the formatted error contains the expected messages
    assert "Error at 'name': Input should be a valid string" in formatted_error
    assert "Error at 'age': Input should be a valid integer" in formatted_error
