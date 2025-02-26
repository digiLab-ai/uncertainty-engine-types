from pydantic import BaseModel

from .message import Message


class ChatHistory(BaseModel):
    messages: list[Message]
