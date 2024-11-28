from view.view import View


class Main:
    def __init__(self):
        print("Test Main")

    def run(self):
        view = View()
        view.ui()
        print("Test_main_run")

if __name__ == '__main__':
    main = Main()
    main.run()