import pytest


def test_import_my_library():
    try:
        import workflow_types
    except ImportError as err:
        pytest.fail(f"Failed to import 'workflow_types': {err}")
