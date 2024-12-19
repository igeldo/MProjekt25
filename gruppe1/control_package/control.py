from model_package.model import Model
from model_package.person import Person
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
        person_data = self.view.show_survey()

        # person = Person(person_data)

        # add person to model
        # self.model.add_person(person_data)