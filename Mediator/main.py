from abc import ABC, abstractmethod

# Colleague (Usuario)
class Usuario(ABC):
    def __init__(self, mediator, user_id):
        self.mediator = mediator
        self.user_id = user_id

    @abstractmethod
    def enviar_mensaje(self, mensaje):
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje, sender_id):
        pass

# Mediator
class Mediator(ABC):
    @abstractmethod
    def registrar_usuario(self, usuario):
        pass

    @abstractmethod
    def enviar_mensaje(self, mensaje, sender_id, receiver_id):
        pass

# ConcreteMediator (ChatMediator)
class ChatMediator(Mediator):
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario

    def enviar_mensaje(self, mensaje, sender_id, receiver_id):
        if receiver_id in self.usuarios:
            self.usuarios[receiver_id].recibir_mensaje(mensaje, sender_id)
        else:
            print(f"El usuario con ID {receiver_id} no está registrado.")

# ConcreteColleague (UsuarioConcreto)
class UsuarioConcreto(Usuario):
    def enviar_mensaje(self, mensaje):
        print(f"Usuario {self.user_id} envía mensaje: {mensaje}")
        self.mediator.enviar_mensaje(mensaje, self.user_id, receiver_id=2)  # Enviar a otro usuario (ID 2)

    def recibir_mensaje(self, mensaje, sender_id):
        print(f"Usuario {self.user_id} recibe mensaje '{mensaje}' de Usuario {sender_id}")

# Uso del Mediator
if __name__ == "__main__":
    # Crear el mediador
    chat_mediator = ChatMediator()

    # Crear usuarios y registrarlos en el mediador
    usuario1 = UsuarioConcreto(chat_mediator, user_id=1)
    usuario2 = UsuarioConcreto(chat_mediator, user_id=2)
    chat_mediator.registrar_usuario(usuario1)
    chat_mediator.registrar_usuario(usuario2)

    # Usuarios envían mensajes a través del mediador
    usuario1.enviar_mensaje("Hola, ¿cómo estás?")
    usuario2.enviar_mensaje("¡Hola! Estoy bien, gracias.")

    # Resultado esperado:
    # Usuario 1 envía mensaje: Hola, ¿cómo estás?
    # Usuario 2 recibe mensaje 'Hola, ¿cómo estás?' de Usuario 1
    # Usuario 2 envía mensaje: ¡Hola! Estoy bien, gracias.
    # Usuario 1 recibe mensaje '¡Hola! Estoy bien, gracias.' de Usuario 2
