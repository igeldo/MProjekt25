from view_package.view_gui import ViewGUI
from model_package.model import Model
from control_package.control_gui import ControlGUI
from tkinter import Tk

class Main:
    def run(self):
        # instantiate main window
        root = Tk()

        # instantiate mvc parts
        model = Model()
        view = ViewGUI(model, root)
        control = ControlGUI(model, view)

        # control calls methods
        root.mainloop()

        #TODO: Mindestfensterbreite

if __name__ == '__main__':
    main = Main()
    main.run()