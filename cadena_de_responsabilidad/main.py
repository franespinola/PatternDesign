from abc import ABC, abstractstaticmethod

# -----------------Manejador Abstracto

class Cumpleanios(ABC): 
    @abstractstaticmethod
    def set_sucesor(sucesor):
        pass

    @abstractstaticmethod
    def set_cantidad(cantidad):
        pass 

# -----------------Manejadores Concretos

class Anios(Cumpleanios):
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor #Aca definimos el siguiente manejador de la cadena

    def set_cantidad(self, cantidad):
        if cantidad >= 365:
            num = cantidad // 365 #Nos devuelve el cociente 
            resto = cantidad % 365 #Nos devuelve el resto
            print(f"Faltan {num} anios para el cumpleaños")
            if resto != 0:  #Si el resto nos da diferente de cero pasaría al siguiente manejador de la cadena
                self._sucesor.set_cantidad(resto) #Le paso el resto al siguiente manejador como cantidad
        else:
            self._sucesor.set_cantidad(cantidad)

class Meses(Cumpleanios):
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor

    def set_cantidad(self, cantidad):
        if cantidad >= 30:
            num = cantidad // 30
            resto = cantidad % 30
            print(f"Faltan {num} meses para el cumpleaños")
            if resto != 0:
                self._sucesor.set_cantidad(resto)
        else:
            self._sucesor.set_cantidad(cantidad)


class Dias(Cumpleanios):
    def __init__(self):
        self._sucesor = None

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor

    def set_cantidad(self, cantidad):
        if cantidad >= 1:
            num = cantidad // 1
            resto = cantidad % 1
            print(f"Faltan {num} dias para el cumpleaños")
            if resto != 0:
                self._sucesor.set_cantidad(resto)
        else:
            self._sucesor.set_cantidad(cantidad)

#----------------Orden de la cadena

class Cuenta_cadena:
    def __init__(self):
        self.cadena1 = Anios()
        self.cadena2 = Meses()
        self.cadena3 = Dias()

        self.cadena1.set_sucesor(self.cadena2)
        self.cadena2.set_sucesor(self.cadena3)

if __name__ == "__main__":
    edad = Cuenta_cadena()
    cantidad = int(input("Ingresar la cantidad: "))
    if cantidad < 0:
        print("Ingrese correctamente")
        exit()
    edad.cadena1.set_cantidad(cantidad)