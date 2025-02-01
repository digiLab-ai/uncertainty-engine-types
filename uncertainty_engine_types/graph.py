from pydantic import BaseModel


NodeId = str
TargetHandle = str
SourceHandle = str


class NodeElement(BaseModel):
    type: str
    inputs: dict[TargetHandle, tuple[NodeId, SourceHandle]] = {}


class Graph(BaseModel):
    nodes: dict[NodeId, NodeElement]
