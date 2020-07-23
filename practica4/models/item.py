from models.producto import producto

class Item():

    __numItem = 0
    __precio = 0
    __estado = ''
    __producto = None

    def __init__(self, numero, precio, estado, producto):
        self.__numItem = numero
        self.__precio = precio
        self.__estado = estado
        self.__producto = producto

    def getNumero(self):
        return self.__numItem
    
    def getPrecio(self):
        return self.__precio
    
    def getEstado(self):
        return self.__estado
    
    def getProducto(self):
        return self.__producto
    
    def setEstado(self, estado):
        self.__estado = estado