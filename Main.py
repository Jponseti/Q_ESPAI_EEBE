from PyQt5.QtWidgets import QApplication
from View import MainView  # Importem la classe MainView des del fitxer View.py
from Presenter import MainPresenter
from Model import TemperatureModel

def main():
    app = QApplication([])
    model = TemperatureModel('temperatures_habitacions.xlsx')
    view = MainView()  # Creem una instància de MainView
    presenter = MainPresenter(view)
    view.show()
    app.exec_()

if __name__ == "__main__":
    main()
