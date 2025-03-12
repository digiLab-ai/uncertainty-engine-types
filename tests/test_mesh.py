import pytest
from datetime import datetime
from unittest.mock import Mock

from uncertainty_engine_types import MeshFile, Mesh


def test_mesh_initialization():
    """Test that Mesh initializes correctly with required fields."""
    mock_file = Mock(spec=MeshFile)
    mesh = Mesh(
        created_by="user123",
        project_id="proj_001",
        name="TestMesh",
        version="1.0",
        nodes=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        elements=[("triangle", [[0, 1, 2]])],
        location=mock_file,
        element_type="triangle",
    )

    assert mesh.created_by == "user123"
    assert mesh.project_id == "proj_001"
    assert mesh.name == "TestMesh"
    assert mesh.version == "1.0"
    assert isinstance(mesh.date_created, datetime)
    assert isinstance(mesh.last_edited, datetime)
    assert mesh.nel == 1  # 1 element added
    assert mesh.nnodes == 2  # 2 nodes added


def test_mesh_defaults():
    """Test that Mesh defaults are correctly assigned."""
    mock_file = Mock(spec=MeshFile)
    mesh = Mesh(
        created_by="user123",
        project_id="proj_002",
        name="DefaultMesh",
        version="1.0",
        location=mock_file,
        element_type="quad",
    )

    assert mesh.nodes == []
    assert mesh.elements == []
    assert mesh.node_data == {}
    assert mesh.element_data == {}
    assert mesh.nel == 0
    assert mesh.nnodes == 0


def test_mesh_computed_fields():
    """Test that nel and nnodes are computed correctly."""
    mock_file = Mock(spec=MeshFile)
    mesh = Mesh(
        created_by="user123",
        project_id="proj_003",
        name="ComputedMesh",
        version="1.0",
        nodes=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]],
        elements=[("triangle", [[0, 1, 3], [1, 2, 3]])],
        location=mock_file,
        element_type="triangle",
    )

    assert mesh.nel == 2
    assert mesh.nnodes == 3


def test_mesh_invalid_nodes():
    """Test that an invalid node structure raises a validation error."""
    mock_file = Mock(spec=MeshFile)
    with pytest.raises(ValueError):
        Mesh(
            created_by="user123",
            project_id="proj_004",
            name="InvalidNodesMesh",
            version="1.0",
            nodes=[[0.0, 0.0], [1.0, 0.0]],  # Invalid: should be 3D coordinates
            location=mock_file,
            element_type="triangle",
        )


def test_mesh_invalid_elements():
    """Test that an invalid element structure raises a validation error."""
    mock_file = Mock(spec=MeshFile)
    with pytest.raises(ValueError):
        Mesh(
            created_by="user123",
            project_id="proj_005",
            name="InvalidElementsMesh",
            version="1.0",
            nodes=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
            elements=[("triangle", [[0, 1]])],  # Invalid: should have 3 indices
            location=mock_file,
            element_type="triangle",
        )
