from model_package.model import *
from view_package.view_gui import ViewGUI

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

        # Erstelle eine Person-Instanz und füge sie dem Modell hinzu
        try:
            person = Person(name=name, age=age, biological_sex=biological_sex,
                            pre_conditions=pre_conditions,
                            fitness_level=fitness_level, diet_level=diet_level)
            self.model.add_person(person)
            self.view.set_status(f"Person '{name}' hinzugefügt", "success")
        except ValueError:
            self.view.set_status("Bei der Datenverarbeitung ist etwas schiefgelaufen. "
                                 "Bitte nehmen Sie mit uns Kontakt auf.", "error")