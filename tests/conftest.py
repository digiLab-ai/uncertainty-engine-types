from datetime import datetime

import pytest
from pytest import FixtureRequest

from uncertainty_engine_types import TextEmbeddingsProvider


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
def node_info_data(
    node_input_info_data: dict, node_output_info_data: dict, node_id: str
) -> dict:
    """
    Some data to define a NodeInfo object.

    Args:
        node_input_info_data: Some data to define a NodeInputInfo object
        node_output_info_data: Some data to define a NodeOutputInfo object
        node_id: A node id
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
        "timeout": 60,
        "nodes": {"node_1": node_info_data},
    }


@pytest.fixture
def message_data() -> dict:
    """
    Data to define a Message object.
    """

    return {
        "role": "user",
        "content": "content",
        "timestamp": datetime(year=2025, month=2, day=25),
    }


@pytest.fixture
def conversation_data(message_data: dict) -> dict:
    """
    Data to define a Conversation object.

    Args:
        message_data: Some data to define a Message object
    """

    return {"messages": [message_data]}


@pytest.fixture
def provider_field(request: FixtureRequest) -> str:
    """
    Indirect fixture to parametrize the provider field

    Args:
        request: The request object
    """

    return getattr(request, "param", TextEmbeddingsProvider.OPENAI.value)


@pytest.fixture
def text_embeddings_config_data(provider_field: str) -> dict:
    """
    Data to define a TextEmbeddingsConfig object

    Args:
        provider_field: The provider field
    """

    return {
        "provider": provider_field,
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
        "inputs": {"target_handle": handle_data}
    }


@pytest.fixture
def graph_data(node_element_data: dict) -> dict:
    """
    Data to define a Graph object.

    Args:
        node_element_data: Some data to define a NodeElement object
    """

    return {"nodes": {"node_name": node_element_data}}
