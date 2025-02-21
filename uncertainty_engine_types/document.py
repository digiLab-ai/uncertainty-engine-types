from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FileExtension(Enum):
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
