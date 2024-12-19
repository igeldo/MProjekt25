from constants_package.age_range import AgeRange
from constants_package.biological_sex import BiologicalSex
from constants_package.pre_condition import PreCondition
from constants_package.fitness_level import FitnessLevel
from constants_package.diet_level import DietLevel
from health_conditions import HealthConditions

class Person:
    def __init__(self, name: str, age: AgeRange, biological_sex: BiologicalSex,
                 pre_condition: PreCondition, fitness_level: FitnessLevel, diet_level: DietLevel):
        self._name = name
        self._age = age
        self._biological_sex = biological_sex
        self._health_condition = HealthConditions(pre_condition, fitness_level, diet_level)