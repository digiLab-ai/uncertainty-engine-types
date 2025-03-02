from typing import Union, List, Tuple, Dict
from datetime import datetime

from pydantic import BaseModel, Field, model_validator

from file import MeshFile

DataType = Union[List[float], List[List[float]]]  # Scalars or Vectors


class Mesh(BaseModel):
    """
    Model representing a mesh with nodes, elements, and associated data
    Includes metadata about the mesh and its storage location
    """

    # Metadata
    created_by: str
    project_id: str
    date_created: datetime = Field(default_factory=datetime.now)
    last_edited: datetime = Field(default_factory=datetime.now)
    name: str
    version: str

    # Mesh data
    nodes: List[List[float]] = Field(default_factory=list)  # 3D coordinates of nodes
    elements: List[Tuple[str, List[List[int]]]] = Field(
        default_factory=list
    )  # Elements with type and connectivity
    node_data: Dict[str, DataType] = Field(
        default_factory=dict
    )  # Additional data associated with nodes
    element_data: Dict[str, List[List[List[int]]]] = Field(
        default_factory=dict
    )  # Additional data associated with elements

    # Storage info
    location: MeshFile

    # Element properties
    element_type: str
    nel: int = 0  # Number of elements (computed)
    nnodes: int = 0  # Number of nodes (computed)

    @model_validator(mode="after")
    def compute_derived_fields(self):
        """Automatically calculate number of elements and nodes after model initialization"""
        self.nel = len(self.elements)
        self.nnodes = len(self.nodes)
        return self
