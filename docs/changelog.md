# Changelog

## Stand 1: Projektstruktur und Startdaten angelegt

Die Projektstruktur wurde erstellt. Es wurden die Ordner `data`, `scripts`, `src`, `reports`, `docs` und `tests` angelegt.

Im Ordner `data` wurden die Startdateien `users.csv`, `tickets.csv` und `support.log` erstellt. Die Dateien enthalten fiktive Benutzerdaten, Helpdesk-Tickets und Logeinträge für die spätere Auswertung.

## Stand 2: Bash-Skripte und Python-Menü umgesetzt

Im zweiten Entwicklungsschritt habe ich die beiden Bash-Skripte `start_helpdesk_tool.sh` und `collect_snapshot.sh` erstellt.

Das Skript `start_helpdesk_tool.sh` dient zum Starten des Helpdesk-Tools. Vor dem Start werden einige wichtige Prüfungen durchgeführt. Dabei wird kontrolliert, ob Python 3 installiert ist, ob die benötigten Projektordner vorhanden sind und ob sich die Datei `main.py` im Ordner `src` befindet. Erst nach erfolgreicher Prüfung wird das Python-Programm gestartet.

Mit dem Skript `collect_snapshot.sh` kann eine Systemmomentaufnahme erstellt werden. Dabei werden Informationen wie Datum, Hostname, aktueller Benutzer, aktueller Pfad sowie der verfügbare Speicherplatz erfasst und automatisch im Ordner `reports` gespeichert.

Zusätzlich habe ich das Python-Hauptprogramm `src/main.py` erstellt. Darin wurde eine Menüführung mit acht Funktionen umgesetzt. Über das Menü können Benutzerdaten geprüft, Tickets ausgewertet, Logdateien analysiert und Supportberichte erstellt werden.

Nach mehreren Tests konnten beide Bash-Skripte sowie die Menüführung erfolgreich ausgeführt werden.


## Stand 3: Auswertungen, Bericht und Fehlerbehandlung fertiggestellt

Die Python-Funktionen zum Einlesen und Prüfen der Daten wurden umgesetzt. Das Tool kann Benutzer prüfen, Tickets anzeigen, Tickets nach Status, Priorität und Kategorie auswerten, kritische offene Tickets anzeigen und die Logdatei analysieren.

Zusätzlich wurde die Funktion zur Erstellung eines Supportberichts umgesetzt. Der Bericht wird als `support_report.txt` im Ordner `reports` gespeichert und enthält Benutzerzahlen, fehlende Pflichtangaben, Ticketzahlen, kritische Tickets sowie ERROR- und WARNING-Meldungen aus der Logdatei.

Die Fehlerbehandlung wurde ergänzt. Fehlende Dateien wie `users.csv`, `tickets.csv` oder `support.log` werden erkannt und mit verständlichen Fehlermeldungen angezeigt. Falsche Menüeingaben werden ebenfalls abgefangen.