from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, field_validator


class TextEmbeddingsProvider(StrEnum):
    OPENAI = "openai"
    OLLAMA = "ollama"


class TextEmbeddingsConfig(BaseModel):
    """
    Connection configuration for text embedding models.
    """

    provider: str
    model: Optional[str] = None
    ollama_url: Optional[str] = None
    openai_api_key: Optional[str] = None

    @field_validator("provider", mode="before")
    @classmethod
    def check_provider(cls, v, values):
        if v == TextEmbeddingsProvider.OLLAMA and not values.get("ollama_url"):
            raise ValueError("ollama_url must be provided for 'ollama' provider.")
        if v == TextEmbeddingsProvider.OPENAI and not values.get("openai_api_key"):
            raise ValueError("openai_api_key must be provided for 'openai' provider.")
        return v
