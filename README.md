# python-oo

Example for
- classes in Python
- unit tests
- unit tests with mocks

## Vorbereitung

Alle Anweisungen hier sind als Kommandos in einer Unix-Shell-Umgebung
anzuwenden, also z. B. in einem Terminal unter Linux oder MacOS oder
in einer Git Bash unter Windows.

### Voraussetzungen

- Python 3 ist installiert (https://www.python.org/downloads/)
- Git-Client ist installiert (https://git-scm.com/downloads)
- GitHub-Account ist angelegt und SSH-Key ist bei GitHub hinterlegt (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

### Clonen des Repositories

```shell
git clone git@github.com:igeldo/MProjekt25.git
```

Es ist ein neues Verzeichnis mit dem Namen `MProjekt25` entstanden.

Wechsel in das Verzeichnis und Abfrage des Status mit
```shell
cd MProjekt25
git status
```
sollte ungefähr folgende Ausgabe ergeben:
```shell
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

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
cd <pfad_zu_src>/MProjekt25
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




