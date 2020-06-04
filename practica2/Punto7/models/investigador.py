from models.persona import Persona


class Investigador(Persona):
    
    __area = ""
    __tipo = 0

    def __init__(self, cuil, nombre, apellido, sueldo, antiguiedad, area, tipo):
        self.__area = area
        self.__tipo = tipo
        super().__init__(cuil, nombre, apellido, sueldo, antiguiedad)

    def getArea(self):
        return self.__area

    def getTipo(self):
        return self.__tipo

    def calcularSueldo(self):
        sueldo = super().getSueldo()
         Sueldo básico+% antigüedad