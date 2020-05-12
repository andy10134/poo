#B.    Definir una clase ManejaSabores que permita manejar los n sabores
#  que la heladería presenta a la venta.

class Sabor:
    __nombre = ""
    __descripcion = ""
    __numeroSabor = 1

    def __init__(self, nombre, descripcion, numero):
        self.__numeroSabor = numero
        self.__nombre = nombre
        self.__descripcion = descripcion
    
    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def getNumero(self):
        return self.__numeroSabor

    def __str__(self):
        return str("Nombre: "  + self.getNombre() + "\nDescripcion: " + self.getDescripcion() + "\nNumero: " + str(self.getNumero()))
