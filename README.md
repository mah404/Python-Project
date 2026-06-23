# 5.1 Projektstruktur vorbereiten

Als erstes habe ich die Projektstruktur für das Helpdesk-Tool erstellt. Ziel war es, alle Dateien übersichtlich zu organisieren, damit eine andere IT-Fachkraft das Projekt leicht verstehen und weiterentwickeln kann.

Ich habe folgende Ordner angelegt:

* data
* scripts
* src
* reports
* docs
* tests

Jeder Ordner hat eine bestimmte Aufgabe. Im Ordner data werden die Eingabedateien gespeichert. Im Ordner scripts befinden sich die Bash-Skripte. Der Python-Quellcode liegt im Ordner src. Automatisch erzeugte Berichte werden im Ordner reports gespeichert. Technische Notizen und Dokumentation befinden sich im Ordner docs. Testnotizen und Testergebnisse werden im Ordner tests abgelegt.

Dadurch entstand eine klare und nachvollziehbare Projektstruktur.

![alt text](<Screenshot 2026-06-16 152833.png>)


# 5.2 Startdaten anlegen

Anschließend habe ich die erforderlichen Startdaten erstellt.

Im Ordner data habe ich folgende Dateien angelegt:

* users.csv
* tickets.csv
* support.log

In der Datei users.csv habe ich die vorgegebenen Benutzer eingetragen. Dabei habe ich bewusst den Benutzer "nklein" ohne E-Mail-Adresse übernommen, da dies später für die Überprüfung fehlender Pflichtangaben benötigt wird.

In der Datei tickets.csv habe ich die vorgegebenen Helpdesk-Tickets eingetragen. Die Tickets enthalten verschiedene Prioritäten und Bearbeitungsstände.

In der Datei support.log habe ich die vorgegebenen Logeinträge gespeichert. Die Datei enthält INFO-, WARNING- und ERROR-Meldungen und dient später zur Auswertung der Logdaten.

Damit standen alle erforderlichen Testdaten für das Projekt zur Verfügung.

# 5.3 Bash-Startskripte erstellen

Im nächsten Schritt habe ich zwei Bash-Skripte erstellt.

## start_helpdesk_tool.sh

Dieses Skript dient als Startskript für das gesamte Helpdesk-Tool.

Vor dem Start des Python-Programms werden mehrere Prüfungen durchgeführt:

* Prüfung, ob Python 3 installiert ist
* Prüfung, ob die benötigten Projektordner vorhanden sind
* Prüfung, ob die Datei src/main.py existiert

Erst wenn alle Prüfungen erfolgreich sind, wird das Python-Hauptprogramm gestartet.

Bei einem Fehler gibt das Skript eine verständliche Fehlermeldung aus und beendet die Ausführung.

## collect_snapshot.sh

Dieses Skript erstellt automatisch eine Systemmomentaufnahme.

Folgende Informationen werden erfasst:

* Aktuelles Datum und Uhrzeit
* Hostname des Systems
* Aktueller Benutzer
* Aktuelles Arbeitsverzeichnis
* Verfügbarer Speicherplatz

Die Informationen werden automatisch in der Datei:

reports/system_snapshot.txt

gespeichert.

## Ausführbarkeit der Skripte

Beide Skripte wurden mit folgendem Befehl ausführbar gemacht:

chmod +x scripts/start_helpdesk_tool.sh
chmod +x scripts/collect_snapshot.sh

## Test der Snapshot-Funktion

Nach der Erstellung habe ich das Skript collect_snapshot.sh ausgeführt.

Das Skript hat erfolgreich die Datei system_snapshot.txt im Ordner reports erzeugt.

Der Bericht enthält Datum, Hostname, Benutzername, aktuelles Verzeichnis und Informationen über den freien Speicherplatz.

Damit wurden die Anforderungen aus Abschnitt 5.3 erfolgreich umgesetzt.

# 5.4 Python-Hauptprogramm vorbereiten

Zusätzlich habe ich bereits die Datei src/main.py erstellt.

In dieser Datei wurde eine erste Menüstruktur für das Helpdesk-Tool angelegt.

Das Menü enthält folgende Punkte:

