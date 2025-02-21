from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class FileLocation(StrEnum):
    LOCAL = "local"
    S3 = "s3"
    SQL = "sql"
    WWW = "www"


class FileType(StrEnum):
    CSV = "csv"
    DOCX = "docx"
    PDF = "pdf"
    TXT = "txt"


class Document(BaseModel):
    """
    Document identification.
    """

    location: FileLocation
    file_type: FileType
    path: str
    excerpt: Optional[str] = None
