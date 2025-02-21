from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, field_validator


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

    @field_validator("ollama_url", "openai_api_key", mode="before")
    @classmethod
    def check_provider(cls, v, values, field):
        provider = values.get("provider")
        if v is None:
            if provider == LLMProvider.OLLAMA and field.name == "ollama_url":
                raise ValueError("ollama_url must be provided for 'ollama' provider.")
            if provider == LLMProvider.OPENAI and field.name == "openai_api_key":
                raise ValueError(
                    "openai_api_key must be provided for 'openai' provider."
                )
        return v
