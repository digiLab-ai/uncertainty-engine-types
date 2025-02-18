from enum import Enum

from pydantic import BaseModel


class VectorStoreProvider(Enum):
    WEAVIATE = "weaviate"


class VectorStoreConfig(BaseModel):
    """
    Connection configuration for a vector store.
    """

    provider: str
    host: str
    port: str = "8080"
    collection: str = "DefaultCollection"
    embedding_type: str
    embedding_model: str
    embedding_api_key: str
