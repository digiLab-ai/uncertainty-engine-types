from typing import Union, List, Tuple, Dict
from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class S3Storage(BaseModel):
    bucket: str
    key: str


class LocalStorage(BaseModel):
    path: str


FileLocation = Union[S3Storage, LocalStorage]


class File(BaseModel):
    pass


class Document(File):
    location: FileLocation


class Image(File):
    location: FileLocation


class Mesh(File):
    """
    Model representing a mesh with nodes, elements, and associated data
    Includes metadata about the mesh and its storage location
    """

    DataType = Union[List[float], List[List[float]]]  # Scalars or Vectors

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
    location: FileLocation

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


class PDF(File):
    location: FileLocation


class SQLTable(File):
    url: str
    query: str


class TabularData(File):
    location: FileLocation


class WebPage(File):
    url: str
