import pandas as pd

class Aula:
    def __init__(self, nombre, planta):
        self.nombre = nombre
        self.planta = planta

class Planta:
    def __init__(self, nombre, aulas=None):
        self.nombre = nombre
        self.aulas = aulas if aulas is not None else []

    def agregar_aula(self, aula):
        self.aulas.append(aula)

class Edificio:
    def __init__(self, nombre, plantas=None):
        self.nombre = nombre
        self.plantas = plantas if plantas is not None else []

    def agregar_planta(self, planta):
        self.plantas.append(planta)

class Model:
    def __init__(self):
        super().__init__()
        self.edificio = self.crear_edificio()

    def crear_edificio(self):
        edificio = Edificio("Edificio Principal")

        planta1 = Planta("Planta 1")
        planta2 = Planta("Planta 2")
        planta3 = Planta("Planta 3")

        aulas_planta1 = [Aula(f"A1{i}", planta1) for i in range(1, 16)]
        aulas_planta2 = [Aula(f"A2{i}", planta2) for i in range(1, 16)]
        aulas_planta3 = [Aula(f"A3{i}", planta3) for i in range(1, 12)]

        for aula in aulas_planta1:
            planta1.agregar_aula(aula)

        for aula in aulas_planta2:
            planta2.agregar_aula(aula)

        for aula in aulas_planta3:
            planta3.agregar_aula(aula)

        edificio.agregar_planta(planta1)
        edificio.agregar_planta(planta2)
        edificio.agregar_planta(planta3)

        return edificio

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
            # Obtener las columnas que son aulas (columnas que empiezan con 'H')
            aulas_columns = [col for col in filtered_data.columns if col.startswith('H')]
            for col in aulas_columns:
                temperatures[col] = filtered_data.iloc[0][col]

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

