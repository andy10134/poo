from Persona import Persona
import numpy as np


class ManejadorPersona:
    __cantidad = 0
    __dimension = 0
    __incremeto = 0

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__sabores = np.empty(self.__dimension, dtype=Persona)