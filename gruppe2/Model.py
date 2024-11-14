

class Person:
    def __init__(self, name, age, sex, weight, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height

    # Getter und Setter für die Klasse Person
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def get_sex(self):
        return self.sex
    def set_sex(self, sex):
        self.sex = sex

    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight

    def get_height(self):
        return self.height
    def set_height(self, height):
        self.height = height

# Berechung des Grundumsatz (bei absoluter körperlicher Ruhe)
def berechne_grundumsatz(self):
    if self.sex == "m":
        grundumsatz = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
    elif self.sex == "w":
        grundumsatz = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
    else:
        raise ValueError("Geschlecht muss 'm' oder 'w' sein.")
    return grundumsatz


class Meals:
    def __init__(self, name_of_meal, ingredients, calories, carbs, protein, fat, vitamin):
        self.name_of_meal = name_of_meal
        self.ingredients = ingredients
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.vitamin = vitamin

# Getter und Setter für die Klasse Meals
def get_name_of_meal(self):
    return self.name_of_meal


class Eating_behaviour(Meals, Person):
    def __init__(self, name_of_meal, time, amount):
        self.name_of_meal = name_of_meal
        self.time = time
        self.amount = amount

    @classmethod
    def add_meal(cls, name_of_meal, time, amount):
        new_meal = cls(name_of_meal, time, amount)
        cls.meal_list.appens(new_meal)
        print(f"Die Mahlzeit '{name_of_meal}' wurde zum '{time}' hinzugefügt.")
