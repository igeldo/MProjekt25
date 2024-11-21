

# Bearbeiten
# keine Vererbung sondern Beziehung !!
class Eating_behaviour(Meal, Person):
    def __init__(self, name_of_meal, time, amount):
        self.name_of_meal = name_of_meal
        self.time = time
        self.amount = amount