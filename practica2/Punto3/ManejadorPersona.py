from Persona import Persona
import csv
import numpy as np


class ManejadorPersona:
    __cantidad = 0
    __dimension = 0
    __incremeto = 5

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__personas = np.empty(self.__dimension, dtype=Persona)

        archivo = open('./practica2/Punto3/Persona.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(self.__cantidad == self.__dimension):
                self.__dimension += self.__incremeto
                self.__personas.resize(self.__dimension)
            self.__personas[self.__cantidad] = Persona(
                fila[0], fila[1], fila[2]
            )
            self.__cantidad += 1