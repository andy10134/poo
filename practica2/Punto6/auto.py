class Auto():
    __modelo = None
    __cantidadPuertas = 0
    __color = None
    __precioBase = 0

    def __init__(self, modelo, puertas, color, precio):
        self.__modelo = modelo
        self.__cantidadPuertas = int(puertas)
        self.__color = color
        self.__precioBase = precio

    def getModelo(self):
        pass

    def getCantidadPuertas(self):
        pass

    def getColor(self):
        pass

    def getPrecioBase(self):
        pass
