#!/bin/bash

# System snapshot Script für die Nordstern Helpdesk Tool Entwicklung
# Dieses Skript sammelt Informationen über das System, um bei der Fehlersuche und Entwicklung



PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_FILE="$PROJECT_DIR/reports/system_snapshot.txt"


##checken ob der reports Ordner existiert, wenn nicht erstelle ihn 

if [ ! -d "$PROJECT_DIR/reports" ]; then
    echo "Der reports Ordner existiert nicht. Erstelle den Ordner..."
    exit 1
fi 


echo "Mach einen System Snapshot für die Nordstern Helpdesk Tool Entwicklung..."  

{
    echo "System Snapshot "
    echo "=================="
    echo "Date: $(date)"
    echo "Hostname: $(hostname)"
    echo "User: $(whoami) "
    echo "Current Directory: $(pwd)"
    echo ""
    echo "Free Disk space"
    df -h . 

} > "$REPORT_FILE"

echo "System Snapshot wurde erfolgreich erstellt und in $REPORT_FILE gespeichert."
