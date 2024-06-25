from PyQt5 import QtWidgets
from ui_EEBE_Mapa import Ui_Planta_3

class View(QtWidgets.QMainWindow, Ui_Planta_3):
    def __init__(self, presenter=None):
        super().__init__()
        self.setupUi(self)
        self.presenter = presenter
        self.plantas.setEnabled(False)
        self.edificios.currentIndexChanged.connect(self.habilitar_plantas)
        self.edificios.currentIndexChanged.connect(self.cambiar_pag)# Conectar la señal currentIndexChanged del comboBox a un método
        self.plantas.currentIndexChanged.connect(self.cambiar_pag)
        self.OK1.clicked.connect(self.update_labels1)
        self.OK1.clicked.connect(self.update_color)
        self.OK2.clicked.connect(self.update_labels2)
        self.OK2.clicked.connect(self.update_color)
        self.OK3.clicked.connect(self.update_labels3)
        self.OK3.clicked.connect(self.update_color)
        self.BACK1.clicked.connect(self.atras)
        self.BACK2.clicked.connect(self.atras)
        self.BACK3.clicked.connect(self.atras)

    def set_presenter(self, presenter):
        self.presenter = presenter

    def habilitar_plantas(self):
        if self.presenter:
            self.presenter.habilitar_plantas()
    def cambiar_pag(self):
        if self.presenter:
            self.presenter.cambiar_pag()
    def update_labels1(self):
        if self.presenter:
            self.presenter.update_labels1()
    def update_labels2(self):
        if self.presenter:
            self.presenter.update_labels2()

    def update_labels3(self):
        if self.presenter:
            self.presenter.update_labels3()

    def update_color(self):
        if self.presenter:
            self.presenter.update_color()

    def atras(self):
        if self.presenter:
            self.presenter.atras()
