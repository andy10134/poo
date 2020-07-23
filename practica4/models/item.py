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

    def getNumero():
        return self.__numItem
    
    def get