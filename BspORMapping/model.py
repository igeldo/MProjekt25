from peewee import SqliteDatabase, Model, CharField, IntegerField, FloatField, ForeignKeyField, CompositeKey

# Database configuration
DATABASE_NAME = "person_measurements.db"
db = SqliteDatabase(DATABASE_NAME)

# Table 1: Person
class Person(Model):
    name = CharField(primary_key=True)  # Name is the primary key
    age = IntegerField()
    blood_type = CharField()

    class Meta:
        database = db

# Table 2: Measurements
class Measurements(Model):
    name = ForeignKeyField(Person, backref='measurements', on_delete='CASCADE')  # Foreign key to Person.name
    hour = IntegerField()
    minute = IntegerField()
    body_temperature = FloatField()

    class Meta:
        database = db
        primary_key = CompositeKey('name', 'hour', 'minute')  # Composite primary key

# Initialize the database
db.connect()
db.create_tables([Person, Measurements])

# Database Access Methods
def add_or_update_person(name, age, blood_type):
    person, created = Person.get_or_create(name=name, defaults={"age": age, "blood_type": blood_type})
    if not created:
        person.age = age
        person.blood_type = blood_type
        person.save()
    return person

def add_or_update_measurement(name, hour, minute, body_temperature):
    try:
        person = Person.get(Person.name == name)
        measurement, created = Measurements.get_or_create(
            name=person, hour=hour, minute=minute, defaults={"body_temperature": body_temperature}
        )
        if not created:
            measurement.body_temperature = body_temperature
            measurement.save()
        return measurement
    except Person.DoesNotExist:
        raise ValueError(f"Person with name '{name}' does not exist.")

def delete_person(name):
    person = Person.get_or_none(Person.name == name)
    if person:
        person.delete_instance(recursive=True)  # Deletes person and related measurements

def delete_measurement(name, hour, minute):
    measurement = Measurements.get_or_none(name=name, hour=hour, minute=minute)
    if measurement:
        measurement.delete_instance()

def get_all_people():
    return list(Person.select())

def get_measurements_for_person(name):
    return list(Measurements.select().where(Measurements.name == name))
