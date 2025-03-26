from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, field_validator, Field


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)

    @field_validator("content", mode="before")
    @classmethod
    def convert_content_to_string(cls, value: Any) -> str:
        return str(value)
