from pydantic import BaseModel


class NodeQuery(BaseModel):
    """
    Represents a query for a specific node and version.
    """

    node_id: str
    version: str | int

    def __str__(self):
        return f"{self.node_id}@{self.version}"


class NodeQueryRequest(BaseModel):
    """
    Represents a request for querying specific node(s) and version(s).
    """

    nodes: list[NodeQuery]
