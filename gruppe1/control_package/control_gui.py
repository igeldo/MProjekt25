from model_package.model import *
from view_package.view_gui import ViewGUI
from model_package.constants_package.age_range import AgeRange
from model_package.constants_package.diet_level import DietLevel
from model_package.constants_package.fitness_level import FitnessLevel
from model_package.constants_package.biological_sex import BiologicalSex
from model_package.constants_package.pre_condition import PreCondition

class ControlGUI:
    def __init__(self, model: Model, view: ViewGUI):
        if not isinstance(model, Model):
            raise ValueError("Model nicht valide.")
        elif not isinstance(view, ViewGUI):
            raise ValueError("View nicht valide.")

        # dependency injection
        self.model = model
        self.view = view

        # bind buttons to methods
        self.view.add_person_button.config(command=self.add_person)
        self.view.button_switch_to_display.config(command=self.show_results)
        self.view.button_switch_to_form.config(command=self.show_form)

    def add_person(self):
        # Hier konvertieren und speichern wir die Benutzerinformationen
        # Beispiel: Datenextraktion aus dem Argument `data`
        data = self.view.get_inputs()
        name = data['name']
        age = data['age']
        biological_sex = data['biological_sex']
        pre_conditions = data['pre_conditions']
        fitness_level = data['fitness_level']
        diet_level = data['diet_level']

        # print(name)
        # print(age)
        # print(biological_sex)
        # print(pre_conditions)
        # print(fitness_level)
        # print(diet_level)
        #
        # print("-------------------------------------------------------------- test ---------------------------------")

        if not (name and age and biological_sex and pre_conditions and fitness_level and diet_level):
            self.view.set_status("Bitte alles ausfüllen!", "error")
            return

        # if not name:
        #     raise ValueError("Bitte geben Sie Ihren Namen an!")
        # if "None" == age:
        #     raise ValueError("Bitte geben Sie Ihr Alter an!")
        # if "None" == biological_sex:
        #     raise ValueError("Bitte geben Sie Ihr biologisches Geschlecht an!")
        # if "None" == pre_conditions:
        #     raise ValueError("Bitte geben Sie an, ob Sie Vorerkrankungen haben!")
        # if "None" == fitness_level:
        #     raise ValueError("Bitte geben Sie Ihren Fitnesslevel an!")
        # if "None" == diet_level:
        #     raise ValueError("Bitte geben Sie Ihre Diät an!")

        # print(age_enum)
        # print(biological_sex_enum)
        # print(pre_conditions_enum)
        # print(fitness_level_enum)
        # print(diet_level_enum)

        try:
            age_enum = AgeRange.string_to_enum(age)
            biological_sex_enum = BiologicalSex.string_to_enum(biological_sex)
            pre_conditions_arguments = [pre_condition.strip() for pre_condition in pre_conditions.split(",")]
            pre_conditions_enum = [PreCondition.string_to_enum(pre_condition) for pre_condition in
                                   pre_conditions_arguments]
            fitness_level_enum = FitnessLevel.string_to_enum(fitness_level)
            diet_level_enum = DietLevel.string_to_enum(diet_level)

            person = Person(name=name, age=age_enum, biological_sex=biological_sex_enum,
                            pre_conditions=pre_conditions_enum,
                            fitness_level=fitness_level_enum, diet_level=diet_level_enum)
            self.model.add_person(person)
            self.view.set_status(f"Person '{name}' hinzugefügt", "success")
        except ValueError:
            self.view.set_status("Bei der Datenverarbeitung ist etwas schiefgelaufen. "
                                 "Bitte nehmen Sie mit uns Kontakt auf.", "error")


    def show_results(self):
        # calcs
        self.view.show_all_results()
        self.view.show_display_frame()


    def show_form(self):
        # clear
        self.view.show_form_frame()