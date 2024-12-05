from view.view import View
from model.model import Model


class Main:
    def run(self):
        view = View()
        view.ui()
        # print("Test_main_run")

if __name__ == '__main__':
    main = Main()
    main.run()