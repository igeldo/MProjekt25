

class Meal:
    def __init__(self, name_of_meal, ingredients, calories, carbs, protein, fat, vitamin):
        self._name_of_meal = name_of_meal
        self._ingredients = ingredients
        self._calories = calories
        self._carbs = carbs
        self._protein = protein
        self._fat = fat
        self._vitamin = vitamin

    # Getter und Setter für die Klasse Meals
    def get_name_of_meal(self):
        return self.name_of_meal

    def set_name_of_meal(self, name_of_meal):
        self._name_of_meal = name_of_meal

    def get_ingredients(self):
        return self._ingredients

    def set_ingredients(self, ingredients):
        self._ingredients = ingredients

    def get_calories(self):
        return self._calories

    def set_calories(self, calories):
        self._calories = calories

    def get_carbs(self):
        return self._carbs

    def set_carbs(self, carbs):
        self._carbs = carbs

    def get_protein(self):
        return self._protein

    def set_protein(self, protein):
        self._protein = protein

    def get_fat(self):
        return self._fat

    def set_fat(self, fat):
        self._fat = fat

    def get_vitamin(self):
        return self._vitamin

    def set_vitamin(self, vitamin):
        self._vitamin = vitamin

 #@classmethod
  #  def add_meal(cls, name_of_meal, time, amount):
   #     new_meal = cls(name_of_meal, time, amount)
    #    cls.meal_list.appens(new_meal)
     #   print(f"Die Mahlzeit '{name_of_meal}' wurde zum '{time}' hinzugefügt.")

