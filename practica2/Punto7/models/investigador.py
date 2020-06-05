from models.persona import Persona


class Investigador(Persona):

    __area = ""
    __tipo = 0

    def __init__(self, cuil, nombre, apellido, sueldo, antiguedad, area, tipo, carrera = '', cargo = '', catedra = ''):
        super().__init__(cuil, nombre, apellido, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__area = area
        self.__tipo = tipo

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def calcularSueldo(self):
        sueldoInvestigador = super().getSueldoBasico() + (
            super().getSueldoBasico() * super().getAntiguiedad())/100

        return sueldoInvestigador

    def __str__(self):
        return (
            '{}'
            'Area: {}'
            'Tipo: {}'.format(
                super().__str__(),
                self.getArea(),
                self.getTipo()
            )
        )
