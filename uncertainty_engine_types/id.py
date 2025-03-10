from pydantic import BaseModel


class ResourceID(BaseModel):
    id: str
