#!/bin/bash
set -e

# Run pytest with coverage
poetry run pytest --cov=uncertainty_engine_types --cov-report=html
open ./htmlcov/index.html
