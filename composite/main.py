from abc import *

# INTERFAZ COMPONENTE

class Elemento(ABC):

    @abstractmethod
    def obtener_precio(self):
        pass

# ELEMENTO HOJA

class Producto(Elemento):

    def __init__(self, name:str, precio:int):

        self.name = name
        self.precio = precio

    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f'{self.name}'

# ELEMENTO COMPUESTO

class Caja(Elemento):

    def __init__(self, name:str, components:list):

        self.name = name
        self.components = components

    def obtener_precio(self):
        
        precio_total = 0

        for element in self.components:
            precio_total += element.obtener_precio()
        
        return precio_total

    def __str__(self):

        elements = []

        for element in self.components:
            elements.append(f'{element}')
        return f'{self.name}: {elements}'

if __name__ == '__main__':

    telefono = Producto('iPhone 14', 615000)
    computadora = Producto('HP I5 1TB', 320000)
    auriculares = Producto('Airpods', 120000)
    cargador = Producto('Cargador Apple', 8000)

    paquete = Caja('Apple box', [telefono, auriculares, cargador])
    paquete_grande = Caja('Caja Grande', [paquete, cargador])

    print(f'> Paquete contiene: {paquete_grande}')
    print(f'> Precio total del paquete: ${paquete_grande.obtener_precio()}')

    
