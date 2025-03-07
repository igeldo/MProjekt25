from biological_sex import BiologicalSex
from age_range import AgeRange
from diet_level import DietLevel
from fitness_level import FitnessLevel
from pre_condition import PreCondition

BIOLOGICAL_SEX_CHANCE = {BiologicalSex.FEMALE: 0.008, BiologicalSex.MALE: 0.015}

AGE_RANGE_CHANCE = {AgeRange.RANGE_18_TO_44: 0.002, AgeRange.RANGE_45_TO_64: 0.016, AgeRange.RANGE_65_TO_79: 0.061}

PRE_CONDITION_CHANCE = {PreCondition.CONDITION_1: 0.291, PreCondition.CONDITION_2: 0.502, PreCondition.OTHER: 0.4461}

FITNESS_LEVEL_CHANCE = {FitnessLevel.LOW: 0.076, FitnessLevel.MID: 0.037, FitnessLevel.HIGH: 0.002}

DIET_LEVEL_CHANCE = {DietLevel.UNHEALTHY: 0.081, DietLevel.MID: 0.019, DietLevel.HEALTHY: 0.007}


#
# from enum import Enum
#
#
# class BiologicalSex(Enum):
#     FEMALE = 'female'
#     MALE = 'male'
#
#
# class AgeRange(Enum):
#     RANGE_18_TO_44 = '18-44'
#     RANGE_45_TO_64 = '45-64'
#     RANGE_65_TO_79 = '65-79'
#
#
# class PreCondition(Enum):
#     CONDITION_1 = 'condition_1'
#     CONDITION_2 = 'condition_2'
#     OTHER = 'other'
#     0 = 'none'
#
#
# class FitnessLevel(Enum):
#     LOW = 'low'
#     MID = 'mid'
#     HIGH = 'high'
#
#
# class DietLevel(Enum):
#     UNHEALTHY = 'unhealthy'
#     MID = 'mid'
#     HEALTHY = 'healthy'
#
#
# # Funktion zur Berechnung der Gesamtwahrscheinlichkeit
# def calculate_probability(age_range, biological_sex, pre_conditions, fitness_level, diet_level):
#     age_chance = AGE_RANGE_CHANCE[age_range]
#     sex_chance = BIOLOGICAL_SEX_CHANCE[biological_sex]
#
#     # Summe der Wahrscheinlichkeiten der ausgewählten Vorerkrankungen
#     pre_condition_chance = sum(PRE_CONDITION_CHANCE[condition] for condition in pre_conditions)
#
#     fitness_chance = FITNESS_LEVEL_CHANCE[fitness_level]
#     diet_chance = DIET_LEVEL_CHANCE[diet_level]
#
#     if pre_condition_chance != 0:
#         total_probability = (
#                 age_chance *
#                 sex_chance *
#                 pre_condition_chance *
#                 (fitness_chance + diet_chance) *
#                 100
#         )
#     else :
#         total_probability = (
#                 age_chance *
#                 sex_chance *
#                 (fitness_chance + diet_chance) *
#                 100
#         )
#     return total_probability
#
#
# # Beispielaufruf der Funktion mit mehreren ausgewählten Vorerkrankungen
# selected_pre_conditions = [PreCondition.CONDITION_1, PreCondition.CONDITION_2, PreCondition.OTHER]
# result = calculate_probability(
#     AgeRange.RANGE_45_TO_64,
#     BiologicalSex.MALE,
#     selected_pre_conditions,
#     FitnessLevel.MID,
#     DietLevel.HEALTHY
# )
#
# print(f'Die berechnete Wahrscheinlichkeit ist: {result:.6f}')
#
