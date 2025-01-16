#!/bin/bash
set -e

# Run pytest with coverage
poetry run pytest --cov=workflow_types --cov-report=html
open ./htmlcov/index.html
