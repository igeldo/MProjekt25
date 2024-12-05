from constants.diet_level import DietLevel
from constants.fitness_level import FitnessLevel
from constants.pre_condition import PreCondition

class HealthConditions:
    def __init__(self, pre_condition: PreCondition, fitness_level: FitnessLevel, diet_level: DietLevel):
        self._pre_condition = pre_condition
        self._fitness_level = fitness_level
        self._diet_level = diet_level