from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class FileExtension(StrEnum):
    PDF = "pdf"
    TXT = "txt"
    DOCX = "docx"


class Document(BaseModel):
    """
    Document identification.
    """

    file_name: str
    file_extension: str
    url: str
    excerpt: Optional[str] = None
