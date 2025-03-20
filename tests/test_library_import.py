import pytest


def test_import_my_library():
    """
    Verify that the library can be imported.
    """
    try:
        import uncertainty_engine_types
    except ImportError as err:
        pytest.fail(f"Failed to import 'uncertainty_engine_types': {err}")


def test_star_import():
    """
    Verify types that are imported with a star import.
    """

    exec("from uncertainty_engine_types import *")
