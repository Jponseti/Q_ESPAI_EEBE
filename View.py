class MainView(QMainWindow, Ui_Planta_3):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.model = TemperatureModel('temperatures_habitacions.xlsx')

        self.dia.addItems([str(i) for i in range(1, 31)])
        self.mes.addItems([str(i) for i in range(1, 13)])
        self.any.addItems(['2024'])
