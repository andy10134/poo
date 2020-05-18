import numpy as np
import csv
from TalleresCapacitacion import TalleresCapacitacion


class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0
    __incremeto = 0

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__sabores = np.empty(self.__dimension, dtype=TalleresCapacitacion)