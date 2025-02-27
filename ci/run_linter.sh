#!/bin/bash
set -e

# When using flake8 we ignore:
# E501: Line too long: Too strict for us
# W503: Line break before binary operator: The advice is changing to the opposite here soon (W504), so no point. See: https://www.flake8rules.com/rules/W503.html.
# For tests we ignore:
# F401: When testing imports, we don't need to use the imported module
poetry run flake8 --ignore=E501,W503 --per-file-ignores="tests/test_library_import.py:F401" uncertainty_engine_types tests
