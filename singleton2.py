class Singleton:
    __instance = None

    def __init__(self):

        if Singleton.__instance is not None:
            raise Exception("Solo puede haber una instancia de Singleton")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

if __name__ == "__main__":

    s1 = Singleton.getInstance()

    s2 = Singleton.getInstance()

    print("\nDireccion de memoria de s1: ", s1)       # direccion de memoria

    print("\nDireccion de memoria de s2: ", s2)       # las variables s1 y s2 tienen la misma direccion de memoria 

    if id(s1) == id(s2):
        print("\nSingleton funciona, ambas variables contienen la misma instancia.\n") # ambas instancias tienen el mismo Object ID. Pertenecen al mismo objeto.
    else:
        print("\nSingleton no funciona, las variables contienen diferentes instancias.\n")

    # s3 = Singleton()      #! Para que salte la excepcion: "Solo puede haber una instancia de Singleton"