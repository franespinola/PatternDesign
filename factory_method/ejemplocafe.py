from abc import ABC, abstractmethod

# Interfaz Producto
class Cafe(ABC):
    @abstractmethod
    def preparar(self):
        pass

# Productos Concretos
class CafeExpressStarbucks(Cafe):
    def preparar(self):
        return "Café express de Starbucks"

class CafeLargoStarbucks(Cafe):
    def preparar(self):
        return "Café largo de Starbucks"

class CapsulaDolceGusto(Cafe):
    def preparar(self):
        return "Cápsula de café Dolce Gusto"

class CapsulaNespresso(Cafe):
    def preparar(self):
        return "Cápsula de café Nespresso"

# Clase Creador (Fábrica)
class FabricaCafe(ABC):
    @abstractmethod
    def preparar_cafe(self) -> Cafe:
        pass

# Creadores Concretos
class FabricaStarbucks(FabricaCafe):
    def preparar_cafe(self) -> Cafe:
        return CafeExpressStarbucks()

class FabricaDolceGusto(FabricaCafe):
    def preparar_cafe(self) -> Cafe:
        return CapsulaDolceGusto()

class FabricaNespresso(FabricaCafe):
    def preparar_cafe(self) -> Cafe:
        return CapsulaNespresso()

# Cliente
def cliente(fabrica: FabricaCafe):
    cafe = fabrica.preparar_cafe()
    print(f"Cliente: He recibido mi {cafe.preparar()}")

# Uso del patrón Factory Method
if __name__ == "__main__":
    fabrica_starbucks = FabricaStarbucks()
    fabrica_dolce_gusto = FabricaDolceGusto()
    fabrica_nespresso = FabricaNespresso()

    cliente(fabrica_starbucks)
    cliente(fabrica_dolce_gusto)
    cliente(fabrica_nespresso)
