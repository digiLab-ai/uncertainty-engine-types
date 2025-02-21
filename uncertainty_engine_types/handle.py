from pydantic import BaseModel, model_validator


class Handle(BaseModel):
    node_name: str
    node_handle: str

    @model_validator(mode="before")
    @classmethod
    def split_handle(cls, values):
        if isinstance(values, str):
            parts = values.split(".")
            if len(parts) != 2:
                raise ValueError(
                    "Handle string must contain exactly one dot ('.') separating node and handle"
                )
            return {"node_name": parts[0], "node_handle": parts[1]}
        return values

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) == 1 and isinstance(args[0], str):
                # Convert the positional argument to a dict via model_validate
                kwargs = self.__class__.model_validate(args[0]).model_dump()
            else:
                raise TypeError("Invalid positional arguments")
        super().__init__(**kwargs)
