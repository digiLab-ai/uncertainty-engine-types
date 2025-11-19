from typing import Any, Optional

from pydantic import BaseModel, ConfigDict

from .version import __version__


class NodeInputInfo(BaseModel):
    type: str
    label: str
    description: str
    required: bool = True
    set_in_node: bool = True
    default: Optional[Any] = None


class NodeOutputInfo(BaseModel):
    type: str
    label: str
    description: str


class NodeRequirementsInfo(BaseModel):
    cpu: int
    gpu: bool
    memory: int
    timeout: int


class ScalingInfo(BaseModel):
    """Scaling configuration."""

    model_config = ConfigDict(use_attribute_docstrings=True)

    max: int = 1
    """Maximum number of service tasks to scale out to."""

    min: int = 0
    """Minimum number of service tasks to scale in to."""


class NodeInfo(BaseModel, extra="allow"):
    """
    Node information.
    """

    # New properties must be added as optional. The Node Registry uses this
    # model and must support Nodes that don't provide a full set of details.
    #
    # Likewise, the `extra="allow"` argument allows the Node Registry to
    # deserialise `NodeInfo` models with properties added post-release.

    id: str
    label: str
    category: str
    description: str
    long_description: str
    image_name: str
    cost: int
    inputs: dict[str, NodeInputInfo]
    outputs: dict[str, NodeOutputInfo] = {}
    requirements: Optional[NodeRequirementsInfo] = None
    """
    Deployment requirements.
    """

    scaling: ScalingInfo = ScalingInfo()
    """Scaling configuration."""

    load_balancer_url: Optional[str] = None

    queue_name: Optional[str] = None
    """Name of the node's job queue."""

    queue_url: Optional[str] = None
    service_arn: Optional[str] = None
    """
    Service ARN.
    """

    cache_url: Optional[str] = None
    version_types_lib: str = __version__
    version_base_image: int
    version_node: int

    tags: list[str] = []
    """Tags associated with the node."""
