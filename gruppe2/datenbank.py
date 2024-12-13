from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Erzeugt die Basis-Klasse für das ORM
Base = declarative_base()

class Person(Base):
    __tablename__ = 'personen'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vorname = Column(String)
    alter = Column(Integer)
    geschlecht = Column(String)
    gewicht = Column(Float)
    groeße = Column(Float)

# Erstellen der SQLite-Datenbank
engine = create_engine('sqlite:///kalorien_tracker.db')
Base.metadata.create_all(engine)

# Erzeugt eine Session-Klasse
Session = sessionmaker(bind=engine)
session = Session()

def add_person(vorname, alter, geschlecht, gewicht, groeße):
    try:
        neue_person = Person(
            vorname=vorname,
            alter=alter,
            geschlecht=geschlecht,
            gewicht=gewicht,
            groeße=groeße
        )
        session.add(neue_person)
        session.commit()
    except Exception as e:
        session.rollback()
        raise