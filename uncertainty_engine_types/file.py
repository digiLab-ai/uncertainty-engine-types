from typing import Union

from pydantic import BaseModel


class S3Storage(BaseModel):
    bucket: str
    key: str


class LocalStorage(BaseModel):
    path: str


FileLocation = Union[S3Storage, LocalStorage]


class File(BaseModel):
    pass


class Document(File):
    location: FileLocation


class Image(File):
    location: FileLocation


class Mesh(File):
    location: FileLocation


class PDF(File):
    location: FileLocation


class SQLTable(File):
    url: str
    query: str


class TabularData(File):
    location: FileLocation


class WebPage(File):
    url: str
