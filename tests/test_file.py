import pytest
from pydantic import ValidationError

from uncertainty_engine_types import (
    PDF,
    Document,
    File,
    Image,
    LocalStorage,
    S3Storage,
    SQLTable,
    MeshFile,
    TabularData,
    WebPage,
)


def test_s3_storage(s3_storage_data: dict):
    """
    Test that an S3 storage location can be created.
    """

    # Instantiate the S3 storage location
    location = S3Storage(bucket="bucket", key="key")

    assert location.model_dump() == s3_storage_data


@pytest.mark.parametrize("field", ["bucket", "key"])
def test_s3_storage_raise_missing(s3_storage_data: dict, field: str):
    """
    Test that the S3Storage model raises an error when missing a required field.

    Args:
        s3_storage_data: Some data to define an S3Storage object
        field: A field to remove from the s3_storage_data
    """

    # Remove a required field
    del s3_storage_data[field]

    # Try to instantiate an S3Storage object with a missing required field
    with pytest.raises(ValidationError):
        S3Storage(**s3_storage_data)


def test_local_storage(local_storage_data: dict):
    """
    Test that a local storage location can be created.

    Args:
        local_storage_data: Some data to define a LocalStorage object
    """

    # Instantiate the local storage location
    location = LocalStorage(path="path")

    assert location.model_dump() == local_storage_data


def test_local_storage_raise_missing(local_storage_data: dict):
    """
    Test that the LocalStorage model raises an error when missing a required field.

    Args:
        local_storage_data: Some data to define a LocalStorage object
    """

    # Remove a required field
    del local_storage_data["path"]

    # Try to instantiate a LocalStorage object with a missing required field
    with pytest.raises(ValidationError):
        LocalStorage(**local_storage_data)


@pytest.mark.parametrize(
    "file_type",
    [
        PDF,
        Document,
        Image,
        TabularData,
    ],
)
def test_file_s3(s3_storage_data: dict, file_type: File):
    """
    Test that the file type can be created with an S3 storage location.

    Args:
        s3_storage_data: Some data to define an S3Storage object
        file_type: A file type class
    """

    # Instantiate the S3 storage location
    location = S3Storage(**s3_storage_data)

    # Instantiate the file type with the S3 storage location
    file = file_type(location=location)

    assert file.model_dump() == {"location": location.model_dump()}


@pytest.mark.parametrize(
    "file_type",
    [
        PDF,
        Document,
        Image,
        TabularData,
    ],
)
def test_file_local(file_type: File, local_storage_data: dict):
    """
    Test that the file type can be created with a local storage location.

    Args:
        file_type: A file type class
        local_storage_data: Some data to define a LocalStorage object
    """

    # Instantiate the local storage location
    location = LocalStorage(**local_storage_data)

    # Instantiate the file type with the local storage location
    file = file_type(location=location)

    assert file.model_dump() == {"location": location.model_dump()}


@pytest.mark.parametrize(
    "file_type",
    [
        PDF,
        Document,
        Image,
        TabularData,
    ],
)
def test_file_raise_missing(file_type: File):
    """
    Test that the file type raises an error when missing a required field.

    Args:
        file_type: A file type class
    """

    # Try to instantiate a file type object with a missing required field
    with pytest.raises(ValueError):
        file_type()


def test_sql_table(sql_table_data: dict):
    """
    Test that an SQL table file can be created.

    Args:
        sql_table_data: Some data to define an SQLTable object
    """

    # Instantiate the SQL table file
    file = SQLTable(**sql_table_data)

    assert file.model_dump() == sql_table_data


def test_web_page(web_page_data: dict):
    """
    Test that a web page file can be created.

    Args:
        web_page_data: Some data to define a WebPage object
    """

    # Instantiate the web page file
    file = WebPage(**web_page_data)

    assert file.model_dump() == web_page_data
