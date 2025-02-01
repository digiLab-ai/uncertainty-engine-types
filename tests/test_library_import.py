import pytest


def test_import_my_library():
    try:
        import uncertainty_engine_types
    except ImportError as err:
        pytest.fail(f"Failed to import 'uncertainty_engine_types': {err}")
