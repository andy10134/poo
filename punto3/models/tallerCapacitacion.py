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

    def agregarInscripcion(self, inscripcion):
        if(type(inscripcion) is Inscripcion):
            if(self.__vacantes == 0):
                print("Inscripciones cerradas")
            else:
                self.__inscripciones[self.__cantidad] = inscripcion
                self.__cantidad += 1
                self.__vacantes -= 1
                print("Quedan ", str(
                    self.__vacantes
                ), " disponibles")

    def mostrarInscripciones(self):
        if(self.__cantidad != 0):
            for inscripcion in self.__inscripciones:
                if(type(inscripcion) is Inscripcion):
                    print(inscripcion)
        else:
            print("No hay inscriptos")

    def getMonto(self):
        return self.__montoInscripcion

    def getInscripciones(self):
        return self.__inscripciones
