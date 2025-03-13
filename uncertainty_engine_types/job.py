from enum import Enum
from typing import Optional

from pydantic import BaseModel


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"


class JobInfo(BaseModel):
    status: JobStatus
    message: Optional[str] = None
    inputs: dict
    outputs: Optional[dict] = None
