import pandas as pd

class Model:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self, day, month, year):
        try:
            # Cargar el archivo Excel
            df = pd.read_excel(self.filepath)

            # Filtrar los datos según el día, mes y año
            filtered_data = df[(df['Dia'] == int(day)) &
                               (df['Mes'] == int(month)) &
                               (df['Any'] == int(year))]

            if not filtered_data.empty:
                temperatures = {}
                for i in range(1, 18):  # Suponiendo que hay 17 aulas
                    temperatures[f'H{i}'] = filtered_data.iloc[0][f'H{i}']
                return temperatures
            else:
                return None
        except Exception as e:
            raise e