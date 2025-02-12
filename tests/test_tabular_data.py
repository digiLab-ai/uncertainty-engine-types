import os

import pytest

from uncertainty_engine_types.tabular_data import TabularData


@pytest.fixture
def csv_string() -> str:
    """
    A CSV string with some data.

    Returns:
        The CSV string with some data.
    """

    return "a,b,c\n1,2,3\n4,5,6\n"


@pytest.fixture(scope="function")
def data_file(csv_string: str):
    """
    Creates a temporary CSV file containing the provided data and returns its file path. 
    The file is automatically removed after the test.

    Args:
        csv_string: The CSV string with some data.

    Yields:
        The path to the temporary CSV file.
    """
    file_path = "tests/test_data.csv"

    # Write the CSV string to a file
    with open(file_path, "w") as f:
        f.write(csv_string)

    yield file_path

    # Clean up
    os.remove(file_path)


def test_load_dataframe(csv_string: str):
    """
    Test that the load_dataframe method returns a DataFrame with the correct data.

    Args:
        csv_string: The CSV string with some data.
    """
    # Define a TabularData instance with a CSV string
    tabular_data = TabularData(csv=csv_string)

    # Load the DataFrame
    df = tabular_data.load_dataframe()

    # Check that the DataFrame has the correct data
    assert df.to_csv(index=False) == csv_string


def test_read_csv(data_file: str, csv_string: str):
    """
    Test that the read_csv method reads a CSV file and returns a TabularData instance with the correct data.

    Args:
        data_file: The path to the CSV file.
    """
    # Read the CSV file
    tabular_data = TabularData.read_csv(data_file)

    # Verify TabularData instance
    assert isinstance(tabular_data, TabularData)

    # Check that the data is correct
    assert tabular_data.csv == csv_string
