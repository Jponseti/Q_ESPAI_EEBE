# Aqui esta el codigo que conecta View con Model
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtGui import QColor

class Presenter(object):
    # Pasar el View y el Model dentro del Presenter
    def __init__(self, view,model):
        self.vista = view
        self.modelo = model
        #captura de las señales del View y conectando con funciones del Presenter
        #self.vista.btncolor.connect(self.update_model) #Conecta del View


    # Funciones del Presenter
    def temperature_changed(self,temperatura):
        try:
            temperatura = float(temperatura)
            self.model.set_temperatura(int(temperatura))
            self.update_color()
        except ValueError as err:
            self.vista.mensaje('Error', str(err))


    #def update_color(self, temperatura):
       # if 1 <= temperatura <= 10:
      #      self.view.aula1.setStyleSheet("background-color: blue")
       # elif 10 < temperatura <= 20:
       #     self.view.aula1.setStyleSheet("background-color: red")
      #  else:
       #     self.view.aula1.setStyleSheet("")

    def mensaje(self,prompt,txt):
        QMessageBox.information(self,'Error',txt)
