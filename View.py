from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox
from ui_EEBE_Mapa import Ui_Planta_3
from Model import TemperatureModel

class View(QMainWindow, Ui_Planta_3):  # Canviar el nom de la classe a 'View'
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.model = TemperatureModel('temperatures_habitacions.xlsx')

        self.dia.addItems([str(i) for i in range(1, 31)])
        self.mes.addItems([str(i) for i in range(1, 13)])
        self.any.addItems(['2024'])

        self.dia.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.mes.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.any.currentIndexChanged.connect(self.actualitzar_temperatures)

    def actualitzar_temperatures(self):
        if self.dia.currentText() == '-' or self.mes.currentText() == '-' or self.any.currentText() == '-':
            return

        day = int(self.dia.currentText())
        month = int(self.mes.currentText())
        year = int(self.any.currentText())

        for i in range(1, 19):  # Ajustament de l'índex superior a 19
            room = f'H{i}'
            temperature = self.model.get_temperature(day, month, year, room)
            label = getattr(self, f'A{i}')
            label.setText(f"{temperature}°C")
