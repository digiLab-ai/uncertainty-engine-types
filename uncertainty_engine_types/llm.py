from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, model_validator


class LLMProvider(StrEnum):
    OPENAI = "openai"
    OLLAMA = "ollama"


class LLMConfig(BaseModel):
    """
    Connection configuration for Language Learning Models (LLMs).
    """

    provider: str
    model: str
    temperature: float = 0.0
    ollama_url: Optional[str] = None
    openai_api_key: Optional[str] = None

    class LLMConfig(BaseModel):
        """
        Connection configuration for Language Learning Models (LLMs).
        """

        provider: str
        model: str
        temperature: float = 0.0
        ollama_url: Optional[str] = None
        openai_api_key: Optional[str] = None

        @model_validator(mode="before")
        @classmethod
        def check_provider(cls, values):
            provider = values.get("provider")
            if provider == LLMProvider.OLLAMA and not values.get("ollama_url"):
                raise ValueError("ollama_url must be provided for 'ollama' provider.")
            if provider == LLMProvider.OPENAI and not values.get("openai_api_key"):
                raise ValueError(
                    "openai_api_key must be provided for 'openai' provider."
                )
            return values
