from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from View import View
from Presenter import Presenter
from Model import Model

import sys
import pandas as pd
import numpy as np

# Llegir el fitxer Excel
df = pd.read_excel('temperatures_habitacions.xlsx')


# Funció per obtenir la temperatura d'una habitació en una data específica
def obtenir_temperatura(dia, mes, any, aula):
    # Filtrar el DataFrame per la data especificada
    fila = df[(df['Dia'] == dia) & (df['Mes'] == mes) & (df['Any'] == any)]

    # Verificar si s'ha trobat la fila corresponent
    if not fila.empty:
        temperatura = fila[aula].values[0]
        return temperatura
    else:
        return 'No hi ha dades'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('interface.ui', self)

        # Connectar els ComboBox a la funció de canvi
        self.comboBoxdia.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.comboBoxmes.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.comboBoxany.currentIndexChanged.connect(self.actualitzar_temperatures)

        # Inicialitzar els ComboBox amb valors
        self.comboBoxDia.addItems([str(i) for i in range(1, 31)])
        self.comboBoxMes.addItems([str(i) for i in range(1, 13)])
        self.comboBoxAny.addItems(['2024'])

    def actualitzar_temperatures(self):
        # Obtenir les dates seleccionades
        dia = int(self.comboBoxDia.currentText())
        mes = int(self.comboBoxMes.currentText())
        any = int(self.comboBoxAny.currentText())

        # Actualitzar les etiquetes de les temperatures
        for i in range(1, 18):
            aula = f'A{i}'
            temperatura = obtenir_temperatura(dia, mes, any, aula)
            label = getattr(self, f'label{aula}')
            label.setText(f"{temperatura}°C")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


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