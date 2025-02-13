from datetime import datetime
from typing import Union

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: Union[str, dict]
    timestamp: datetime
