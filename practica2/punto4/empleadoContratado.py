
class Contratado():

    __cantHoras = 0
    __valorHora = 50

    def __init__(self, cantidad):
        self.__cantHoras = cantidad

    def getCantidad(self):
        return self.__cantHoras

    def getValor(self):
        return self.__valorHora

    def __str__(self):
        return ('Cantidad de horas trabajadas: {}'.format(self.getCantidad()))
