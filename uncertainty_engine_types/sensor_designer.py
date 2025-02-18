from pydantic import BaseModel


class SensorDesigner(BaseModel):
    bed: dict
