from enum import Enum

from pydantic import BaseModel


class SQLKind(Enum):
    POSTGRES = "POSTGRES"


class SQLConfig(BaseModel):
    """
    Connection configuration for SQL databases.
    """

    kind: SQLKind
    host: str
    username: str
    password: str
    port: int
    database: str
