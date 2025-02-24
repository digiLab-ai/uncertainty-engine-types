from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class FileType(StrEnum):
    DOCUMENT = "document"
    IMAGE = "image"
    WEBPAGE = "webpage"


class FileLocation(StrEnum):
    LOCAL = "local"
    S3 = "s3"
    WWW = "www"


class File(BaseModel):
    file_type: FileType
    path: str
    location: FileLocation
    meta: Optional[dict] = None
