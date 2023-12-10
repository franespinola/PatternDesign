# Interfaz EstrategiaRuta
class EstrategiaRuta:
    def generar_ruta(self, origen, destino):
        pass

# Estrategias Concretas
class RutaEnCoche(EstrategiaRuta):
    def generar_ruta(self, origen, destino):
        print(f"Generando ruta en coche desde {origen} hasta {destino}")

class RutaAPie(EstrategiaRuta):
    def generar_ruta(self, origen, destino):
        print(f"Generando ruta a pie desde {origen} hasta {destino}")

class RutaTransportePublico(EstrategiaRuta):
    def generar_ruta(self, origen, destino):
        print(f"Generando ruta en transporte público desde {origen} hasta {destino}")

# Contexto
class Navegador:
    def __init__(self, estrategia_ruta):
        self.estrategia_ruta = estrategia_ruta

    def planificar_ruta(self, origen, destino):
        self.estrategia_ruta.generar_ruta(origen, destino)

# Uso del patrón
navegador_coche = Navegador(RutaEnCoche())
navegador_coche.planificar_ruta("Inicio", "Destino")  # Salida: Generando ruta en coche desde Inicio hasta Destino

navegador_pie = Navegador(RutaAPie())
navegador_pie.planificar_ruta("Inicio", "Destino")  # Salida: Generando ruta a pie desde Inicio hasta Destino

navegador_transporte_publico = Navegador(RutaTransportePublico())
navegador_transporte_publico.planificar_ruta("Inicio", "Destino")  # Salida: Generando ruta en transporte público desde Inicio hasta Destino
