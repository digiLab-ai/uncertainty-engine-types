from datetime import datetime
from typing import Dict, Literal, Sequence, Union

from pydantic import BaseModel


Value = Union[str, float, int]


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: Union[str, Dict[str, Union[Value, Sequence[Value]]]]
    timestamp: datetime
