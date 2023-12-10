from abc import *

# FABRICA ABSTRACTA

class ComputerFactory(ABC):

    @abstractmethod
    def createComputer(self):
        pass

# FABRICAS CONCRETAS

class PCFactory(ComputerFactory):

    def createComputer(self, ram:str, hdd:str, cpu:str):
        return PC(ram, hdd, cpu)

class ServerFactory(ComputerFactory):

    def createComputer(self, ram:str, hdd:str, cpu:str):
        return Server(ram, hdd, cpu)

# PRODUCTO ABSTRACTO

class Computer(ABC):

    @abstractmethod
    def getRAM(self):
        pass

    @abstractmethod
    def getHDD(self):
        pass

    @abstractmethod
    def getCPU(self):
        pass

    def __str__(self):

        return f'Specs: > RAM: '+ self.getRAM() + ', > HDD: ' + self.getHDD() + ', > CPU: ' + self.getCPU()

# PRODUCTOS CONCRETOS

class PC(Computer):

    def __init__(self, ram:str, hdd:str, cpu:str):

        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def getRAM(self):
        return self.ram

    def getHDD(self):
        return self.hdd

    def getCPU(self):
        return self.cpu

class Server(Computer):

    def __init__(self, ram:str, hdd:str, cpu:str):

        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def getRAM(self):
        return self.ram

    def getHDD(self):
        return self.hdd

    def getCPU(self):
        return self.cpu

if __name__ == '__main__':

    pcFactory = PCFactory()
    serverFactory = ServerFactory()

    pc = pcFactory.createComputer("2 GB", "500 GB", "2.4 GHz")
    server = serverFactory.createComputer("16 GB", "1 TB", "2.9 GHz")

    print(f'> PC: {pc}')
    print(f'> Server: {server}')