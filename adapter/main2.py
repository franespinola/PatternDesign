# Interfaz objetivo
class SistemaInterfaz:
    def guardar_archivo(self):
        pass

# Implementación existente - SistemaLocal
class SistemaLocal:
    def guardar_archivo_local(self):
        print("Archivo guardado localmente")

# Implementación existente - SistemaNube
class SistemaNube:
    def guardar_archivo_nube(self):
        print("Archivo guardado en la nube")

# Adaptador para SistemaLocal
class AdaptadorLocal(SistemaInterfaz):
    def __init__(self, sistema_local):
        self.sistema_local = sistema_local

    def guardar_archivo(self):
        self.sistema_local.guardar_archivo_local()

# Adaptador para SistemaNube
class AdaptadorNube(SistemaInterfaz):
    def __init__(self, sistema_nube):
        self.sistema_nube = sistema_nube

    def guardar_archivo(self):
        self.sistema_nube.guardar_archivo_nube()

# Cliente
def cliente(sistema):
    sistema.guardar_archivo()

# Uso del adaptador
sistema_local = SistemaLocal()
adaptador_local = AdaptadorLocal(sistema_local)

sistema_nube = SistemaNube()
adaptador_nube = AdaptadorNube(sistema_nube)

cliente(adaptador_local)  # Archivo guardado localmente
cliente(adaptador_nube)   # Archivo guardado en la nube

