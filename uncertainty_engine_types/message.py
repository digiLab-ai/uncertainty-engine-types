from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: dict[str, Any]
    timestamp: datetime
