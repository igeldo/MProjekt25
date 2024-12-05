from biological_sex import BiologicalSex
from age_range import AgeRange
from diet_level import DietLevel
from fitness_level import FitnessLevel
from pre_condition import PreCondition

#TODO: look up actual data



BIOLOGICAL_SEX_CHANCE = {BiologicalSex.FEMALE: 0.01 , BiologicalSex.MALE: 0.02}

# TODO: other ranges
AGE_RANGE_CHANCE = {AgeRange.RANGE_18_TO_25: 0.0001 , AgeRange.RANGE_28_TO_37: 0.0008}

#TODO: other conditions: 'Schilddrüsenunterfunktion', 'Bluthochdruck', ...
PRE_CONDITION_CHANCE = {PreCondition.CONDITION_1: 0.02 , PreCondition.CONDITION_2: 0.04 , PreCondition.OTHER: 0.1}

FITNESS_LEVEL_CHANCE = {FitnessLevel.LOW: 0.006 , FitnessLevel.MID: 00.3 , FitnessLevel.HIGH: 0.001}

DIET_LEVEL_CHANCE = {DietLevel.UNHEALTHY: 0.01 , DietLevel.MID: 0.004 , DietLevel.HEALTHY: 0.001}

