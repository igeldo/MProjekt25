from model_package.constants_package.diet_level import DietLevel
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.pre_condition import PreCondition

class HealthConditions:
    def __init__(self, pre_condition: PreCondition, fitness_level: FitnessLevel, diet_level: DietLevel):
        if not (isinstance(pre_condition, PreCondition)
                and isinstance(fitness_level, FitnessLevel)
                and isinstance(diet_level, DietLevel)):
            raise ValueError("Data types do not match.")
        self._pre_condition = pre_condition
        self._fitness_level = fitness_level
        self._diet_level = diet_level