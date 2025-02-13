from datetime import datetime
from typing import Dict, Sequence, Union

from pydantic import BaseModel


Value = Union[str, float, int]


class Message(BaseModel):
    role: str
    content: Union[str, Dict[str, Union[Value, Sequence[Value]]]]
    timestamp: datetime
