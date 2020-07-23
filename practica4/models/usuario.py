
class Usuario():
    __dni = 0
    __clave = ''
    __tipo = ''
    __pedidos = []

    def __init__(self, dni, clave, tipo):
        self.__dni = dni
        self.__clave = clave
        self.__tipo = tipo
    
    def agregarPedido(self, pedido):
        self.__pedidos.append(pedido)

    def getDni(self):
        return self.__dni
    
    def getClave(self):
        return self.__clave
    
    def getTipo(self):
        return self.__tipo