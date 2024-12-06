from model.model import Model
from view.view import View

class Control:
    def __init__(self, model: Model, view: View):
        if not isinstance(model, Model) or not isinstance(view, View):
            raise ValueError("Model und View nicht valide.")