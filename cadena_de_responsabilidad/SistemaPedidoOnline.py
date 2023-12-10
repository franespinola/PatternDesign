from abc import ABC, abstractmethod

# Clase base para un manejador
class Handler(ABC):
    @abstractmethod
    def handle_request(self, order):
        pass

# Manejador para validar el inventario
class InventoryValidator(Handler):
    def handle_request(self, order):
        if order.quantity <= 0:
            print("Error: Cantidad no válida en el pedido.")
        elif order.quantity > 10:
            print("Error: La cantidad supera el límite de inventario.")
        else:
            print("Inventario validado correctamente.")
            if self.next_handler:
                self.next_handler.handle_request(order)

# Manejador para calcular el precio final
class PriceCalculator(Handler):
    def handle_request(self, order):
        order.calculate_total_price()
        print(f"Precio calculado: {order.total_price}")
        if self.next_handler:
            self.next_handler.handle_request(order)

# Manejador para generar la factura
class InvoiceGenerator(Handler):
    def handle_request(self, order):
        print(f"Factura generada para el pedido {order.order_id}. Monto: {order.total_price}")
        # Este manejador no pasa la solicitud al siguiente, ya que es el último en la cadena.

# Clase que representa un pedido
class Order:
    def __init__(self, order_id, quantity, product_name):
        self.order_id = order_id
        self.quantity = quantity
        self.product_name = product_name
        self.total_price = None

    def calculate_total_price(self):
        # En este ejemplo, simplemente multiplicamos la cantidad por un precio unitario fijo.
        # En una aplicación real, este cálculo podría ser más complejo.
        unit_price = 10  # Precio unitario ficticio
        self.total_price = self.quantity * unit_price

# Cliente que utiliza la cadena de responsabilidad
def process_order(order):
    # Configuramos la cadena de responsabilidad
    validator = InventoryValidator()
    calculator = PriceCalculator()
    invoice_generator = InvoiceGenerator()

    validator.next_handler = calculator
    calculator.next_handler = invoice_generator

    # Iniciamos el proceso con el primer manejador
    validator.handle_request(order)

# Uso del patrón Chain of Responsibility en un sistema de pedidos online
order = Order(order_id=1, quantity=5, product_name="Producto A")
process_order(order)
