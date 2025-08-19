from enum import Enum
from typing import Optional

from pydantic import BaseModel


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"

    def is_terminal(self) -> bool:
        return self in [JobStatus.COMPLETED, JobStatus.FAILED]


class JobInfo(BaseModel):
    status: JobStatus
    message: Optional[str] = None
    inputs: dict
    outputs: Optional[dict] = None
    progress: "None | str | dict[str, JobInfo]" = None
