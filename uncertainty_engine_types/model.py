from pydantic import BaseModel, ConfigDict


class MachineLearningModel(BaseModel):
    model_type: str
    config: dict
    metadata: dict

    model_config = ConfigDict(protected_namespaces=())
