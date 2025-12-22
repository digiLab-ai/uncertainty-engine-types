import pytest

from uncertainty_engine_types import ToolMetadata


def test_tool_metadata_empty_by_default(tool_metadata_empty: ToolMetadata) -> None:
    """
    Test ToolMetadata is empty when instantiated with no args
    """
    assert tool_metadata_empty.is_empty()
    assert tool_metadata_empty.inputs == {}
    assert tool_metadata_empty.outputs == {}


def test_tool_metadata_is_empty_with_data(tool_metadata_complete: ToolMetadata) -> None:
    """
    Test ToolMetadata is not empty when given input and output args
    """
    assert not tool_metadata_complete.is_empty()


def test_tool_metadata_has_partial_data_only_inputs(
    tool_metadata_only_inputs: ToolMetadata,
) -> None:
    """
    Test has_partial_data returns True when ToolMetadata instantiated with only inputs
    """
    assert tool_metadata_only_inputs.has_partial_data()


def test_tool_metadata_has_partial_data_only_outputs(
    tool_metadata_only_outputs: ToolMetadata,
) -> None:
    """
    Test has_partial_data returns True when ToolMetadata instantiated with only outputs
    """
    assert tool_metadata_only_outputs.has_partial_data()


def test_tool_metadata_has_partial_data_both_defined(
    tool_metadata_complete: ToolMetadata,
) -> None:
    """
    Test has_partial_data returns False when ToolMetadata instantiated with inputs and outputs
    """
    assert not tool_metadata_complete.has_partial_data()


def test_tool_metadata_has_partial_data_empty(
    tool_metadata_empty: ToolMetadata,
) -> None:
    """
    Test has_partial_data returns False when ToolMetadata instantiated with no inputs or outputs
    """
    assert not tool_metadata_empty.has_partial_data()


def test_validate_complete_success(tool_metadata_complete: ToolMetadata) -> None:
    """
    Test validate_complete does not raise when ToolMetadata is complete
    """
    tool_metadata_complete.validate_complete()


def test_validate_complete_empty(tool_metadata_empty: ToolMetadata) -> None:
    """
    Test validate_complete does not raise when ToolMetadata is empty
    """
    tool_metadata_empty.validate_complete()


def test_validate_complete_only_inputs_raises(
    tool_metadata_only_inputs: ToolMetadata,
) -> None:
    """
    Test validate_complete raises ValueError when not complete
    """
    with pytest.raises(
        ValueError, match="Tool metadata must have both inputs AND outputs defined"
    ):
        tool_metadata_only_inputs.validate_complete()


def test_validate_complete_only_outputs_raises(
    tool_metadata_only_outputs: ToolMetadata,
) -> None:
    """
    Test validate_complete raises ValueError when not complete
    """
    with pytest.raises(
        ValueError, match="Tool metadata must have both inputs AND outputs defined"
    ):
        tool_metadata_only_outputs.validate_complete()
