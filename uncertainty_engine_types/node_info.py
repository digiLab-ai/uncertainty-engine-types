from typing import Any, Optional

from pydantic import BaseModel

from . import __version__


class Versions(BaseModel):
    base_image: str
    types_lib: str = __version__
    node: str


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


class NodeInfo(BaseModel):
    id: str
    label: str
    category: str
    description: str
    long_description: str
    image_name: str
    cost: int
    inputs: dict[str, NodeInputInfo]
    outputs: dict[str, NodeOutputInfo] = {}
    queue_url: Optional[str] = None
    cache_url: Optional[str] = None
    versions: Versions
