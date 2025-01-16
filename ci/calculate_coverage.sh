#!/bin/bash
set -e

# Run pytest with coverage
poetry run pytest --cov=workflow_types --cov-report=xml

# Extract coverage percentage using a more specific awk command
COVERAGE_PERCENT=$(awk -F'"' '/<coverage.*line-rate=/ {for(i=1;i<=NF;i++) if($i ~ /line-rate/) print $(i+1)}' coverage.xml)

# Convert the fraction to percentage
COVERAGE_PERCENT=$(echo "$COVERAGE_PERCENT * 100" | bc -l | xargs printf "%.0f")

# Output the coverage percentage
echo $COVERAGE_PERCENT
