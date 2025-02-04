from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Literal, List, Dict

from pydantic import BaseModel
from typeguard import typechecked


class VectorStoreProvider(Enum):
    WEAVIATE = "weaviate"


class VectorStoreConnection(ABC):
    @abstractmethod
    def ingest(self, texts, metadatas):
        pass

    @abstractmethod
    def retrieve(self, query, k):
        pass

    @abstractmethod
    def get_vector_store(self):
        pass

    @abstractmethod
    def close(self):
        pass


@typechecked
class WeaviateVectorStoreConnection(VectorStoreConnection):

    def __init__(
        self,
        host: str,
        port: str,
        collection: str,
        embedding_type: str,
        embedding_model: str,
        embedding_api_key: str,
    ):

        self.host = host
        self.port = port
        self.collection = collection
        self.embedding_type = embedding_type
        self.embedding_model = embedding_model
        self.embedding_api_key = embedding_api_key
        self.vector_store = get_persistent_vector_store(
            host, port, collection, embedding_type, embedding_model, embedding_api_key
        )

    def ingest(self, texts: List[str], metadatas: List[Dict]) -> List[str]:
        """
        Ingest a list of texts into the vector store.

        Args:
            texts (List[str]): The texts to ingest.
            metadatas (List[Dict]): The metadata associated with each text.

        Returns:
            List[str]: The IDs of the ingested texts.

        """

        return self.vector_store.add_texts(texts=texts, metadatas=metadatas)

    def retrieve(self, query: Optional[str], k: int) -> List[Dict]:
        """
        Retrieve the k most relevant documents to a query.

        Args:
            query (Optional[str]): The query to retrieve documents for.
            k (int): The number of documents to retrieve.

        Returns:
            List[str]: The IDs of the retrieved documents.

        """

        docs = self.vector_store.max_marginal_relevance_search(query=query, k=k)
        docs_list = [
            {"content": doc.page_content, "metadata": doc.metadata} for doc in docs
        ]
        return docs_list

    def get_vector_store(self):
        """
        Get the underlying vector store.

        Returns:
            LangcahinWeaviateVectorStore: The underlying vector store.

        """

        return self.vector_store

    def close(self):
        self.vector_store._client.close()


class VectorStoreManager(BaseModel):
    """
    Connection manager for a vector store.
    """

    provider: str
    host: str
    port: str = "8080"
    collection: str = "DefaultCollection"
    embedding_type: str
    embedding_model: str
    embedding_api_key: str

    @typechecked
    def connect(self) -> WeaviateVectorStoreConnection:
        """
        Connect to the vector store.

        Returns:
            VectorStoreConnection: The vector store connection.
        """

        match self.provider:
            case VectorStoreProvider.WEAVIATE.value:
                return WeaviateVectorStoreConnection(
                    host=self.host,
                    port=self.port,
                    collection=self.collection,
                    embedding_type=self.embedding_type,
                    embedding_model=self.embedding_model,
                    embedding_api_key=self.embedding_api_key,
                )
            case _:
                raise ValueError(f"Unknown vector store provider: {self.provider}")


@typechecked
def get_persistent_vector_store(
    host: str,
    port: str,
    collection: str,
    embedding_type: str,
    embedding_model: str,
    embedding_api_key: Optional[str] = None,
):
    """
    Get a database client connected to a deployed Weaviate vector store
    """

    from langchain_weaviate import WeaviateVectorStore
    from weaviate.connect import ConnectionParams
    import weaviate

    try:
        client = weaviate.WeaviateClient(
            connection_params=ConnectionParams.from_params(
                http_host=host,
                http_port=port,
                http_secure=False,
                grpc_host=host,
                grpc_port="50051",
                grpc_secure=False,
            ),
            skip_init_checks=True,
        )
        client.connect()
    except Exception as e:
        raise ValueError(f"Failed to connect to Weaviate: {e}")

    embedding_function = get_embedding_function(
        embedding_type, embedding_model, embedding_api_key
    )

    # check if a collection exists and makes one if it doesn't
    if not client.collections.exists(collection):
        client.collections.create(collection)

    try:
        vector_store = WeaviateVectorStore(
            client=client,
            index_name=collection,
            text_key="text",
            embedding=embedding_function,
        )
    except Exception as e:
        raise ValueError(f"Failed to initialize Weaviate vector store: {e}")

    return vector_store


@typechecked
def get_embedding_function(
    embedding_type: Literal["huggingface", "openai"],
    embedding_model: str,
    embedding_api_key: Optional[str] = None,
):
    """
    Get an embedding function based on the specified type and configuration.
    """

    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_openai import OpenAIEmbeddings

    match embedding_type:
        case "huggingface":
            try:
                return HuggingFaceEmbeddings(model_name=embedding_model)
            except Exception as e:
                raise ValueError(
                    f"Failed to initialize HuggingFace embedding model: {str(e)}"
                ) from e

        case "openai":
            if not embedding_api_key:
                raise ValueError("OpenAI embeddings require an API key")
            try:
                return OpenAIEmbeddings(
                    model=embedding_model, api_key=embedding_api_key
                )
            except Exception as e:
                raise ValueError(
                    f"Failed to initialize OpenAI embedding model: {str(e)}"
                ) from e

        case _:
            raise ValueError(
                f"Embedding type must be one of ['huggingface', 'openai']. Got {embedding_type}"
            )