1. System Snapshot anzeigen
2. Benutzerliste prüfen
3. Ticketübersicht anzeigen
4. Tickets analysieren
5. Kritische Tickets anzeigen
6. Logdatei analysieren
7. Supportbericht erstellen
8. Programm beenden

Aktuell sind die Menüpunkte als Platzhalter vorhanden. Die eigentlichen Funktionen werden in den nächsten Schritten implementiert.

Damit ist die grundlegende Struktur des Python-Hauptprogramms bereits vorbereitet.

![alt text](<Screenshot 2026-06-16 161438.png>)


# 6. Verbindliche Supportfälle

## Fall 1 – Fehlende Benutzerdaten

### Ausgangssituation

In der Datei `users.csv` wurde geprüft, ob alle Benutzer die erforderlichen Pflichtangaben besitzen.

### Verwendete Funktion

Menüpunkt 2 – Check user list

### Ergebnis

Das Tool hat erkannt, dass beim Benutzer **nklein** die E-Mail-Adresse fehlt. Zusätzlich wurde angezeigt, dass der Benutzer **archiv01** als inaktiv markiert ist.

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Fall 2 – Hoch priorisiertes VPN Ticket

### Ausgangssituation

Es sollte geprüft werden, welche offenen Tickets eine hohe Priorität besitzen.

### Verwendete Funktion

Menüpunkt 5 – Show critical open tickets

### Ergebnis

Das Tool hat die beiden kritischen Tickets **HD-1001** und **HD-1002** angezeigt.

Aus meiner Sicht sollte zuerst **HD-1002** bearbeitet werden, da eine VPN-Verbindung regelmäßig abbricht und dadurch die Arbeit von Benutzern direkt beeinträchtigt werden kann.

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Fall 3 – Logauffälligkeiten

### Ausgangssituation

Die Logdatei `support.log` wurde ausgewertet, um mögliche Fehler und Warnungen zu erkennen.

### Verwendete Funktion

Menüpunkt 6 – Analyze log file

### Ergebnis

Das Tool hat die Logdatei erfolgreich analysiert.

Gefundene Einträge:

* INFO: 2
* WARNING: 2
* ERROR: 2

Dadurch können kritische Ereignisse schneller erkannt werden.

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Fall 4 – Supportbericht für Teamleitung

### Ausgangssituation

Für die Teamleitung sollte ein automatischer Supportbericht erstellt werden.

### Verwendete Funktion

Menüpunkt 7 – Create support report

### Ergebnis

Der Bericht wurde erfolgreich erstellt und im Ordner `reports` als Datei `support_report.txt` gespeichert.

Der Bericht enthält Informationen über Benutzer, Tickets, Logmeldungen sowie eine kurze technische Bewertung.

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Fall 5 – Fehlende Eingabedatei

### Ausgangssituation

Um die Fehlerbehandlung zu testen, wurde eine Eingabedatei vorübergehend umbenannt.

### Verwendete Funktion

Benutzerprüfung über Menüpunkt 2

### Ergebnis

Das Tool hat die fehlende Datei erkannt und eine verständliche Fehlermeldung ausgegeben. Das Programm ist dabei nicht abgestürzt und konnte weiterhin verwendet werden.

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Fall 6 – Übergabe an Supportteam

### Ausgangssituation

Für die Mitarbeiterin Lea Sommer sollte eine kurze Anleitung erstellt werden.

### Verwendete Funktion

Bedienungsanleitung

### Ergebnis

Es wurde eine einfache Anleitung erstellt, mit der das Tool gestartet und die wichtigsten Funktionen verwendet werden können.

### Kurzanleitung

Tool starten:

```bash
./scripts/start_helpdesk_tool.sh
```

Snapshot erstellen:

```bash
./scripts/collect_snapshot.sh
```

Wichtige Menüfunktionen:

* 1 = System Snapshot anzeigen
* 2 = Benutzer prüfen
* 3 = Ticketübersicht anzeigen
* 4 = Tickets analysieren
* 5 = Kritische Tickets anzeigen
* 6 = Logdatei analysieren
* 7 = Supportbericht erstellen
* 8 = Programm beenden

### Nachweis

Siehe Screenshot am Ende der Dokumentation.

---

## Screenshots

![alt text](<falls.png>)
![alt text](<falls2.png>)
![alt text](<falls3.png>)
