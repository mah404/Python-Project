#!/bin/bash

# Start script for the Nordstern Helpdesk Tool
# This script checks the environment before starting the Python program.

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "Starting Nordstern Helpdesk Tool..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed."
    exit 1
fi

# Check required folders
for folder in data src reports
do
    if [ ! -d "$PROJECT_DIR/$folder" ]; then
        echo "ERROR: Required folder '$folder' is missing."
        exit 1
    fi
done

# Check if main.py exists
if [ ! -f "$PROJECT_DIR/src/main.py" ]; then
    echo "ERROR: Python main program src/main.py is missing."
    exit 1
fi

echo "All checks passed."
echo "Starting Python program..."

python3 "$PROJECT_DIR/src/main.py"