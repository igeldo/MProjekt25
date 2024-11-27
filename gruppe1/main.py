from view.main_view import Main_view


class Main:
    def __init__(self):
        print("Test Main")

    def run(self):
        main_view = Main_view()
        main_view.ui()
        print("Test_main_run")

if __name__ == '__main__':
    main = Main()
    main.run()