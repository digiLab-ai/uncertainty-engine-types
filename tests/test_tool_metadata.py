from uncertainty_engine_types import NodeInputInfo, NodeOutputInfo, ToolMetadata


def test_tool_metadata_empty_by_default() -> None:
    metadata = ToolMetadata()

    assert metadata.is_empty()
    assert metadata.inputs == {}
    assert metadata.outputs == {}


def test_tool_metadata_is_empty_with_data(
    node_input_info_data: dict, node_output_info_data: dict
) -> None:
    metadata = ToolMetadata(
        inputs={"node1": {"handle1": NodeInputInfo(**node_input_info_data)}},
        outputs={"node1": {"handle1": NodeOutputInfo(**node_output_info_data)}},
    )
    assert not metadata.is_empty()
