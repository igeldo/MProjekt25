# HelloPython

Example for
- classes in Python
- unit tests with pytest
- unit tests with mocks

## Vorbereitung

Alle Anweisungen hier sind als Kommandos in einer Unix-Shell-Umgebung
anzuwenden, also z. B. in einem Terminal unter Linux oder MacOS oder
in einer Git Bash unter Windows.

### Voraussetzungen

- Anweisungen der übergeordneten README-Datei sind ausgeführt
- Python 3 ist installiert (https://www.python.org/downloads/)

### Einrichten des virtual environment 

Einmalig wird die virtuelle Umgebung für das Projekt eingerichtet:
```shell
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Starten des Programms

### Wechsel in virtual environment

Für jede neu geöffnete Shell muss einmalig in die virtuelle Umgebung gewechselt werden:
```shell
cd <pfad_zu_src>/MProjekt25/HelloPython
source venv/bin/activate
```

### Ausführen der Tests

Ausführen aller Unit-Tests im Verzeichnis 'tests'

```shell
pytest
```

### Ausführen des Programms

```shell
python main.py
```

