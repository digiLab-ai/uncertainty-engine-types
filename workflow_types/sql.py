from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

from pydantic import BaseModel
from typeguard import typechecked


class SQLDatabase(ABC):
    @abstractmethod
    def execute(self, query: str) -> list[tuple[Any, ...]]:
        """
        Execute the given query.

        Parameters:
            query (str): The SQL query to execute.

        Returns:
            str: The result of the query.
        """
        pass


class PostgreSQL(SQLDatabase):
    @typechecked
    def __init__(
        self, host: str, username: str, password: str, port: int, database: str
    ):
        import psycopg2

        self.connection = psycopg2.connect(
            host=host, user=username, password=password, port=port, database=database
        )
        self.cursor = self.connection.cursor()

    @typechecked
    def execute(self, query: str) -> list[tuple[Any, ...]]:
        """
        Execute the given query.

        Parameters:
            query (str): The SQL query to execute.

        Returns:
            str: The result of the query.
        """

        self.cursor.execute(query)
        return self.cursor.fetchall()


class SQLKind(Enum):
    POSTGRES = "POSTGRES"


class SQLManager(BaseModel):
    """
    Connection manager for SQL databases.
    """

    kind: SQLKind
    host: str
    username: str
    password: str
    port: int
    database: str

    @typechecked
    def connect(self) -> SQLDatabase:
        """
        Connect to the SQL database.
        """

        match self.kind:
            case SQLKind.POSTGRES:
                return PostgreSQL(
                    host=self.host,
                    username=self.username,
                    password=self.password,
                    port=self.port,
                    database=self.database,
                )
            case _:
                raise ValueError("Unsupported SQL kind")
