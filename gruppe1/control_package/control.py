from model_package.model import *
from model_package.constants_package.age_range import AgeRange
from model_package.constants_package.diet_level import DietLevel
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.biological_sex import BiologicalSex
from model_package.constants_package.pre_condition import PreCondition
from view_package.view import View

class Control:
    def __init__(self, model: Model, view: View):
        if not isinstance(model, Model) or not isinstance(view, View):
            raise ValueError("Model und View nicht valide.")
        else:
            self.model = model
            self.view = view

    def get_input(self):
        # get person data
        name, age, biological_sex, pre_existing_conditions, fitness_level, diet_level = map(str, self.view.show_survey())
        #TODO exception handling

        # conversions
        age = AgeRange.str_to_age_range(age)
        biological_sex = BiologicalSex.str_to_biological_sex(biological_sex)
        pre_existing_conditions = PreCondition.str_to_pre_condition(pre_existing_conditions)
        fitness_level = FitnessLevel.str_to_fitness_level(fitness_level)
        diet_level = DietLevel.str_to_diet_level(diet_level)

        person = Person(name, age, biological_sex, pre_existing_conditions, fitness_level, diet_level)

        # add person to model
        self.model.add_person(person)