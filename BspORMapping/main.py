# main.py
from model import Person
from view import PersonView
from controller import PersonController

def main():
    model = Person()
    view = PersonView()
    controller = PersonController(model, view)
    view.run()

if __name__ == "__main__":
    main()

