from typing import Any, Optional

from pydantic import BaseModel

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

    load_balancer_url: Optional[str] = None
    queue_url: Optional[str] = None
    service_arn: Optional[str] = None
    """
    Service ARN.
    """

    cache_url: Optional[str] = None
    version_types_lib: str = __version__
    version_base_image: int
    version_node: int
