from typing import Any, Optional

from pydantic import BaseModel


class NodeInputInfo(BaseModel):
    label: str
    type: str
    description: str
    required: bool = True
    set_in_node: bool = True
    default: Optional[Any] = None


class NodeOutputInfo(BaseModel):
    label: str
    type: str
    description: str


class NodeInfo(BaseModel):
    id: str
    version: int
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
