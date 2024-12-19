from model_package.model import Model
from view_package.view import View

class Control:
    def __init__(self, model: Model, view: View):
        if not isinstance(model, Model) or not isinstance(view, View):
            raise ValueError("Model und View nicht valide.")
        else:
            self.model = model
            self.view = view