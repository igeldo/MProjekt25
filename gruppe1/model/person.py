from constants.age_range import AgeRange
from constants.biological_sex import BiologicalSex
from constants.pre_condition import PreCondition
from constants.fitness_level import FitnessLevel
from constants.diet_level import DietLevel
from health_conditions import HealthConditions

class Person:
    def __init__(self, name: str, age: AgeRange, biological_sex: BiologicalSex,
                 pre_condition: PreCondition, fitness_level: FitnessLevel, diet_level: DietLevel):
        self._name = name
        self._age = age
        self._biological_sex = biological_sex
        self._health_condition = HealthConditions(pre_condition, fitness_level, diet_level)