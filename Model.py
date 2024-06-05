import pandas as pd

class TemperatureModel:
    def __init__(self, filename):
        self.df = pd.read_excel(filename)

    def get_temperature(self, day, month, year, room):
        row = self.df[(self.df['Dia'] == day) & (self.df['Mes'] == month) & (self.df['Any'] == year)]
        if not row.empty:
            temperature = row[room].values[0]
            return temperature
        else:
            return 'No hi ha dades'
