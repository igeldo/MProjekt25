from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'  # Name der Tabelle in der Datenbank

    # Spalten in der Tabelle
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)  # "M" für männlich, "F" für weiblich
    weight = Column(Float, nullable=False)  # Gewicht in kg
    height = Column(Float, nullable=False)  # Größe in cm
    # created_at = Column(DateTime, default=datetime.utcnow)  # Zeitstempel

    # Konstruktor wird durch ORM automatisch verwaltet, kann aber erweitert werden
    def __repr__(self):
        return f"<Person(name={self.name}, age={self.age}, sex={self.sex}, weight={self.weight}, height={self.height})>"

# Verbindung zur SQLite-Datenbank herstellen
engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)  # Erstellt die Tabellen, falls sie noch nicht existieren

# Session einrichten
Session = sessionmaker(bind=engine)
session = Session()

# CRUD-Operationen
def create_person(name, age, sex, weight, height):
    """Erstellt eine neue Person und speichert sie in der Datenbank."""
    new_person = Person(name=name, age=age, sex=sex, weight=weight, height=height)
    session.add(new_person)
    session.commit()
    print(f"Person {name} wurde erstellt!")

def get_all_persons():
    """Gibt alle Personen aus der Datenbank zurück."""
    return session.query(Person).all()

def find_person_by_name(name):
    """Findet eine Person nach Name."""
    return session.query(Person).filter(Person.name == name).first()


def update_person(name, **kwargs):
    """Aktualisiert die Daten einer Person basierend auf ihrem Namen."""
    person = find_person_by_name(name)
    if not person:
        print(f"Person {name} nicht gefunden!")
        return

    for key, value in kwargs.items():
        if hasattr(person, key):
            setattr(person, key, value)
    session.commit()
    print(f"Person {name} wurde aktualisiert!")

def delete_person(name):
    """Löscht eine Person aus der Datenbank."""
    person = find_person_by_name(name)
    if person:
        session.delete(person)
        session.commit()
        print(f"Person {name} wurde gelöscht!")
    else:
        print(f"Person {name} nicht gefunden!")