from model_package.model import *
from view_package.view_gui import ViewGUI

class ControlGUI:
    def __init__(self, model: Model, view: ViewGUI):
        if not isinstance(model, Model) or not isinstance(view, ViewGUI):
            raise ValueError("Model und View nicht valide.")
        else:
            self.model = model
            self.view = view

            # Registriere Callbacks für die Benutzeroberfläche
        self.view.set_callbacks({
            'submit': self.handle_submit,
            'pre_existing_conditions': self.handle_pre_existing_conditions,
        })

    def handle_submit(self, data):
        # Hier konvertieren und speichern wir die Benutzerinformationen
        # Beispiel: Datenextraktion aus dem Argument `data`
        name = data['name']
        age = data['age']
        biological_sex = data['biological_sex']
        pre_existing_conditions = data['pre_existing_conditions']
        fitness_level = data['fitness_level']
        diet_level = data['diet_level']

        # Erstelle eine Person-Instanz und füge sie dem Modell hinzu
        person = Person(name=name, age=age, biological_sex=biological_sex,
                        pre_existing_conditions=pre_existing_conditions,
                        fitness_level=fitness_level, diet_level=diet_level)
        self.model.add_person(person)

    def handle_pre_existing_conditions(self, value):
        if value == "ja":
            self.view.show_pre_existing_conditions_options()
        else:
            self.view.hide_pre_existing_conditions_options()