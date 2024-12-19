from peewee import SqliteDatabase, Model as PeeweeModel, CharField, IntegerField, FloatField, CompositeKey, \
    ForeignKeyField

# Database connection
db = SqliteDatabase("person_measurements.db")

# ORM Models
class Person(PeeweeModel):
    name = CharField(primary_key=True)
    age = IntegerField()
    blood_type = CharField()

    class Meta:
        database = db

class Measurement(PeeweeModel):
    name = ForeignKeyField(Person, backref='measurements', on_delete='CASCADE')  # Foreign key to Person.name
    hour = IntegerField()
    minute = IntegerField()
    temperature = FloatField()

    class Meta:
        database = db
        primary_key = CompositeKey("name", "hour", "minute")

# Unified Model Class
class Model: # DAO Class
    def __init__(self):
        db.connect()
        db.create_tables([Person, Measurement])

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
