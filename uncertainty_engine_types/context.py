from pydantic import BaseModel, ConfigDict

from uncertainty_engine_types.node_info import NodeInfo


class UserContext(BaseModel):
    email: str
    project_id: str
    cost_code: str
    user_id: str | None = None


class Context(BaseModel):
    """The context around an Uncertainty Engine node execution."""

    sync: bool
    """Whether to run the node synchronously."""

    job_id: str
    """The node execution job ID."""

    queue_url: str
    """The node queue URL."""

    cache_url: str
    """The node cache URL."""

    timeout: int
    """The node timeout in seconds."""

    nodes: dict[str, NodeInfo]
    """Dictionary of nodes and their runtime details."""

    user: UserContext
    """The context around the user executing the node."""

    is_root: bool = False
    """Indicates whether a node is the root node of a workflow."""

    model_config = ConfigDict(use_attribute_docstrings=True)
