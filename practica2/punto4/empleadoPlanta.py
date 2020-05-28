from empleado import Empleado


class EmpleadoPlanta(Empleado):

    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, sueldo, antiguedad):
        self.__sueldoBasico = sueldo
        self.__antiguedad = antiguedad

    def getSueldo(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad
    
    def __str__(self):
        return ('Sueldo: {} \nAntiguedad: {}'.format(self.getSueldo(), self.getAntiguedad))