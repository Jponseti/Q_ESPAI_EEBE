# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from View import View
from Presenter import Presenter
from Model import Model

def main():
    app = QtWidgets.QApplication(sys.argv)
    model = Model("temperatures_habitacions.xlsx")  # Ruta al archivo Excel
    view = View()
    presenter = Presenter(view, model)
    view.set_presenter(presenter)
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
