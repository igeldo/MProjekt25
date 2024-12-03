from person import Person

class Model(list[Person]):
    def add_person(self, person: Person):
        if isinstance(person, Person):
            self.append(person)
        else:
            raise ValueError("Nur Objekte der Klasse 'Person' können hinzugefügt werden.")