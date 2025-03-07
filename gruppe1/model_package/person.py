from model_package.constants_package.age_range import AgeRange
from model_package.constants_package.biological_sex import BiologicalSex
from model_package.constants_package.diabetes_ii_chance import AGE_RANGE_CHANCE, BIOLOGICAL_SEX_CHANCE, \
    PRE_CONDITION_CHANCE, FITNESS_LEVEL_CHANCE, DIET_LEVEL_CHANCE
from model_package.constants_package.pre_condition import PreCondition
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.diet_level import DietLevel
from model_package.health_conditions import HealthConditions

class Person:
    def __init__(self, name: str, age: AgeRange, biological_sex: BiologicalSex,
                 pre_conditions: list[PreCondition], fitness_level: FitnessLevel, diet_level: DietLevel):
        if not (isinstance(name, str)
                and isinstance(age, AgeRange)
                and isinstance(biological_sex, BiologicalSex)
                and isinstance(pre_conditions, list)
                and all(isinstance(condition, PreCondition) for condition in pre_conditions)
                and isinstance(fitness_level, FitnessLevel)
                and isinstance(diet_level, DietLevel)):
            raise ValueError("Data types do not match.")
        self._name = name
        self._age = age
        self._biological_sex = biological_sex
        self._health_condition = HealthConditions(pre_conditions, fitness_level, diet_level)
        self._risk = 0
        self.calculate_probability()

    def calculate_probability(self):
        age_chance = AGE_RANGE_CHANCE[self._age]
        sex_chance = BIOLOGICAL_SEX_CHANCE[self._biological_sex]
        fitness_chance = FITNESS_LEVEL_CHANCE[self._health_condition._fitness_level]
        diet_chance = DIET_LEVEL_CHANCE[self._health_condition._diet_level]

        if not PreCondition.NONE == self._health_condition._pre_conditions[0]:
            pre_condition_chance = sum(
                PRE_CONDITION_CHANCE[condition] for condition in self._health_condition._pre_conditions)

            total_probability = (
                    age_chance *
                    sex_chance *
                    pre_condition_chance *
                    (fitness_chance + diet_chance) *
                    100
            )
        else :
            total_probability = (
                    age_chance *
                    sex_chance *
                    (fitness_chance + diet_chance) *
                    100
            )
        self._risk = total_probability

    # # for debugging purposes only
    # def __str__(self):
    #     return (f"Name: {self._name}, Alter: {self._age}, "
    #             f"biologisches Geschlecht: {self._biological_sex}, "
    #             f"Vorerkrankungen: {self._health_condition._pre_conditions}, "
    #             f"Fitnesslevel: {self._health_condition._fitness_level}, "
    #             f"Dietlevel: {self._health_condition._diet_level}, "
    #             f"Risiko: {self._risk: .6f}")