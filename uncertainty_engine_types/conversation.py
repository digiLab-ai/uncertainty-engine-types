from pydantic import BaseModel

from .message import Message


class Conversation(BaseModel):
    messages: list[Message]
