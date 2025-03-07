from model_package.constants_package.age_range import AgeRange
from model_package.constants_package.biological_sex import BiologicalSex
from model_package.constants_package.pre_condition import PreCondition
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.diet_level import DietLevel
from model_package.health_conditions import HealthConditions

class Person:
    def __init__(self, name: str, age: AgeRange, biological_sex: BiologicalSex,
                 pre_conditions: PreCondition, fitness_level: FitnessLevel, diet_level: DietLevel):
        if not (isinstance(name, str)
                and isinstance(age, AgeRange)
                and isinstance(biological_sex, BiologicalSex)
                and isinstance(pre_conditions, PreCondition)
                and isinstance(fitness_level, FitnessLevel)
                and isinstance(diet_level, DietLevel)):
            raise ValueError("Bei der Datenverarbeitung ist etwas schiefgelaufen. "
                             "Bitte nehmen Sie mit uns Kontakt auf.")
        self._name = name
        self._age = age
        self._biological_sex = biological_sex
        self._health_condition = HealthConditions(pre_conditions, fitness_level, diet_level)

    # for debugging purposes only
    def __str__(self):
        return (f"Name: {self._name}, Alter: {self._age}, "
                f"biologisches Geschlecht: {self._biological_sex}, "
                f"Vorerkrankungen: {self._health_condition._pre_condition}, "
                f"Fitnesslevel: {self._health_condition._fitness_level}, "
                f"Dietlevel: {self._health_condition._diet_level}")