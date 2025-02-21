from pydantic import BaseModel, model_validator


class Handle(BaseModel):
    node_name: str
    node_handle: str

    @model_validator(mode="before")
    @classmethod
    def split_handle(cls, values):
        if isinstance(values, str):  # Handle single-string case
            parts = values.split(".")
            if len(parts) != 2:
                raise ValueError(
                    "Handle string must contain exactly one dot ('.') separating node and handle"
                )
            return {"node_name": parts[0], "node_handle": parts[1]}
        return values
