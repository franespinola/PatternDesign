# Paso 1: Interfaz constructora Builder
class Builder:
    def construir_paredes(self):
        pass
    
    def construir_puertas(self):
        pass
    
    def construir_ventanas(self):
        pass
    
    def obtener_casa(self):
        pass

# Paso 2: Constructores concretos
class ConstructorCasasMadera(Builder):
    def __init__(self):
        self.casa = Casa("Madera")
    
    def construir_paredes(self):
        self.casa.agregar_parte("Paredes de madera")
    
    def construir_puertas(self):
        self.casa.agregar_parte("Puertas de madera")
    
    def construir_ventanas(self):
        self.casa.agregar_parte("Ventanas de vidrio")

    def obtener_casa(self):
        return self.casa

class ConstructorCasasPiedra(Builder):
    def __init__(self):
        self.casa = Casa("Piedra")
    
    def construir_paredes(self):
        self.casa.agregar_parte("Paredes de piedra")
    
    def construir_puertas(self):
        self.casa.agregar_parte("Puertas de hierro")
    
    def construir_ventanas(self):
        self.casa.agregar_parte("Ventanas pequeñas")

    def obtener_casa(self):
        return self.casa

# Paso 3: Productos
class Casa:
    def __init__(self, material):
        self.material = material
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def __str__(self):
        return f"Casa de {self.material}: {', '.join(self.partes)}"

# Paso 4: Clase directora
class Director:
    def construir_casa(self, constructor):
        constructor.construir_paredes()
        constructor.construir_puertas()
        constructor.construir_ventanas()

# Paso 5: Cliente
if __name__ == "__main__":
    constructor_madera = ConstructorCasasMadera()
    constructor_piedra = ConstructorCasasPiedra()

    director = Director()

    # Construir casa de madera
    director.construir_casa(constructor_madera)
    casa_madera = constructor_madera.obtener_casa()
    print(casa_madera)

    # Construir casa de piedra
    director.construir_casa(constructor_piedra)
    casa_piedra = constructor_piedra.obtener_casa()
    print(casa_piedra)
