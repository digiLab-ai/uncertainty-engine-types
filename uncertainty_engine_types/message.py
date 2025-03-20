from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, field_validator


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: str
    timestamp: datetime

    @field_validator("content", mode="before")
    @classmethod
    def convert_content_to_string(cls, value: Any) -> str:
        if isinstance(value, (str, int, float, bool)):
            return str(value)
        raise ValueError(
            f"Invalid type for content: {type(value).__name__}. Must be str, int, float, or bool."
        )
