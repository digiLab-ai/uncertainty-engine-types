from typing import Any

import pytest
from pydantic import ValidationError

from uncertainty_engine_types import OverrideWorkflowInput


def test_override_workflow_input(override_workflow_input_data: dict[str, Any]):
    """
    Basic test that OverrideWorkflowInput is working as expected

    Args:
        override_workflow_input_data: data to define a OverrideWorkflowInput
            object
    """

    override_workflow_input = OverrideWorkflowInput(**override_workflow_input_data)

    assert override_workflow_input.model_dump() == override_workflow_input_data


@pytest.mark.parametrize("field", ["node_label", "input_handle", "value"])
def test_override_workflow_input_raise_missing(
    override_workflow_input_data: dict[str, Any], field: str
):
    """
    Test that OverrideWorkflowInput object raises an error when
    missing a required field.

    Args:
        override_workflow_input_data: data to define a OverrideWorkflowInput
            object
        field: A field to remove from the override_workflow_input_data
    """

    # Remove a required field
    del override_workflow_input_data[field]

    # Try to instantiate a Message object with a missing required field
    with pytest.raises(ValidationError):
        OverrideWorkflowInput(**override_workflow_input_data)
