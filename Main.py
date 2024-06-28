# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
import os
from View import View
from Presenter import Presenter
from Model import Model

def main():
    os.environ["QT_SCALE_FACTOR"] = "1.2"  # Variable de entorno para escalar
    app = QtWidgets.QApplication(sys.argv)

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #Habilita el escalado automático de la interfaz de usuario para pantallas de alta DPI
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #Asegura que los pixmaps (imágenes) se escalen correctamente en pantallas de alta DPI.


    model = Model()
    view = View()
    presenter = Presenter(view, model)
    view.set_presenter(presenter)
    view.setWindowTitle("Espai EEBE")
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




