import sqlite3


def create_table() -> object:
    """

    :rtype: object
    """
    verbindung = sqlite3.connect("test.db")
    zeiger = verbindung.cursor()
    sql_anweisung = """
    CREATE TABLE IF NOT EXISTS person (
        vorname VARCHAR(20),
        age INTEGER,
        geschlecht VARCHAR(10),
        gewicht DOUBLE,
        groeße DOUBLE
    );"""
    zeiger.execute(sql_anweisung)
    verbindung.commit()
    verbindung.close()


def add_person(vorname, age, geschlecht, gewicht, size):
    verbindung = sqlite3.connect("test.db")
    zeiger = verbindung.cursor()
    sql_anweisung = "INSERT INTO person (vorname, age, geschlecht, gewicht, groeße) VALUES (?, ?, ?, ?, ?);"  # die "?" stehen für sichere Parameter vorname, age, geschlecht, gewicht, groeße
    zeiger.execute(sql_anweisung, (vorname, age, geschlecht, gewicht, size))
    verbindung.commit()
    verbindung.close()


# Funktion um Daten aus Datenbank zu lesen und rückzugeben

def get_all_persons():
    verbindung = sqlite3.connect("test.db")  # Verbindung zur Datenbank
    zeiger = verbindung.cursor()  # Cursor erstellen
    sql_anweisung = "SELECT * FROM person;"  # SQL-Abfrage, um alle Daten aus der Tabelle zu holen
    zeiger.execute(sql_anweisung)  # Abfrage ausführen
    daten = zeiger.fetchall()  # Alle Ergebnisse abrufen fetchall(): Gibt alle Datensätze als Liste von Tupeln zurück.
    verbindung.close()  # Verbindung schließen
    return daten  # Daten zurückgeben
