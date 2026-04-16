#!/bin/bash

# Activate virtual environment
source ./venv/bin/activate

# Run pytest suite
python -m pytest test_pink_morsel_visualised.py

# Capture pytest exit code
status=$?

# Return success only if tests passed
if [ "$status" -eq 0 ]; then
  exit 0
else
  exit 1
fi