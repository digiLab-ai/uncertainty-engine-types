from enum import Enum
from typing import Optional

from pydantic import BaseModel, model_validator


class LLMProvider(Enum):
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

    @model_validator(mode="before")
    @classmethod
    def check_provider(cls, values):
        provider = values.get("provider")
        if provider == LLMProvider.OLLAMA.value and not values.get("ollama_url"):
            raise ValueError("ollama_url must be provided for 'ollama' provider.")
        if provider == LLMProvider.OPENAI.value and not values.get("openai_api_key"):
            raise ValueError("openai_api_key must be provided for 'openai' provider.")
        return values
