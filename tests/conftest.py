from datetime import datetime
from typing import Any

import pytest
from pytest import FixtureRequest

from uncertainty_engine_types import JobStatus, SQLKind, TextEmbeddingsProvider


@pytest.fixture
def node_id() -> str:
    """
    A node id.
    """

    return "node_id"


@pytest.fixture
def node_input_info_data() -> dict:
    """
    Some data to define a NodeInputInfo object.
    """

    return {
        "type": "type",
        "label": "label",
        "description": "description",
        "required": True,
        "set_in_node": True,
        "default": None,
    }


@pytest.fixture
def node_output_info_data() -> dict:
    """
    Some data to define a NodeOutputInfo object.
    """

    return {
        "type": "type",
        "label": "label",
        "description": "description",
    }


@pytest.fixture
def node_requirements_info_data() -> dict:
    """
    Some data to define a NodeRequirementsInfo object.
    """

    return {"cpu": 256, "gpu": True, "memory": 512, "timeout": 60}


@pytest.fixture
def node_info_data(
    node_input_info_data: dict,
    node_output_info_data: dict,
    node_id: str,
    node_requirements_info_data: dict,
) -> dict[str, Any]:
    """
    Some data to define a NodeInfo object.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
        node_output_info_data: Some data to define a NodeOutputInfo object
        node_id: A node id
        node_requirements_info_data: Some data to define a NodeRequirementsInfo object
    """

    return {
        "id": node_id,
        "label": "label",
        "category": "category",
        "description": "description",
        "long_description": "long_description",
        "image_name": "image_name",
        "cost": 10,
        "inputs": {"input_1": node_input_info_data},
        "outputs": {"output_1": node_output_info_data},
        "requirements": node_requirements_info_data,
        "load_balancer_url": "load_balancer_url",
        "queue_url": "queue_url",
        "cache_url": "cache_url",
        "version_types_lib": "version_types_lib",
        "version_base_image": 1,
        "version_node": 1,
    }


@pytest.fixture
def context_data(node_info_data: dict) -> dict:
    """
    Data to define a Context object.

    Args:
        node_info_data: Some data to define a NodeInfo object
    """

    return {
        "sync": True,
        "job_id": "job_id",
        "queue_url": "queue_url",
        "cache_url": "cache_url",
        "nodes": {"node_1": node_info_data},
        "timeout": 60,
        "user": {
            "email": "mr.pinecones@digilab.ai",
            "project_id": "9hd239n8nd7923j08j",
            "cost_code": "This is a cost code",
        },
    }


@pytest.fixture
def role_field(request: FixtureRequest) -> str:
    """
    Indirect fixture to parametrize the role field

    Args:
        request: The request object
    """

    return getattr(request, "param", "user")


@pytest.fixture
def message_data(role_field: str) -> dict:
    """
    Data to define a Message object.
    """

    return {
        "role": role_field,
        "content": "content",
        "timestamp": datetime(year=2025, month=2, day=25),
    }


@pytest.fixture
def chat_history_data(message_data: dict) -> dict:
    """
    Data to define a ChatHistory object.

    Args:
        message_data: Some data to define a Message object
    """

    return {"messages": [message_data]}


@pytest.fixture
def embeddings_provider_field(request: FixtureRequest) -> str:
    """
    Indirect fixture to parametrize the provider field

    Args:
        request: The request object
    """

    return getattr(request, "param", TextEmbeddingsProvider.OPENAI.value)


@pytest.fixture
def text_embeddings_config_data(embeddings_provider_field: str) -> dict:
    """
    Data to define a TextEmbeddingsConfig object

    Args:
        provider_field: The provider field
    """

    return {
        "provider": embeddings_provider_field,
        "model": "model",
        "ollama_url": "ollama_url",
        "openai_api_key": "openai_api_key",
    }


@pytest.fixture
def s3_storage_data() -> dict:
    """
    Data to define a S3Storage object.
    """

    return {"bucket": "bucket", "key": "key"}


@pytest.fixture
def local_storage_data() -> dict:
    """
    Data to define a LocalStorage object.
    """

    return {"path": "path"}


