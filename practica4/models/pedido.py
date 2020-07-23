
class Pedido():
    __numPedido = 0
    __fecha = None
    __total = 0
    __cobrado = None
    __observacion = ''
    __mesa = 0
    __items = []

    def __init__(self, numero, fecha, total, cobrado, observacion, mesa):
        self.__numPedido = numero
        self.__fecha = fecha
        self.__total = total
        self.__cobrado = cobrado
        self.__observacion = observacion
        self.__mesa = mesa

    def agregarItem(self, item):
        self.__items.append(item)

    def getNumero(self):
        return self.__numPedido
    
    def getFecha(self):
        return self.__fecha
    
    def getTotal(self):
        return self.__total
    
    def getCobrado(self):
        return self.__cobrado
    
    def getObservacion(self):
        return self.__observacion
    
    def getMesa(self):
        return self.__mesa
    
    def getItems(self):
        return self.__items

    def setCobrado(self, cobrado):
        self.__cobrado = cobrado