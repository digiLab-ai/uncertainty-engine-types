from datetime import datetime

import pytest

from uncertainty_engine_types import TextEmbeddingsProvider


@pytest.fixture
def node_input_info_data():
    """
    Some data to define a NodeInputInfo object
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
def node_output_info_data():
    """
    Some data to define a NodeOutputInfo object
    """

    return {
        "type": "type",
        "label": "label",
        "description": "description",
    }


@pytest.fixture
def node_info_data(node_input_info_data, node_output_info_data):
    """
    Some data to define a NodeInfo object
    """

    return {
        "id": "id",
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
def context_data(node_info_data):
    """
    Data to define a Context object
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
def message_data():
    """
    Data to define a Message object
    """

    return {
        "role": "user",
        "content": "content",
        "timestamp": datetime(year=2025, month=2, day=25),
    }


@pytest.fixture
def conversation_data(message_data):
    """
    Data to define a Conversation object
    """

    return {"messages": [message_data]}


@pytest.fixture
def provider_field(request):
    """
    Indirect fixture to parametrize the provider field
    """

    return getattr(request, "param", TextEmbeddingsProvider.OPENAI.value)


@pytest.fixture
def text_embeddings_config_data(provider_field):
    """
    Data to define a TextEmbeddingsConfig object
    """

    return {
        "provider": provider_field,
        "model": "model",
        "ollama_url": "ollama_url",
        "openai_api_key": "openai_api_key",
    }
