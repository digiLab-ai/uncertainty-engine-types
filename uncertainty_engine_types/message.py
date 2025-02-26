from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    role: Literal["instruction", "user", "engine"]
    content: str
    timestamp: datetime
