from PyQt5.QtCore import QObject

class Presenter(QObject):
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

    def habilitar_plantas(self):
        if self.view.edificios.currentIndex() != 0:
            self.view.plantas.setEnabled(True)
        else:
            self.view.plantas.setEnabled(False)
            self.view.plantas.setCurrentIndex(0)

    def cambiar_pag(self):
        if self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 1:
            self.view.stackedWidget.setCurrentIndex(1)
            self.view.tabWidget.setCurrentIndex(0)
        elif self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 2:
            self.view.stackedWidget.setCurrentIndex(1)
            self.view.tabWidget.setCurrentIndex(1)
        elif self.view.edificios.currentIndex() == 1 and self.view.plantas.currentIndex() == 3:
            self.view.stackedWidget.setCurrentIndex(1)
            self.view.tabWidget.setCurrentIndex(2)
        else:
            self.view.stackedWidget.setCurrentIndex(0)

    def update_labels1(self):
        dia = self.view.dia1.currentText()
        mes = self.view.mes1.currentText()
        anyo = self.view.any1.currentText()
        filepath = "temperatures_planta1.xlsx"

        self.model.data_junto(dia, mes, anyo)
        try:
            data1 = self.model.get_data(filepath)
        except Exception as e:
            print(f"Error en data P1: {e}")
            return

        if data1 is None:
            return

        planta1 = self.model.edificio.plantas[0]
        for i, aula in enumerate(planta1.aulas, start=1):
            try:
                label = getattr(self.view, aula.nombre)
                label.setText(str(data1.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError en P1: {e}")

    def update_labels2(self):
        dia = self.view.dia2.currentText()
        mes = self.view.mes2.currentText()
        anyo = self.view.any2.currentText()
        filepath = "temperatures_planta2.xlsx"

        self.model.data_junto(dia, mes, anyo)
        try:
            data2 = self.model.get_data(filepath)
        except Exception as e:
            print(f"Error en data P2: {e}")
            return

        if data2 is None:
            return

        planta2 = self.model.edificio.plantas[1]
        for i, aula in enumerate(planta2.aulas, start=1):
            try:
                label = getattr(self.view, aula.nombre)
                label.setText(str(data2.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError en P2: {e}")


    def update_labels3(self):
        dia = self.view.dia3.currentText()
        mes = self.view.mes3.currentText()
        anyo = self.view.any3.currentText()
        filepath = "temperatures_planta3.xlsx"

        self.model.data_junto(dia, mes, anyo)
        try:
            data3 = self.model.get_data(filepath)
        except Exception as e:
            print(f"Error en data P3: {e}")
            return

        if data3 is None:
            return

        planta3 = self.model.edificio.plantas[2]
        for i, aula in enumerate(planta3.aulas, start=1):
            try:
                label = getattr(self.view, aula.nombre)
                label.setText(str(data3.get(f"H{i}", "")))
            except AttributeError as e:
                print(f"AttributeError en P3: {e}")

    def update_color(self):
        def update_color_planta(planta, prefijo):
            for i, aula in enumerate(planta.aulas, start=1):
                temp_label_name = aula.nombre
                color_label_name = f"color{prefijo}{i}"
                try:
                    temp_label = getattr(self.view, temp_label_name)
                    color_label = getattr(self.view, color_label_name)
                    temp = temp_label.text()
                    if temp:
                        temp = float(temp)
                        if temp <= 17:  # Lila
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(89,0,127,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        elif 17 < temp <= 18:  # Blau fort
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0,127,255,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        elif 18 < temp <= 19:  # Blau fluix
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(0,255,255,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        elif 19 < temp <= 20:  # Verd
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(102,191,38,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        elif 20 < temp <= 21:  # Groc
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(255,255,0,255), stop: 0.982955 rgba(255, 255, 255, 255))")
                        elif 21 < temp <= 22:  # Taronja
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.193182 rgba(255,114,0,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        elif 22 < temp <= 23:  # Vermell
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
                        elif 23 < temp <= 24:  # Vermell fort
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(127,0,44,255), stop:0.982955 rgba(255, 255, 255, 255))")
                        else:  # Fucsia
                            color_label.setStyleSheet(
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.255682 rgba(255,0,255,255), stop:0.982955 rgba(255, 255, 255, 255))")

                except AttributeError as e:
                    print(f"AttributeError en colores: {e}")

        update_color_planta(self.model.edificio.plantas[0], "A1")
        update_color_planta(self.model.edificio.plantas[1], "A2")
        update_color_planta(self.model.edificio.plantas[2], "A3")

    def atras(self):
        planta1 = self.model.edificio.plantas[0]
        for i, aula in enumerate(planta1.aulas, start=1):
            label_name = aula.nombre
            color_label_name = f"colorA1{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError en P1: {e}")

        planta2 = self.model.edificio.plantas[1]
        for i, aula in enumerate(planta2.aulas, start=1):
            label_name = aula.nombre
            color_label_name = f"colorA2{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError en P2: {e}")

        planta3 = self.model.edificio.plantas[2]
        for i, aula in enumerate(planta3.aulas, start=1):
            label_name = aula.nombre
            color_label_name = f"colorA3{i}"
            try:
                temp_label = getattr(self.view, label_name)
                color_label = getattr(self.view, color_label_name)
                temp_label.setText("")
                color_label.setStyleSheet("")
            except AttributeError as e:
                print(f"AttributeError en P3: {e}")

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

