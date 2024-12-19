from model_package.person import Person

class Model(list[Person]):
    def add_person(self, person: Person):
        if isinstance(person, Person):
            self.append(person)
        else:
            raise ValueError("Nur Objekte der Klasse 'Person' können hinzugefügt werden.")

    # def get_person(self, index):
    #     if index < 0 or index >= len(self):
    #         raise IndexError("Index liegt außerhalb der Grenzen der Liste.")
    #     return self[index]