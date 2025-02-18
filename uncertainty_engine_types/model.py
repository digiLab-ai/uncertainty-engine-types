from pydantic import BaseModel, ConfigDict


class TwinLabModel(BaseModel):
    model_type: str
    config: dict
    metadata: dict

    model_config = ConfigDict(protected_namespaces=())
