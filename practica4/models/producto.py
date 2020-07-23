
class Producto():
    __numProducto = 0
    __nombre = ''
    __preciounitario = 0

    def __init__(self, numero, nombre, precio):
        self.__numProducto = numero
        self.__nombre = nombre
        self.__preciounitario = precio

    def getNumero(self):
        return self.__numProducto
    
    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__preciounitario
    