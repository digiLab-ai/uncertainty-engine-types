import pytest

from uncertainty_engine_types import NodeInputInfo, NodeOutputInfo, ToolMetadata


def test_tool_metadata_empty_by_default() -> None:
    """
    Test ToolMetadata is empty when instantiated with no args
    """
    metadata = ToolMetadata()

    assert metadata.is_empty()
    assert metadata.inputs == {}
    assert metadata.outputs == {}


def test_tool_metadata_is_empty_with_data(
    node_input_info_data: dict, node_output_info_data: dict
) -> None:
    """
    Test ToolMetadata is not empty when given input and output args
    """
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}},
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}},
    )
    assert not metadata.is_empty()


def test_tool_metadata_has_partial_data_only_inputs(node_input_info_data: dict) -> None:
    """
    Test has_partial_data returns True when ToolMetadata instantiated with only inputs
    """
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}}
    )
    assert metadata.has_partial_data()


def test_tool_metadata_has_partial_data_only_outputs(
    node_output_info_data: dict,
) -> None:
    """
    Test has_partial_data returns True when ToolMetadata instantiated with only outputs
    """
    metadata = ToolMetadata(
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}}
    )
    assert metadata.has_partial_data()


def test_tool_metadata_has_partial_data_both_defined(
    node_input_info_data: dict, node_output_info_data: dict
) -> None:
    """
    Test has_partial_data returns False when ToolMetadata instantiated with inputs and outputs
    """
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}},
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}},
    )
    assert not metadata.has_partial_data()


def test_tool_metadata_has_partial_data_empty() -> None:
    """
    Test has_partial_data returns False when ToolMetadata instantiated with no inputs or outputs
    """
    metadata = ToolMetadata()
    assert not metadata.has_partial_data()


def test_validate_complete_success(
    node_input_info_data: dict, node_output_info_data: dict
) -> None:
    """
    Test validate_complete does not raise when ToolMetadata is complete
    """
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}},
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}},
    )
    metadata.validate_complete()


def test_validate_complete_empty() -> None:
    """
    Test validate_complete does not raise when ToolMetadata is empty
    """
    metadata = ToolMetadata()
    metadata.validate_complete()


def test_validate_complete_only_inputs_raises(node_input_info_data: dict) -> None:
    """
    Test validate_complete raises ValueError when not complete
    """
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}}
    )
    with pytest.raises(
        ValueError, match="Tool metadata must have both inputs AND outputs defined"
    ):
        metadata.validate_complete()


def test_validate_complete_only_outputs_raises(node_output_info_data: dict) -> None:
    """
    Test validate_complete raises ValueError when not complete
    """
    metadata = ToolMetadata(
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}}
    )
    with pytest.raises(
        ValueError, match="Tool metadata must have both inputs AND outputs defined"
    ):
        metadata.validate_complete()
