class DatabaseConnection:
    # 1. Añade un campo estático privado para almacenar la instancia Singleton.
    _instance = None

    # 4. Declara el constructor de clase como privado.
    def __init__(self, database_url):
        self.database_url = database_url
        # Lógica de inicialización de la conexión a la base de datos

    # 2. Declara un método de creación estático público para obtener la instancia Singleton.
    @classmethod
    def get_instance(cls, database_url):
        # 3. Implementa una inicialización diferida dentro del método estático.
        # Devuelve siempre esa instancia en todas las llamadas siguientes.
        if cls._instance is None:
            cls._instance = cls(database_url)
        return cls._instance


# Ejemplo de uso del Singleton en el contexto de una conexión a la base de datos
if __name__ == "__main__":
    # Intentar crear una instancia directamente generará un error
    # connection = DatabaseConnection("url_de_prueba")  # Esto lanzará una excepción

    # Utiliza el método estático para obtener la instancia Singleton
    db_connection1 = DatabaseConnection.get_instance("url_de_prueba")
    db_connection2 = DatabaseConnection.get_instance("otra_url_de_prueba")

    # Ambas instancias deberían ser iguales
    print(db_connection1 == db_connection2)  # Debería imprimir True
