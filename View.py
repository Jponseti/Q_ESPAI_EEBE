from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from ui_mapa import Ui_MainWindow as form_class
import sys


class View(QMainWindow, form_class):
    # la definicion del objeto (QtWidgets.QMainWindow) debera ser la misma que en el Main
    # crear los signals para enviarlos al Presenter
    btncolor = QtCore.pyqtSignal()


    def __init__(self, parent=None):
        # icicializamos el formulario poniendo los componentes a los valores iniciales.
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # poner componentes a su valor inicial

    # definicion de los slots
    def color(self):
        self.btncolor.emit() # se emite la señal para el presenter

    def entrada(self):
        try:
            a = float(self.T_aula1.text())
            return a
        except:
            raise ValueError('error', str(sys.exc_info()[1]))

    def salida(self):
        self.T_aula1.textChanged.connect(self.presenter.temperature_changed)

    def update_color(self):
        if 1 <= int(self.T_aula1.text()) <= 10:
            print(self.T_aula1.text())
            self.aula1.setPixmap(QPixmap("red"))
        elif 10 < int(self.T_aula1.text()) <=  20:
            self.aula1.setStyleSheet("background-color: red")
        else:
            self.aula1.setStyleSheet("")



if __name__ == '__main__':
    V = View()
    input()
