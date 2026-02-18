from pydantic import BaseModel

from .handle import Handle


NodeId = str
TargetHandle = str
SourceHandle = str


class NodeElement(BaseModel):
    type: str
    inputs: dict[TargetHandle, Handle] = {}
    version: str | int | None = None


class Graph(BaseModel):
    nodes: dict[NodeId, NodeElement]
