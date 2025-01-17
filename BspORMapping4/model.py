from peewee import PostgresqlDatabase, Model, CharField, IntegerField, FloatField, ForeignKeyField, CompositeKey

# PostgreSQL-Datenbankverbindung definieren
db = PostgresqlDatabase(
    'person_measurements.db',  # Name der Datenbank
    user='user',  # Benutzername
    password='password',  # Passwort
    host='localhost',  # Host (z. B. localhost oder IP)
    port=5432  # Standard-Port für PostgreSQL
)

# ORM Models
# Basismodell definieren
class BaseModel(Model):
    class Meta:
        database = db  # Verknüpfe alle Modelle mit der PostgreSQL-Datenbank

# Tabelle: Person
class Person(BaseModel):
    name = CharField(primary_key=True)  # Primärschlüssel: Name der Person
    age = IntegerField()  # Alter der Person
    blood_type = CharField()  # Blutgruppe der Person

# Tabelle: Measurement
class Measurement(BaseModel):
    name = ForeignKeyField(Person, backref='measurements', on_delete='CASCADE')  # Fremdschlüssel zu Person.name
    hour = IntegerField()  # Stunde der Messung
    minute = IntegerField()  # Minute der Messung
    temperature = FloatField()  # Temperaturmessung

    class Meta:
        primary_key = CompositeKey('name', 'hour', 'minute')  # Zusammengesetzter Primärschlüssel
# Unified Model Class
# DAO-Klasse
class Model:
    def __init__(self):
        db.connect()
        db.create_tables([Person, Measurement])
        # Tabellen in der Datenbank auflisten
        # tables = db.get_tables()
        # print(tables)

    def add_or_update_person(self, name, age, blood_type):
        person, created = Person.get_or_create(name=name, defaults={"age": age, "blood_type": blood_type})
        if not created:
            person.age = age
            person.blood_type = blood_type
            person.save()

    def delete_person(self, name):
        person = Person.get_or_none(Person.name == name)
        if person:
            person.delete_instance(recursive=True)  # Deletes person and related measurements

    def get_all_people(self):
        return [{"name": p.name, "age": p.age, "blood_type": p.blood_type} for p in Person.select()]

    def add_or_update_measurement(self, name, hour, minute, temperature):
        measurement, created = Measurement.get_or_create(
            name=name, hour=hour, minute=minute, defaults={"temperature": temperature}
        )
        if not created:
            measurement.temperature = temperature
            measurement.save()

    def delete_measurement(self, name, hour, minute):
        Measurement.delete().where(
            (Measurement.name == name) & (Measurement.hour == hour) & (Measurement.minute == minute)
        ).execute()

    def get_measurements_for_person(self, name):
        return [
            {"hour": m.hour, "minute": m.minute, "temperature": m.temperature}
            for m in Measurement.select().where(Measurement.name == name)
        ]
