from view_package.view import View
from model_package.model import Model
from control_package.control import Control

class Main:
    def run(self):
        # instantiate mvc parts
        model = Model()
        view = View(model)
        control = Control(model, view)

        # control calls methods
        control.get_input()

if __name__ == '__main__':
    main = Main()
    main.run()