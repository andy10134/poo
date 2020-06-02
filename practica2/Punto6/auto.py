import abc

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
        return self.__modelo

    def getCantidadPuertas(self):
        return self.__cantidadPuertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__precioBase

    @abc.abstractclassmethod
    def calcularPrecio(self):
        pass

    @abc.abstractclassmethod
    def toJSON(self):
        pass

    def __str__(self):
        return((
            'Modelo: {} \nCantidad de puertas: {} \nColor: {} \nPrecio Base: {}'.format(self.getModelo(), self.getCantidadPuertas(), self.getColor(), self.getPrecioBase())
        ))