from abc import *
import copy

# PROTOTIPO

class Person(ABC):

    def __init__(self, nombre:str, edad:int, nacionalidad:str):

        # ATRIBUTOS BASE
        self.nombre = nombre
        self.edad = edad
        self. nacionalidad = nacionalidad

    # METODO DE CLONADO
    @abstractmethod
    def clone(self):
        pass

# PROTOTIPOS CONCRETOS

class Kid(Person):
    
    def __init__(self, nombre:str, edad:int, nacionalidad:str):

        self.nombre = nombre
        self.edad = edad
        self. nacionalidad = nacionalidad

        # ATRIBUTOS ESPECIFICOS DE LA SUBCLASE
        self.juguete = 'auto'

    def clone(self):
        return copy.deepcopy(self) # GENERA UNA COPIA DEL PROTOTIPO CONCRETO

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}'

class Adult(Person):
    
    def __init__(self, nombre:str, edad:int, nacionalidad:str):

        self.nombre = nombre
        self.edad = edad
        self. nacionalidad = nacionalidad

        self.auto = 'Volkswagen Up'

    def clone(self):
        return copy.deepcopy(self) 

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Nacionalidad: {self.nacionalidad}'

if __name__ == '__main__':

    print('[ Creando prototipos concretos Niño y Adulto ]\n')

    kid = Kid('Agustin', 5, 'Argentino')
    adult = Adult('Tomas', 21, 'Argentino')

    print('>> Niño: [ > ' + ', > '.join("%s: %s" % item for item in vars(kid).items()) + ' ]') 
    print('>> Adulto: [ > ' + ', > '.join("%s: %s" % item for item in vars(adult).items()) + ' ]') 

    print('\n[ Creando copia Niño ]\n')

    for n in range(5):
        kid_clone = kid.clone()
        print(f'Clon nro {n+1} de Niño creado')
    
    print(f"\n>> Estructura de los clones: {kid_clone}")

    print('\n[ Creando copia Adulto ]\n')

    for n in range(5):
        adult_clone = adult.clone()
        print(f'Clon nro {n+1} de Adulto creado')

    print(f"\n>> Estructura de los clones: {adult_clone}")