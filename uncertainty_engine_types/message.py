from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime
