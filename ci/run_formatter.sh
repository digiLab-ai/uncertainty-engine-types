#!/bin/bash
set -e

poetry run black --check --diff uncertainty_engine_types
