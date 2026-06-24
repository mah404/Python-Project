#!/bin/bash

# Start script for the Nordstern Helpdesk Tool
# This script checks the environment before starting the Python program.


#$0 is a special variable in bash that represents the name of the script being executed. In this case, it refers to the start_helpdesk_tool.sh script itself. 
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "Starting Nordstern Helpdesk Tool..."

# Check if Python 3 is installed
# ! command -v python3 &> /dev/null checks if the command python3 is available in the system's PATH. If it is not found, the script prints an error message and exits with a status code of 1.
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
#! -f checks if the file does not exist. If it doesn't, it prints an error message and exits the script with a status code of 1.
if [ ! -f "$PROJECT_DIR/src/main.py" ]; then
    echo "ERROR: Python main program src/main.py is missing."
    exit 1
fi

echo "All checks passed."
echo "Starting Python program..."

python3 "$PROJECT_DIR/src/main.py"