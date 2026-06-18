# Changelog

## Stand 1: Projektstruktur und Startdaten angelegt

Die Projektstruktur wurde erstellt. Es wurden die Ordner `data`, `scripts`, `src`, `reports`, `docs` und `tests` angelegt.

Im Ordner `data` wurden die Startdateien `users.csv`, `tickets.csv` und `support.log` erstellt. Die Dateien enthalten fiktive Benutzerdaten, Helpdesk-Tickets und Logeinträge für die spätere Auswertung.

## Stand 2: Bash-Skripte und Python-Menü umgesetzt

Die Bash-Skripte `start_helpdesk_tool.sh` und `collect_snapshot.sh` wurden erstellt.

Das Startskript prüft, ob Python 3 vorhanden ist, ob die benötigten Projektordner existieren und ob das Python-Hauptprogramm vorhanden ist. Danach startet es das Helpdesk-Tool.

Das Snapshot-Skript erstellt eine Systemmomentaufnahme mit Datum, Hostname, Benutzer, aktuellem Pfad und freiem Speicherplatz. Die Ausgabe wird im Ordner `reports` gespeichert.

Außerdem wurde das Python-Hauptprogramm `src/main.py` mit einer Menüführung erstellt. Das Menü enthält acht Punkte für typische Supportaufgaben.

## Stand 3: Auswertungen, Bericht und Fehlerbehandlung fertiggestellt

Die Python-Funktionen zum Einlesen und Prüfen der Daten wurden umgesetzt. Das Tool kann Benutzer prüfen, Tickets anzeigen, Tickets nach Status, Priorität und Kategorie auswerten, kritische offene Tickets anzeigen und die Logdatei analysieren.

Zusätzlich wurde die Funktion zur Erstellung eines Supportberichts umgesetzt. Der Bericht wird als `support_report.txt` im Ordner `reports` gespeichert und enthält Benutzerzahlen, fehlende Pflichtangaben, Ticketzahlen, kritische Tickets sowie ERROR- und WARNING-Meldungen aus der Logdatei.

Die Fehlerbehandlung wurde ergänzt. Fehlende Dateien wie `users.csv`, `tickets.csv` oder `support.log` werden erkannt und mit verständlichen Fehlermeldungen angezeigt. Falsche Menüeingaben werden ebenfalls abgefangen.