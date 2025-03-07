from model_package.person import Person

class Model:
    def add_person(self, person: Person):
        if isinstance(person, Person):
            self._person_list.append(person)
        else:
            raise ValueError("Type does not match.")

    _person_list = []

    def get_person_list(self):
        return self._person_list