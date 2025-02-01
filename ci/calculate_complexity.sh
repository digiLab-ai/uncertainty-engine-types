#!/bin/bash
set -e

# Run the radon command and capture the output
RADON_OUTPUT=$(poetry run radon cc uncertainty_engine_types -a)
echo "$RADON_OUTPUT"

# Extract the complexity score using grep and awk
COMPLEXITY_SCORE=$(echo "$RADON_OUTPUT" | grep "Average complexity:" | awk '{print $3}')

# Output the complexity score
echo $COMPLEXITY_SCORE