@pytest.fixture
def sql_table_data() -> dict:
    """
    Data to define a SQLTable object.
    """

    return {"url": "url", "query": "query"}


@pytest.fixture
def web_page_data() -> dict:
    """
    Data to define a WebPage object.
    """

    return {"url": "url"}


@pytest.fixture
def handle_data() -> dict:
    """
    Data to define a Handle object.
    """

    return {"node_name": "node_name", "node_handle": "node_handle"}


@pytest.fixture
def node_element_data(handle_data: dict, node_id: str) -> dict:
    """
    Data to define a NodeElement object.

    Args:
        handle_data: Some data to define a Handle object
        node_id: A node id
    """

    return {
        "type": "type",  # I'm pretty sure the node_id is now used as the node type
        "inputs": {"target_handle": handle_data},
    }


@pytest.fixture
def graph_data(node_element_data: dict) -> dict:
    """
    Data to define a Graph object.

    Args:
        node_element_data: Some data to define a NodeElement object
    """

    return {"nodes": {"node_name": node_element_data}}


@pytest.fixture
def job_info_data() -> dict:
    """
    Data to define a JobInfo object.
    """

    return {
        "status": JobStatus.COMPLETED,
        "message": "message",
        "inputs": {"input_1": "input_1"},
        "outputs": {"output_1": "output_1"},
        "progress": None,
    }


@pytest.fixture
def llm_provider_field(request: FixtureRequest) -> str:
    """
    Indirect fixture to parametrize the provider field

    Args:
        request: The request object
    """

    return getattr(request, "param", TextEmbeddingsProvider.OPENAI.value)


@pytest.fixture
def llm_config_data(llm_provider_field: str) -> dict:
    """
    Data to define a LLMConfig object

    Args:
        provider_field: The provider field
    """

    return {
        "provider": llm_provider_field,
        "model": "model",
        "temperature": 0.0,
        "ollama_url": "ollama_url",
        "openai_api_key": "openai_api_key",
    }


@pytest.fixture
def machine_learning_model_data() -> dict:
    """
    Some data to define a MachineLearningModel object.
    """

    return {
        "model_type": "model_type",
        "config": {"config": "config"},
        "metadata": {"metadata": "metadata"},
    }


@pytest.fixture
def sensor_designer_data() -> dict:
    """
    Some data to define a SensorDesigner object.
    """

    return {"bed": {"bed": "bed"}}


@pytest.fixture
def sql_config_data() -> dict:
    """
    Some data to define a SQLConfig object.
    """

    return {
        "kind": SQLKind.POSTGRES,
        "host": "host",
        "username": "username",
        "password": "password",
        "port": 5432,
        "database": "database",
    }


@pytest.fixture
def vector_store_config_data() -> dict:
    """
    Some data to define a VectorStoreConfig object.
    """

    return {
        "provider": "provider",
        "host": "host",
        "port": "port",
        "collection": "collection",
        "embedding_type": "embedding_type",
        "embedding_model": "embedding_model",
        "embedding_api_key": "embedding_api_key",
    }


@pytest.fixture
def model_config_data() -> dict:
    """
    Some data to define a ModelConfig object.
    """

    return {
        "input_variance": 0.1,
        "input_retained_dimensions": 1,
        "output_variance": 0.1,
        "output_retained_dimensions": 1,
        "model_type": "SingleTaskGPTorch",
        "warp_inputs": True,
        "kernel": "kernel",
        "seed": 42,
    }


@pytest.fixture
def resource_id_data() -> dict:
    """
    Some data to define a ResourceID object.
    """

    return {"id": "id"}


@pytest.fixture
def prompt_data() -> dict:
    """
    Some data to define a Prompt object.
    """

    return {"prompt": "prompt"}


@pytest.fixture
def uncertainty_plot_data() -> dict:
    """
    Some data to define an UncertaintyPlot object.
    """

    return {
        "x_label": "X",
        "y_label": "y",
        "x_vals": [1, 2, 3],
        "mean": [1, 4, 9],
        "std": [1, 1, 1],
        "lower": [0, 3, 8],
        "upper": [2, 5, 10],
    }
