from typing import Any, Optional

from pydantic import BaseModel

from .token import Token


class NodeInputInfo(BaseModel):
    type: str
    label: str
    description: str
    required: bool
    default: Optional[Any] = None


class NodeOutputInfo(BaseModel):
    type: str
    label: str
    description: str


class NodeInfo(BaseModel):
    type: str  # The class of the node
    category: str  # The categories joined by a period
    cost: int  # The cost of the node
    token: Token  # The token type of the node
    short_description: str  # Comes from the class docstring
    long_description: str  # Comes from the run method docstring
    inputs: dict[str, NodeInputInfo]
    outputs: dict[str, NodeOutputInfo]
