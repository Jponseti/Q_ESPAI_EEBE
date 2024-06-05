from View import View
from Model import TemperatureModel

class Presenter:
    def __init__(self, view):
        self.view = view

        self.view.dia.addItems([str(i) for i in range(1, 31)])
        self.view.mes.addItems([str(i) for i in range(1, 13)])
        self.view.any.addItems(['2024'])

        self.view.dia.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.view.mes.currentIndexChanged.connect(self.actualitzar_temperatures)
        self.view.any.currentIndexChanged.connect(self.actualitzar_temperatures)

    def actualitzar_temperatures(self):
        if self.view.dia.currentText() == '-' or self.view.mes.currentText() == '-' or self.view.any.currentText() == '-':
            return

        day = int(self.view.dia.currentText())
        month = int(self.view.mes.currentText())
        year = int(self.view.any.currentText())

        for i in range(1, 19):  # Ajustament de l'índex superior a 19
            room = f'H{i}'
            temperature = self.view.model.get_temperature(day, month, year, room)
            label = getattr(self.view, f'A{i}')
            label.setText(f"{temperature}°C")
