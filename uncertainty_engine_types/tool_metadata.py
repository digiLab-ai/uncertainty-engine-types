from pydantic import BaseModel, Field

from uncertainty_engine_types import NodeInputInfo, NodeOutputInfo

NodeId = str
"""Unique ID of a Uncertainty Engine node. Eg `label` field in the SDK"""
HandleLabel = str
"""Unique ID of a handle to a given node. Eg `input_variance`"""


class ToolMetadata(BaseModel):
    """Tool metadata."""

    inputs: dict[NodeId, dict[HandleLabel, NodeInputInfo]] = Field(default_factory=dict)
    """Defines which inputs on a workflow can be used as Tool Inputs"""
    outputs: dict[NodeId, dict[HandleLabel, NodeOutputInfo]] = Field(
        default_factory=dict
    )
    """Defines which outputs on a workflow can be used as Tool outputs"""

    def is_empty(self) -> bool:
        """Check if the metadata is completely empty"""
        return not self.inputs and not self.outputs

    def has_partial_data(self) -> bool:
        """Check if only inputs or only outputs are defined"""
        return bool(self.inputs) != bool(self.outputs)

    def validate_complete(self) -> None:
        """
        Validate that tool metadata is complete (has both inputs and outputs).

        Raises:
            ValueError: If metadata has only inputs or only outputs
        """
        if self.has_partial_data():
            raise ValueError(
                "Tool metadata must have both inputs AND outputs defined. "
                f"Currently has: inputs={'yes' if self.inputs else 'no'}, "
                f"outputs={'yes' if self.outputs else 'no'}"
            )
