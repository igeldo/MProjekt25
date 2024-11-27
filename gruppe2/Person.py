

class Person:
    def __init__(self, name, age, sex, weight, height):
        self._name = name
        self._age = age
        self._sex = sex
        self._weight = weight
        self._height = height

    # Getter und Setter für die Klasse Person
    def get_name(self):
        return self.name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self._age = age

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self._sex = sex

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        return self.height

    def set_height(self, height):
        self._height = height
