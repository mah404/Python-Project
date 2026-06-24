#!/bin/bash

# System snapshot script for the Nordstern Helpdesk Tool
# This script saves basic system information into the reports folder.

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_FILE="$PROJECT_DIR/reports/system_snapshot.txt"

# Check if reports folder exists
# ! -d means "if the directory does not exist". If the reports folder is missing, it prints an error message and exits the script with a status code of 1.
if [ ! -d "$PROJECT_DIR/reports" ]; then
    echo "ERROR: reports folder is missing."
    exit 1
fi

echo "Creating system snapshot..."

{
    echo "System Snapshot"
    echo "==============="
    echo "Date: $(date)"
    echo "Hostname: $(hostname)"
    echo "User: $(whoami)"
    echo "Current Path: $(pwd)"
    echo ""
    echo "Free Disk Space:"
    df -h .
} > "$REPORT_FILE"

echo "System snapshot saved to: $REPORT_FILE"