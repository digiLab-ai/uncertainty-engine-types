from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class TextEmbeddingsProvider(StrEnum):
    OPENAI = "openai"
    OLLAMA = "ollama"


class TextEmbeddingsConfig(BaseModel):
    """
    Connection configuration for text embedding models.
    """

    provider: str
    model: str
    ollama_url: Optional[str] = None
    openai_api_key: Optional[str] = None
