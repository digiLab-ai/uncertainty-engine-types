from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class JobStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class JobInfo(BaseModel):
    status: JobStatus
    message: Optional[str] = None
    inputs: dict
    outputs: Optional[dict] = None
