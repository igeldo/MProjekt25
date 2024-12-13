# main.py
from model import PersonList
from view import PersonView
from controller import PersonController

def main():
    model = PersonList()
    view = PersonView(model)
    controller = PersonController(model, view)
    view.run()

if __name__ == "__main__":
    main()
