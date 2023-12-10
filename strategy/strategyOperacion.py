from abc import ABC, abstractmethod

# Interfaz Estrategia
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Estrategias Concretas
class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b

class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b

# Clase Contexto
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

# Código cliente
class ExampleApplication:
    def main(self):
        # Crear objeto de contexto
        context = Context(None)

        # Leer primer número
        first_number = int(input("Enter the first number: "))

        # Leer segundo número
        second_number = int(input("Enter the second number: "))

        # Leer la acción deseada desde la entrada del usuario
        action = input("Enter the desired action (addition/subtraction/multiplication): ")

        # Configurar la estrategia en base a la acción
        if action == "addition":
            context.set_strategy(ConcreteStrategyAdd())
        elif action == "subtraction":
            context.set_strategy(ConcreteStrategySubtract())
        elif action == "multiplication":
            context.set_strategy(ConcreteStrategyMultiply())
        else:
            print("Invalid action. Exiting.")
            return

        # Ejecutar la estrategia seleccionada y obtener el resultado
        result = context.execute_strategy(first_number, second_number)

        # Imprimir el resultado
        print(f"Result: {result}")

# Instanciar y ejecutar la aplicación de ejemplo
app = ExampleApplication()
app.main()
