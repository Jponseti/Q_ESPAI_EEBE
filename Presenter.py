from Q_ESPAI_EEBE.Model import CalculatorModel


class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            num = self.view.get_user_input()
            operation = input("Operación (+ o -): ")
            if operation == '+':
                self.model.add(num)
            elif operation == '-':
                self.model.subtract(num)
            else:
                print("Operación no válida")
                continue
            result = self.model.get_result()
            self.view.display_result(result)

if __name__ == "__main__":
    Model = CalculatorModel()
    View = CalculatorView()
    Presenter = CalculatorPresenter(model, view)
    presenter.run()
