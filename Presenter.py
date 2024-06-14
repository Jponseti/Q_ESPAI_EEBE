# Aqui esta el codigo que conecta View con Model
from PyQt5.QtCore import QObject
from Model import Model

class Presenter(QObject):
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

    def update_labels(self):
        dia = self.view.dia.currentText()
        mes = self.view.mes.currentText()
        anyo = self.view.any.currentText()

        datos_filtrados = self.model.get_data(dia, mes, anyo)

        if datos_filtrados is None:
            return

        self.view.A1.setText(str(datos_filtrados.get("H1", "")))
        self.view.A2.setText(str(datos_filtrados.get("H2", "")))
        self.view.A3.setText(str(datos_filtrados.get("H3", "")))
        self.view.A4.setText(str(datos_filtrados.get("H4", "")))
        self.view.A5.setText(str(datos_filtrados.get("H5", "")))
        self.view.A6.setText(str(datos_filtrados.get("H6", "")))
        self.view.A7.setText(str(datos_filtrados.get("H7", "")))
        self.view.A8.setText(str(datos_filtrados.get("H8", "")))
        self.view.A9.setText(str(datos_filtrados.get("H9", "")))
        self.view.A10.setText(str(datos_filtrados.get("H10", "")))
        self.view.A11.setText(str(datos_filtrados.get("H11", "")))
        self.view.A12.setText(str(datos_filtrados.get("H12", "")))
        self.view.A13.setText(str(datos_filtrados.get("H13", "")))
        self.view.A14.setText(str(datos_filtrados.get("H14", "")))
        self.view.A15.setText(str(datos_filtrados.get("H15", "")))
        self.view.A16.setText(str(datos_filtrados.get("H16", "")))
        self.view.A17.setText(str(datos_filtrados.get("H17", "")))