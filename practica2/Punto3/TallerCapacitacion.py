from Inscripcion import Inscripcion
import numpy as np


class TallerCapacitacion:

    __idTaller = 0
    __nombre = ""
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = None

    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, idTaller, nombre, vacantes, montoInscripcion):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = montoInscripcion
        self.__dimension = self.__vacantes
        self.__inscripciones = np.empty(
            self.__dimension, dtype=Inscripcion
        )

    def getId(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacantes(self):
        return self.__vacantes

    def getMontoInstcripcion(self):
        return self.__montoInstcripcion

    def agregarInscripcion(self, inscripcion):
        if(type(inscripcion) is Inscripcion):
            if(self.__cantidad == self.__vacantes):
                print("Inscripciones cerradas")
            self.__inscripciones[self.__cantidad] = inscripcion

    def mostrarInscripciones(self):
        for inscripcion in self.__inscripciones:
            if(type(inscripcion) is Inscripcion):
                print(inscripcion)
