from datetime import datetime
from typing import Literal, Union

from pydantic import BaseModel, field_validator


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: str
    timestamp: datetime

    @field_validator("content", mode="before")
    @classmethod
    def convert_content_to_string(cls, value: Union[str, int, float, bool]) -> str:
        """Converts the content to a string if it is not already a string."""
        return str(value)
