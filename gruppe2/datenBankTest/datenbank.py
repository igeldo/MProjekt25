from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Person import Base, Person  # Importiere das Model "Person" und "Base"

# Datenbankverbindung einrichten
DATABASE_URL = "sqlite:///test.db"

# Engine erstellen
engine = create_engine(DATABASE_URL, echo=True)

# Tabellen erstellen (falls nicht vorhanden)
Base.metadata.create_all(engine)

# Session einrichten
Session = sessionmaker(bind=engine)
session = Session()

# Funktionen zur Verwaltung von Personendaten
def add_person(vorname, age, geschlecht, gewicht, size):
    """Fügt eine neue Person zur Datenbank hinzu."""
    neue_person = Person(
        name=vorname,
        age=age,
        sex=geschlecht,
        weight=gewicht,
        height=size
    )
    session.add(neue_person)
    session.commit()
    print(f"Person {vorname} wurde erfolgreich hinzugefügt!")


def get_all_people():
    """Holt alle Personen aus der Datenbank."""
    return session.query(Person).all()