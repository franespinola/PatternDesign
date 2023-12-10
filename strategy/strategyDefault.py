# Interfaz Estrategia
class Estrategia:
    def ejecutar_operacion(self):
        pass

# Estrategias Concretas
class EstrategiaA(Estrategia):
    def ejecutar_operacion(self):
        print("Ejecutando Operación según Estrategia A")

class EstrategiaB(Estrategia):
    def ejecutar_operacion(self):
        print("Ejecutando Operación según Estrategia B")

# Contexto
class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def ejecutar_operacion(self):
        self.estrategia.ejecutar_operacion()

# Uso del patrón
contexto_con_A = Contexto(EstrategiaA())
contexto_con_A.ejecutar_operacion()  # Salida: Ejecutando Operación según Estrategia A

contexto_con_B = Contexto(EstrategiaB())
contexto_con_B.ejecutar_operacion()  # Salida: Ejecutando Operación según Estrategia B

#Ejemplo:

#Supongamos que tienes una clase Contexto que realiza cierta operación y quieres que esta operación pueda variar de acuerdo a 
#diferentes estrategias. Entonces, tendrías una interfaz Estrategia y varias clases concretas que implementan esa interfaz.
#En este ejemplo, el Contexto tiene una referencia a una estrategia, y en tiempo de ejecución puedes cambiar la estrategia 
#asignada al contexto, permitiendo que la operación se realice de acuerdo a la estrategia específica seleccionada.
#El patrón Strategy es útil cuando tienes varios algoritmos o estrategias posibles y quieres que el cliente pueda elegir 
#entre ellos sin tener que modificar el código del cliente. Además, facilita la extensión, ya que puedes agregar nuevas 
#estrategias sin modificar el código existente.
