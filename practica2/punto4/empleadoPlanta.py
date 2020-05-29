from practica2.punto4.empleado import Empleado


class EmpleadoPlanta(Empleado):

    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, dni, nombre, direccion, telefono, sueldo, antiguedad):
        self.__sueldoBasico = sueldo
        self.__antiguedad = antiguedad
        super().__init__(dni, nombre, direccion, telefono)

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def calcularSueldo(self):
        sueldo = 0
        sueldo = self.__sueldoBasico + (
            self.__sueldoBasico/100
        ) * self.__antiguedad
        return sueldo

    def getAntiguedad(self):
        return self.__antiguedad

    def __str__(self):
        return (
            super().__str__,
            'Sueldo: {} \nAntiguedad: {}'.format(
                self.getSueldo(), self.getAntiguedad
            )
        )
