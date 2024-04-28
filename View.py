class CalculatorView:
    def display_result(self, result):
        print("Resultado: ", result)

    def get_user_input(self):
        return float(input("Introduce un número: "))
