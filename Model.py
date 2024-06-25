import pandas as pd


class Model:
    def __init__(self):
        super().__init__()

    def get_data(self, day, month, year, filepath):
        try:
            # Cargar el archivo Excel
            df = pd.read_excel(filepath)

            # Filtrar los datos según el día, mes y año
            filtered_data = df[(df['Dia'] == int(day)) &
                               (df['Mes'] == int(month)) &
                               (df['Any'] == int(year))]

            if filtered_data.empty:
                raise ValueError(f"No se encontraron datos para la fecha: {day}/{month}/{year}")

            temperatures = {}
            for i in range(1, 16):  # Suponiendo que hay 15 aulas
                temperatures[f'H{i}'] = filtered_data.iloc[0][f'H{i}']
            return temperatures

        except FileNotFoundError:
            print(f"Error: El archivo {filepath} no se ha encontrado.")
            return None
        except ValueError as ve:
            print(ve)
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

