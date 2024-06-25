from PyQt5.QtCore import QObject

class Presenter(QObject):
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

    def habilitar_plantas(self):
        if self.view.edificios.currentIndex() != 0:  # Asumiendo que el índice 0 es la opción por defecto
            self.view.plantas.setEnabled(True)
        else:
            self.view.plantas.setEnabled(False)
            self.view.plantas.setCurrentIndex(0)
    def cambiar_pag(self):
        if self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 1:  # Cambiar estos índices según corresponda
            self.view.stackedWidget.setCurrentIndex(1)  # Cambia a la segunda página
            self.view.tabWidget.setCurrentIndex(0)  # Selecciona la primera pestaña del tabWidget
        elif self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 2:
            self.view.stackedWidget.setCurrentIndex(1)
            self.view.tabWidget.setCurrentIndex(1)  # Selecciona la segunda pestaña del tabWidget
        elif self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 3:
            self.view.stackedWidget.setCurrentIndex(1)
            self.view.tabWidget.setCurrentIndex(2)  # Selecciona la tercera pestaña del tabWidget
        else:
            self.view.stackedWidget.setCurrentIndex(0)  # Volver a la primera página si las condiciones no se cumplen

    def update_labels1(self):
        dia = self.view.dia1.currentText()
        mes = self.view.mes1.currentText()
        anyo = self.view.any1.currentText()

        try:
            data1 = self.model.get_data(dia, mes, anyo, "tempaulesP1.xlsx")
        except Exception as e:
            print(f"Error loading data: {e}")
            return

        if data1 is None:
            return

        for i in range(1, 16):
            label_name = f"A1{i}"
            try:
                label = getattr(self.view, label_name)
                label.setText(str(data1.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError: {e}")

    def update_labels2(self):

        dia = self.view.dia2.currentText()
        mes = self.view.mes2.currentText()
        anyo = self.view.any2.currentText()

        try:
            data2 = self.model.get_data(dia, mes, anyo, "tempaulesP2.xlsx")
        except Exception as e:
            print(f"Error loading data: {e}")
            return

        if data2 is None:
            return

        for i in range(1, 16):
            label_name = f"A2{i}"
            try:
                label = getattr(self.view, label_name)
                label.setText(str(data2.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError: {e}")


    def update_labels3(self):

        dia = self.view.dia3.currentText()
        mes = self.view.mes3.currentText()
        anyo = self.view.any3.currentText()

        try:
            data3 = self.model.get_data(dia, mes, anyo, "tempaulesP3.xlsx")
        except Exception as e:
            print(f"Error loading data: {e}")
            return

        if data3 is None:
            return

        for i in range(1, 12):
            label_name = f"A3{i}"
            try:
                label = getattr(self.view, label_name)
                label.setText(str(data3.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError: {e}")


    def update_color(self):
        for i in range(1, 16):
            temp_label_name = f"A1{i}"
            color_label_name = f"colorA1{i}"
            try:
                temp_label = getattr(self.view, temp_label_name)
                color_label = getattr(self.view, color_label_name)
                temp = temp_label.text()
                if temp:
                    temp = float(temp)
                    if temp <= 17: #Lila
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(45, 0, 154, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 17 < temp <= 18: #Blau fort
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 54, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 18 < temp <= 19: #Blau fluix
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 217, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 19 < temp <= 20: #Verd
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 239, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 20 < temp <= 21:  # Groc
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(0, 255, 87, 255), stop: 0.982955 rgba(255, 255, 255, 255))")
                    elif 21 < temp <= 22:#Taronja
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 152, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 22 < temp <= 23: #Vermell
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
                    elif 22 < temp <= 23: #Vermell fort
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(177, 0, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    else: #Fucsia
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(223, 0, 180, 255), stop:0.982955 rgba(255, 255, 255, 255))")

            except AttributeError as e:
                print(f"AttributeError: {e}")

        for i in range(1, 16):
            temp_label_name = f"A2{i}"
            color_label_name = f"colorA2{i}"
            try:
                temp_label = getattr(self.view, temp_label_name)
                color_label = getattr(self.view, color_label_name)
                temp = temp_label.text()
                if temp:
                    temp = float(temp)
                    if temp <= 10:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 54, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 10 < temp <= 16:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 217, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 16 < temp <= 19:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 239, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 19 < temp <= 24:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 152, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 24 < temp <= 30:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
                    else:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(177, 0, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
            except AttributeError as e:
                print(f"AttributeError: {e}")

        for i in range(1, 12):
            temp_label_name = f"A3{i}"
            color_label_name = f"colorA3{i}"
            try:
                temp_label = getattr(self.view, temp_label_name)
                color_label = getattr(self.view, color_label_name)
                temp = temp_label.text()
                if temp:
                    temp = float(temp)
                    if temp <= 10:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 54, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 10 < temp <= 16:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0, 217, 255, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 16 < temp <= 19:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 239, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 19 < temp <= 24:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255, 152, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
                    elif 24 < temp <= 30:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
                    else:
                        color_label.setStyleSheet(
                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(177, 0, 0, 255), stop:0.982955 rgba(255, 255, 255, 255))")
            except AttributeError as e:
                print(f"AttributeError: {e}")

    def atras(self):
        # Limpiar temperaturas y colores de la planta 1
        for i in range(1, 16):
            label_name = f"A1{i}"
            color_label_name = f"colorA1{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError: {e}")

        # Limpiar temperaturas y colores de la planta 2
        for i in range(1, 16):
            label_name = f"A2{i}"
            color_label_name = f"colorA2{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError: {e}")

        # Limpiar temperaturas y colores de la planta 3
        for i in range(1, 12):
            label_name = f"A3{i}"
            color_label_name = f"colorA3{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError: {e}")

        self.view.dia1.setCurrentIndex(0)
        self.view.dia2.setCurrentIndex(0)
        self.view.dia3.setCurrentIndex(0)
        self.view.mes1.setCurrentIndex(0)
        self.view.mes2.setCurrentIndex(0)
        self.view.mes3.setCurrentIndex(0)
        self.view.any1.setCurrentIndex(0)
        self.view.any2.setCurrentIndex(0)
        self.view.any3.setCurrentIndex(0)

        self.view.edificios.setCurrentIndex(0)
        self.view.plantas.setCurrentIndex(0)
        self.view.plantas.setEnabled(False)
        self.view.stackedWidget.setCurrentIndex(0)
