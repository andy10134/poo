class TallerCapacitacion:

    __idTaller = 0
    __nombre = ""
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = None

    def __init__(self, id, nombre, vacantes, montoInscripcion):
        self.__idTaller = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInscripcion
        self.__inscripciones = []
    
    def agregarInscripcion(self, inscripcion):
        self.__inscripciones.append(inscripcion)

    def getId(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacantes(self):
        return self.__vacantes

    def getMonto(self):
        return self.__montoInscripcion

    def getInscripciones(self):
        return self.__inscripciones

    def setVacantes(self, numero):
        self.__vacantes-= 1

    

