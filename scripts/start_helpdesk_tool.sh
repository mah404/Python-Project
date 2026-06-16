#!/bin/bash

#Start script for the Nordstern Helpdesk Tool
#this script checks the environment before starting the Python Program 
#check if python3 is installed

#get the project directory
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"


echo "Start Nordstern Helpdesk Tool..."

#check if python3 is installed
if ! command -v python3 &> /dev/null
then 
    echo "FEHLER: Python 3 ist nicht installiert. Bitte installieren Sie Python 3, um das Nordstern Helpdesk-Tool auszuführen."
    exit 1 
fi 

# check if the required python packages are installed
for folder in data src reports 
do
   if [ ! -d "$PROJECT_DIR/$folder" ]; then
      echo "FEHLER: Erforderlicher Ordner '$folder' fehlt. Bitte stellen Sie sicher, dass alle erforderlichen Ordner vorhanden sind."
      exit 1
   fi
done


#check if main.py exists
if [ ! -f "$PROJECT_DIR/src/main.py" ]; then
    echo "ERROR: main.py is missing in the src folder. Please ensure main.py is present in the src folder."
    exit 1
fi

echo "Alle Überprüfungen erfolgreich durchgeführt. Das Nordstern Helpdesk-Tool wird nun gestartet...."
echo "zum Beenden des Tools, drücken Sie Ctrl + C"

python3 "$PROJECT_DIR/src/main.py"