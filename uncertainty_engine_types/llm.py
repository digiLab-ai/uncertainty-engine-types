from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LLMProvider(Enum):
    OPENAI = "openai"
    OLLAMA = "ollama"


class LLMConfig(BaseModel):
    """
    Connection manager for Language Learning Models (LLMs).
    """

    url: str
    provider: str
    model: str
    temperature: float = 0.0
    api_key: Optional[str] = None
