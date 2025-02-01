from pydantic import BaseModel


class Handle(BaseModel):
    node_name: str
    node_handle: str

    def __init__(self, handle_str: str):
        if handle_str.count(".") != 1:
            raise ValueError(
                "Handle string must contain exactly one dot ('.') separating node and handle"
            )

        node_name, node_handle = handle_str.split(".")
        super().__init__(node_name=node_name, node_handle=node_handle)
