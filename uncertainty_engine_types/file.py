from enum import StrEnum

from pydantic import BaseModel


class FileLocation(StrEnum):
    LOCAL = "local"
    S3 = "s3"


class File(BaseModel):
    pass


class Document(File):
    location: FileLocation
    path: str


class Image(File):
    location: FileLocation
    path: str


class Mesh(File):
    location: FileLocation
    path: str


class SQLTable(File):
    url: str
    query: str


class TabularData(File):
    location: FileLocation
    path: str


class WebPage(File):
    url: str
