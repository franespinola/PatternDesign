from abc import ABCMeta, abstractmethod
import sys, time


#T* Constructor
#! Paso 1

class Objeto(metaclass=ABCMeta): 

    @property
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def envase(self):
        pass

    @abstractmethod
    def precio(self):
        pass
    
    
    

#! Paso 2 
#T* Constructor
class Envase(metaclass=ABCMeta): 
    @abstractmethod
    def paquete(self): 
        pass
    
class Envoltorio_papel(Envase): 
    def paquete(self):
        return "Envoltorio de papel"

class Botella(Envase):
    def paquete(self):
        return "Botella"




#! Paso 3

class Hamburguesa(Objeto):
    def envase(self):
        return Envoltorio_papel()

    def precio(self):
        pass

class Bebida(Objeto):
    def envase(self):
        return Botella()

    def precio(self):
        pass





#T* ConstructorConcreto
#! Paso 4

class Hamb_Carne(Hamburguesa):

    def precio(self):
        return 1590
        
    def nombre(self):
        return "Hamburguesa de carne"

#T* ConstructorConcreto
class Hamb_Pollo(Hamburguesa):
    
    def precio(self):
        return 1390

    def nombre(self):
        return "Hamburguesa de pollo"
    
    



#T* ConstructorConcreto
class Coca(Bebida):
    
    def precio(self):
        return 150

    def nombre(self):
        return "Coca"
    
#T* ConstructorConcreto
class Pepsi(Bebida):

    def precio(self):
        return 150

    def nombre(self):
        return "Pepsi"
    
    
    
    
    
    
#! Paso 5
class Combo:   
    
    def __init__(self):
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def precio_total(self):
        total = 0
        for objeto in self.objetos:
            total = total + objeto.precio()
        return total

    def ver_pedido(self):
        print(("\nObjeto").ljust(25)+ ("Envase").ljust(25)+ ("Precio").ljust(25))
        for objeto in self.objetos:
            print((objeto.nombre()).ljust(25),end='')
            print(((objeto.envase().paquete())).ljust(25),end='')
            print(("$"+ str(objeto.precio())).ljust(25),end='\n')   






#T* ConstructorConcreto
#! Paso 6

class Combo_Constructor:
    
    def preparar_combo_carne (self):
        print("\n\nPreparando Combo de Carne...")
        combo = Combo()
        combo.agregar_objeto(Hamb_Carne())
        combo.agregar_objeto(Coca())
        return combo

    def preparar_combo_pollo (self):
        print("\n\nPreparando combo de pollo...")
        combo = Combo()
        combo.agregar_objeto(Hamb_Pollo())
        combo.agregar_objeto(Pepsi())
        return combo


def animacion_carga(): 
    animation = "|/-\\"
    cont_animacion = 0
    cont_tiempo = 0        
    i = 0

    while (cont_tiempo != 20): 
        time.sleep(0.1)  
        sys.stdout.write("\r" + "Paciencia por favor.. " + animation[cont_animacion]) 
        sys.stdout.flush() 
        cont_animacion = (cont_animacion + 1)% 4
        i += 1
        cont_tiempo += 1
    
    sys.stdout.flush() 
    sys.stdout.write("\r")








if __name__ == "__main__":
    
    #T* Director 
    #! Paso 7
    
    combo_constructor1 = Combo_Constructor()
    pedido_carne = combo_constructor1.preparar_combo_carne()
    animacion_carga()
    pedido_carne.ver_pedido()
    print("Total:".ljust(50) + "$"+str(pedido_carne.precio_total()).ljust(25))
    print("\n")

    combo_constructor2 = Combo_Constructor()
    pedido_pollo = combo_constructor1.preparar_combo_pollo()
    animacion_carga()
    pedido_pollo.ver_pedido()
    print("Total:".ljust(50) + "$"+str(pedido_pollo.precio_total()).ljust(25))
    print("\n")