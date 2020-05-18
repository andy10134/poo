from Inscripcion import Inscripcion
import numpy as np

class ManejadorInscripciones:
    __cantidad= 0
    __dimension= 0
    __incremento= 5

    def __init__(self, cantidadInscripciones = 20):
        self.__dimension = cantidadInscripciones
        self.__inscripciones = np.empty(self.__dimension, dtype=Inscripcion)
    
    #def agregarInscripcion(self, persona, taller, ):
    #    if(self.__dimension == self.__cantidad):
    #        self.__dimension += self.__incremento
    #        self.__inscripciones.resize(self.__dimension)
    #    self.__inscripciones[self.__cantidad] = Inscripcion(inscripcion[0], inscripcion[1], inscripcion[2])
    #    self.__cantidad += 1