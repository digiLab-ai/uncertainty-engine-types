from datetime import datetime
from typing import Dict, Literal, Sequence, Union

from pydantic import BaseModel, model_validator


Value = Union[str, float, int]
StructuredOutput = Dict[str, Union[Value, Sequence[Value], Dict[str, Value]]]


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: Union[str, StructuredOutput]
    timestamp: datetime

    @model_validator(mode="before")
    @classmethod
    def validate(cls, values: Dict) -> Dict:
        role = values.get("role")
        content = values.get("content")

        if role in ["instruction", "user"]:
            if not isinstance(content, str):
                raise ValueError(f"Content must be a string when role is {role}")
        elif role == "engine":
            if not isinstance(content, StructuredOutput):
                raise ValueError(
                    "Content must be a structured output when role is engine"
                )
        return values
