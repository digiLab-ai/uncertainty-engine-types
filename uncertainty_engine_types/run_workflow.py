# Types for running a workflow via `run_workflow` or `queue_workflow` endpoints
from typing import Any, List, Optional

from pydantic import BaseModel


class OverrideWorkflowInput(BaseModel):
    node_label: str
    input_handle: str
    value: Any  # Required as any to allow for input to all nodes


class OverrideWorkflowOutput(BaseModel):
    node_label: str
    output_handle: str
    output_label: str


class RunWorkflowRequest(BaseModel):
    inputs: Optional[List[OverrideWorkflowInput]] = None
    outputs: Optional[List[OverrideWorkflowOutput]] = None
