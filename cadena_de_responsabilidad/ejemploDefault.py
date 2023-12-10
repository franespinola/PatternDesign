from abc import ABC, abstractmethod

# Declara la interfaz manejadora
class Manejador(ABC):
    @abstractmethod
    def manejar_solicitud(self, solicitud):
        pass

# Implementa la clase manejadora abstracta base
class ManejadorBase(Manejador):
    def __init__(self, siguiente=None):
        self._siguiente = siguiente

    def manejar_solicitud(self, solicitud):
        if self._siguiente:
            self._siguiente.manejar_solicitud(solicitud)

# Crea subclases manejadoras concretas
class ManejadorConcretoA(ManejadorBase):
    def manejar_solicitud(self, solicitud):
        if solicitud == "A":
            print("ManejadorConcretoA maneja la solicitud A.")
        else:
            super().manejar_solicitud(solicitud)

class ManejadorConcretoB(ManejadorBase):
    def manejar_solicitud(self, solicitud):
        if solicitud == "B":
            print("ManejadorConcretoB maneja la solicitud B.")
        else:
            super().manejar_solicitud(solicitud)

class ManejadorConcretoC(ManejadorBase):
    def manejar_solicitud(self, solicitud):
        if solicitud == "C":
            print("ManejadorConcretoC maneja la solicitud C.")
        else:
            super().manejar_solicitud(solicitud)

# Cliente
if __name__ == "__main__":
    # Ensambla la cadena
    manejador_a = ManejadorConcretoA()
    manejador_b = ManejadorConcretoB()
    manejador_c = ManejadorConcretoC()

    manejador_a.siguiente = manejador_b
    manejador_b.siguiente = manejador_c

    # Activa cualquier manejador de la cadena
    manejador_a.manejar_solicitud("A")
    manejador_a.manejar_solicitud("B")
    manejador_a.manejar_solicitud("C")
    manejador_a.manejar_solicitud("D")
