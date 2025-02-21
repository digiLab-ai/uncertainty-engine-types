from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FileType(Enum):
    PDF = "pdf"
    TXT = "txt"
    DOCX = "docx"


class Document(BaseModel):
    """
    Document identification.
    """

    file_name: str
    file_type: str
    url: str
