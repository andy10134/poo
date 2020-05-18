class Inscripcion:

    __fechaInscripcion = None
    __pago = False
    __persona = None
    __taller = None

    def __init__(self, pago, persona, taller):
        self.__persona = persona
        self.__taller = taller
        self.__pago = pago
    
    def getFechaInscripcion(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago
    
    def getPersona(self):
        return self.__persona

    def getTaller(self):
        return self.__taller
        