# from biological_sex import BiologicalSex
# from age_range import AgeRange
# from diet_level import DietLevel
# from fitness_level import FitnessLevel
# from pre_condition import PreCondition

from model_package.constants_package.age_range import AgeRange
from model_package.constants_package.biological_sex import BiologicalSex
from model_package.constants_package.pre_condition import PreCondition
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.diet_level import DietLevel


BIOLOGICAL_SEX_CHANCE = {BiologicalSex.FEMALE: 0.008, BiologicalSex.MALE: 0.015}

AGE_RANGE_CHANCE = {AgeRange.RANGE_18_TO_44: 0.002, AgeRange.RANGE_45_TO_64: 0.016, AgeRange.RANGE_65_TO_79: 0.061}

PRE_CONDITION_CHANCE = {PreCondition.CONDITION_1: 0.291, PreCondition.CONDITION_2: 0.502, PreCondition.OTHER: 0.4461}

FITNESS_LEVEL_CHANCE = {FitnessLevel.LOW: 0.076, FitnessLevel.MID: 0.037, FitnessLevel.HIGH: 0.002}

DIET_LEVEL_CHANCE = {DietLevel.UNHEALTHY: 0.081, DietLevel.MID: 0.019, DietLevel.HEALTHY: 0.007}