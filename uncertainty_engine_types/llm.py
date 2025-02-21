from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, root_validator
from pydantic import field_validator


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

        @field_validator("provider", mode="before")
        @classmethod
        def check_provider(cls, v, values):
            if v == LLMProvider.OLLAMA and not values.get("ollama_url"):
                raise ValueError("ollama_url must be provided for 'ollama' provider.")
            if v == LLMProvider.OPENAI and not values.get("openai_api_key"):
                raise ValueError(
                    "openai_api_key must be provided for 'openai' provider."
                )
            return v
