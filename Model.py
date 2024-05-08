from math import log10, sqrt

# las funciones puramente de cálculo que no tienen nada que ver con el interfaz grafico
class Model(object):
    def __init__(self):
        self.temperatura = 0

    def set_value(self, temperatura):
        self.temperatura = temperatura

    def get_value(self):
        return self.temperatura