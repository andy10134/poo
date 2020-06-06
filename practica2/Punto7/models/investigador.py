from models.persona import Persona


class Investigador(Persona):

    __area = ""
    __tipo = 0

    def __init__(self, cuil, nombre, apellido, sueldo, antiguedad, area, tipo, carrera = '', cargo = '', catedra = ''):
        super().__init__(cuil, nombre, apellido, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__area = area
        self.__tipo = tipo

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def calcularSueldo(self):
        sueldoInvestigador = super().getSueldoBasico() + (
            super().getSueldoBasico() * super().getAntiguedad())/100
        return sueldoInvestigador

    def __str__(self):
        return (
            '{}\n'
            'Area: {}\n'
            'Tipo: {}'.format(
                super().__str__(),
                self.getArea(),
                self.getTipo()
            )
        )

    def __lt__(self, persona): 
        if(self.getApellido() < persona.getApellido() ):
            return True
        else: 
            return False
    
    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            atributos = dict(
                cuil = super().getCuil(),
                nombre = super().getNombre(),
                apellido = super().getApellido(),
                sueldo = super().getSueldoBasico(),
                antiguedad = super().getAntiguedad(),
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return d