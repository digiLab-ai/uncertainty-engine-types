from pydantic import BaseModel

from .node_info import NodeInfo


class UserContext(BaseModel):
    email: str
    project_id: str
    cost_code: str


class Context(BaseModel):
    sync: bool
    job_id: str
    queue_url: str
    cache_url: str
    timeout: int
    nodes: dict[str, NodeInfo]
    user: UserContext
