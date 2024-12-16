from tkinter import Tk  # For creating the root window
from model import Model  # Import the Model class (handles database and ORM)
from view import View  # Import the View class (handles user interface)
from controller import Controller  # Import the Controller class (mediates Model and View)

if __name__ == "__main__":
    root = Tk()  # Initialize the main Tkinter window
    model = Model()  # Create an instance of the Model
    view = View(root,model)  # Create an instance of the View
    controller = Controller(model, view)  # Create an instance of the Controller
    root.mainloop()  # Start the Tkinter main event loop
