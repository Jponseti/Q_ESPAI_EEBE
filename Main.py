from PyQt5.QtWidgets import QApplication
from View import View
from Presenter import Presenter
from Model import Model

def main():
    app = QApplication([])
    model = Model()  # Crear una instància del model
    view = View()
    presenter = Presenter(view, model)  # Passar la vista i el model com a paràmetres al presentador
    view.show()
    app.exec_()

if __name__ == "__main__":
    main()
