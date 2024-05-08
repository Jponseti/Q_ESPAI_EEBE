from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from View import View
from Presenter import Presenter
from Model import Model


class Principal(QMainWindow):
    # la definicion del objeto (QtWidgets.QMainWindow) debera ser la misma que en el View
    def __init__(self, parent=None):
        super().__init__(parent)

        self.window = QMainWindow()
        self.my_view = View()
        self.my_model = Model()
        self.my_presenter = Presenter(self.my_view, self.my_model)
        self.setCentralWidget(self.my_view)
        self.setWindowTitle("Espai EEBE")


def get_qapplication_instance():
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)
    return app


if __name__ == '__main__':
    app = get_qapplication_instance()
    window = Principal()
    window.resize(470,255)
    window.show()
    app.exec_()