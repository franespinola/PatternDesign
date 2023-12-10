from abc import ABC, abstractmethod

# Interfaz Estrategia
class Estrategia(ABC):
    @abstractmethod
    def ejecutar_algoritmo(self, datos):
        pass

# Estrategias Concretas
class AlgoritmoA(Estrategia):
    def ejecutar_algoritmo(self, datos):
        print(f"Ejecutando Algoritmo A con datos: {datos}")

class AlgoritmoB(Estrategia):
    def ejecutar_algoritmo(self, datos):
        print(f"Ejecutando Algoritmo B con datos: {datos}")

# Clase Contexto
class Contexto:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    def realizar_trabajo(self, datos):
        self._estrategia.ejecutar_algoritmo(datos)
        # Puedes realizar otras operaciones en el contexto si es necesario

# Uso del patrón
contexto = Contexto(AlgoritmoA())
contexto.realizar_trabajo("Datos para Algoritmo A")  # Salida: Ejecutando Algoritmo A con datos: Datos para Algoritmo A

contexto.set_estrategia(AlgoritmoB())
contexto.realizar_trabajo("Datos para Algoritmo B")  # Salida: Ejecutando Algoritmo B con datos: Datos para Algoritmo B
