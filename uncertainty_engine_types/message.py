from datetime import datetime
from typing import Dict, Literal, Sequence, Union

from pydantic import BaseModel


Value = str | float | int
StructuredOutputValue = Value | Sequence[Value]
StructuredOutput = dict[str, StructuredOutputValue]


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: StructuredOutput
    timestamp: datetime
