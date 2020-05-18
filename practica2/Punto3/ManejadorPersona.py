from Persona import Persona
import csv
import numpy as np


class ManejadorPersona:
    __cantidad = 0
    __dimension = 1
    __incremeto = 0

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__personas = np.empty(self.__dimension, dtype=Persona)

        archivo = open('./practica2/Punto3/Persona.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(self.__cantidad == self.__dimension):
                self.__dimension += self.__incremeto
                self.__talleres.resize(self.__dimension)
            self.__talleres[self.__cantidad] = Persona(
                fila[0], fila[1], fila[2]
            )
            self.__cantidad += 1
