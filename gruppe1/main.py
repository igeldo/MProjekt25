from view.view import View
from model.model import Model
from control.control import Control


class Main:
    def run(self):
        # instantiate mvc parts
        model = Model()
        view = View()
        control = Control(view, model)

        # control calls methods


if __name__ == '__main__':
    main = Main()
    main.run()