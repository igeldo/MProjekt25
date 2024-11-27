# model.py
import json
# import os


class Person:
    """Repräsentiert eine einzelne Person."""
    def __init__(self, name, age, height, weight, blood_type):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.blood_type = blood_type

    def __str__(self):
        return (f"Name: {self.name}, Alter: {self.age}, "
                f"Größe: {self.height} cm, Gewicht: {self.weight} kg, Blutgruppe: {self.blood_type}")

    def to_dict(self):
        """Konvertiert die Person in ein Dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "blood_type": self.blood_type
        }

    @staticmethod
    def from_dict(data):
        """Erstellt eine Person aus einem Dictionary."""
        return Person(data["name"], data["age"], data["height"], data["weight"], data["blood_type"])


class PersonList:
    """Verwaltet eine Liste von Personen."""
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        """Fügt eine Person zur Liste hinzu."""
        self.persons.append(person)

    def remove_person(self, index):
        """Entfernt eine Person aus der Liste."""
        if 0 <= index < len(self.persons):
            del self.persons[index]

    def get_all(self):
        """Gibt alle Personen in der Liste zurück."""
        return self.persons

    def save_to_file(self, filename):
        """Speichert die Personenliste in einer JSON-Datei."""
        with open(filename, 'w') as file:
            json.dump([person.to_dict() for person in self.persons], file)
 #           print(f"JSON-Datei wird gespeichert unter: {os.getcwd()}")

    def load_from_file(self, filename):
        """Lädt die Personenliste aus einer JSON-Datei."""
        try:
            with open(filename, 'r') as file:
                self.persons = [Person.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            self.persons = []
