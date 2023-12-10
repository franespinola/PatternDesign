from abc import ABC, abstractmethod

# Interfaz abstracta para la creación de productos relacionados con la interfaz de usuario
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

# Interfaz abstracta para el producto "Botón"
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Interfaz abstracta para el producto "Cuadro de texto"
class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

# Implementación concreta de UIFactory para la plataforma Windows
class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_textbox(self):
        return WindowsTextBox()

# Implementación concreta de UIFactory para la plataforma macOS
class MacOSUIFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_textbox(self):
        return MacOSTextBox()

# Implementación concreta de Button para la plataforma Windows
class WindowsButton(Button):
    def render(self):
        return "Windows-style Button"

# Implementación concreta de TextBox para la plataforma Windows
class WindowsTextBox(TextBox):
    def render(self):
        return "Windows-style TextBox"

# Implementación concreta de Button para la plataforma macOS
class MacOSButton(Button):
    def render(self):
        return "MacOS-style Button"

# Implementación concreta de TextBox para la plataforma macOS
class MacOSTextBox(TextBox):
    def render(self):
        return "MacOS-style TextBox"

# Cliente que utiliza la fábrica abstracta para crear productos
def create_ui(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    print(f"Rendering {button.render()} and {textbox.render()}")

# Uso del patrón Abstract Factory
windows_factory = WindowsUIFactory()
create_ui(windows_factory)

print("\n")

macos_factory = MacOSUIFactory()
create_ui(macos_factory)
