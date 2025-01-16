#!/bin/bash
set -e

# Run the radon mi command with summaries and capture the output
OUTPUT=$(poetry run radon mi -s workflow_types)

# Extract the numerical maintainability index scores using awk
SCORES=$(echo "$OUTPUT" | awk -F'[()]' '{print $2}')

# Calculate the average of these scores using awk
AVERAGE_SCORE=$(echo "$SCORES" | awk '{sum += $1; n++} END {if (n > 0) print sum / n; else print "No scores calculated"}')

# Output the average maintainability score
echo $AVERAGE_SCORE
