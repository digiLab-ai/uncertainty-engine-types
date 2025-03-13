from pydantic import BaseModel

from .node_info import NodeInfo


class Context(BaseModel):
    sync: bool
    job_id: str
    queue_url: str
    cache_url: str
    timeout: int
    nodes: dict[str, NodeInfo]
