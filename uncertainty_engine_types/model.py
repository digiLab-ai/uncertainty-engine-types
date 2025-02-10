from typing import Any, Dict, Tuple
import json
import tempfile

from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    model_type: str
    config: dict
    metadata: dict

    model_config = ConfigDict(protected_namespaces=())

    def load_model(self) -> Tuple[Any, Dict]:

        from twinlab_models.models import model_type_from_str  # type: ignore

        model_type = self.model_type
        tl_model = model_type_from_str(model_type)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
            # Write the JSON to the temporary file
            json.dump(self.model_dump(), f)  # Changed dumps to dump
            f.flush()
            tl_model, meta_data = tl_model.load(f.name)

        return tl_model, meta_data

    @classmethod
    def save_model(cls, model, meta_data: dict) -> "Model":

        with tempfile.NamedTemporaryFile(mode="r", suffix=".json") as f:
            model.save(f.name, meta_data)
            f.seek(0)
            config = json.load(f)

        return cls(**config)
