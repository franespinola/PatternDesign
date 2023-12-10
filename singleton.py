class SingletonMeta(type):
 
    _instances = {}

    def __call__(cls):    # El método __call__ permite escribir clases donde las instancias se comportan como funciones y se pueden llamar como una función.
     
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance

        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):  # una metaclase es una clase cuyas instancias son clases. En otras palabras, como los objetos son instancias de una clase, las clases son instancias de una metaclase.

    pass

if __name__ == "__main__":

    s1 = Singleton()

    s2 = Singleton()

    print("\nDireccion de memoria de s1: ", s1)       # direccion de memoria

    print("\nDireccion de memoria de s2: ", s2)       # las variables s1 y s2 tienen la misma direccion de memoria 

    if id(s1) == id(s2):
        print("\nSingleton funciona, ambas variables contienen la misma instancia.\n") # ambas instancias tienen el mismo Object ID. Pertenecen al mismo objeto.
    else:
        print("\nSingleton no funciona, las variables contienen diferentes instancias.\n")