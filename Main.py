# -*- coding: utf-8 -*-

import sys
import pandas as pd
from PyQt5 import QtWidgets
from ui_EEBE_Mapa import Ui_Planta_3

# Llegir el fitxer Excel
df = pd.read_excel('temperatures_habitacions.xlsx')


# Funció per obtenir la temperatura d'una habitació en una data específica
def obtenir_temperatura(dia, mes, any, habitacio):
    # Filtrar el DataFrame per la data especificada
    fila = df[(df['Dia'] == dia) & (df['Mes'] == mes) & (df['Any'] == any)]

    # Verificar si s'ha trobat la fila corresponent
    if not fila.empty:
        temperatura = fila[habitacio].values[0]
        return temperatura
    else:
        return 'No hi ha dades'


class MainWindow(QtWidgets.QMainWindow, Ui_Planta_3):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Inicialitzar els ComboBox amb valors
        self.dia.addItems([str(i) for i in range(1, 31)])
        self.mes.addItems([str(i) for i in range(1, 13)])
        self.any.addItems(['2024'])

        # Connectar els ComboBox a la funció de canvi
        self.dia.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.mes.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.any.currentIndexChanged.connect(self.actualitzar_temperatures)

    def actualitzar_temperatures(self):
        # Obtenir les dates seleccionades
        dia = int(self.dia.currentText())
        mes = int(self.mes.currentText())
        any = int(self.any.currentText())

        # Actualitzar les etiquetes de les temperatures
        for i in range(1, 18):
            habitacio = f'H{i}'
            temperatura = obtenir_temperatura(dia, mes, any, habitacio)
            label = getattr(self, f'A{i}')
            label.setText(f"{temperatura}°C")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
