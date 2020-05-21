from datetime import datetime


class Inscripcion:

    __fechaInscripcion = None
    __pago = False
    __persona = None
    __taller = None

    def __init__(self, persona, taller):
        self.__persona = persona
        self.__taller = taller
        self.__pago = False
        self.__fechaInscripcion = datetime.today()

    def __str__(self):
        return (('Persona: {} \nPago : {} \nFecha: {}').format(
            self.__persona.getNombre(), self.getPago(),
            self.getFechaInscripcion()
            ))

    def getFechaInscripcion(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago

    def getPersona(self):
        return self.__persona

    def getDni(self):
        return self.__persona.getDni()

    def getTaller(self):
        return self.__taller
