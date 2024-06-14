from PyQt5 import QtWidgets
from ui_EEBE_Mapa import Ui_Planta_3

class View(QtWidgets.QMainWindow, Ui_Planta_3):
    def __init__(self, presenter=None):
        super().__init__()
        self.setupUi(self)
        self.presenter = presenter
        self.OK.clicked.connect(self.update_labels)

    def set_presenter(self, presenter):
        self.presenter = presenter

    def update_labels(self):
        if self.presenter:
            self.presenter.update_labels()