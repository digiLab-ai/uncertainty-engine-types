from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from typeguard import typechecked


@typechecked
class LLM(ABC):

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError("Temperature must be between 0.0 and 1.0")
        self._temperature = value

    @abstractmethod
    def get_langchain_llm(self, query: str) -> "LLM":
        """
        Return a BaseLLM object from Langchain according to the provider type.
        """
        pass

    def run_query(self, query: str) -> str:
        """
        Call the LLM with a query.
        """
        llm = self.get_langchain_llm()
        return llm.invoke(query).content


@typechecked
class OpenAILLM(LLM):

    def __init__(self, api_key: str, model: str, temperature: float = 0.0):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def get_langchain_llm(self):
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            api_key=self.api_key,
        )


@typechecked
class OllamaLLM(LLM):
    def __init__(self, url: str, model: str, temperature: float = 0.0):
        self.url = url
        self.model = model
        self.temperature = temperature

    def get_langchain_llm(self):
        from langchain_ollama import ChatOllama

        return ChatOllama(
            base_url=self.url,
            model=self.model,
            temperature=self.temperature,
        )


@typechecked
class LLMProvider(Enum):
    OPENAI = "openai"
    OLLAMA = "ollama"


@typechecked
class LLMManager(BaseModel):
    """
    Connection manager for Language Learning Models (LLMs).
    """

    url: str
    provider: str
    model: str
    temperature: float = 0.0
    api_key: Optional[str] = None

    def connect(self) -> LLM:
        """
        Connect to the LLM.
        """

        match self.provider:
            case LLMProvider.OPENAI.value:
                if self.api_key is None:
                    raise ValueError("API key is required for OpenAI LLM")
                return OpenAILLM(
                    api_key=self.api_key,
                    model=self.model,
                    temperature=self.temperature,
                )
            case LLMProvider.OLLAMA.value:
                return OllamaLLM(
                    url=self.url,
                    model=self.model,
                    temperature=self.temperature,
                )
            case _:
                raise ValueError(f"Unknown LLM provider: {self.provider}")
