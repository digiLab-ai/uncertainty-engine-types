from pydantic import BaseModel


class NodeQueryInput(BaseModel):
    """
    Represents a query for a specific node and version.
    """

    node_id: str
    version: str

    def __str__(self):
        return f"{self.node_id}@{self.version}"


class NodeQueryListInput(BaseModel):
    """
    List of node queries for batch operations.
    """

    nodes: list[NodeQueryInput]
