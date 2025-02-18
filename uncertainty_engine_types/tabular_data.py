from pydantic import BaseModel


class TabularData(BaseModel):
    csv: str
