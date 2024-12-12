from view import App
from controller import Controller
from Person import Person
from datenbank import add_person


def main():

    app = App()
    controller = Controller(view=app, model=Person)
    app.mainloop()

if __name__ == "__main__":
    main()
