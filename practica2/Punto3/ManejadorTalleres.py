import numpy as np
import csv
from TallerCapacitacion import TallerCapacitacion


class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0
    __incremeto = 0

    def __init__(self, cantidad=5):
        self.__dimension = cantidad

        archivo = open('./practica2/Punto3/Talleres.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(len(fila) > 1):
                if(self.__cantidad == self.__dimension):
                    self.__talleres.resize(self.__dimension)
                self.__talleres[self.__cantidad] = TallerCapacitacion(
                    fila[0], fila[1], fila[2], fila[3]
                )
                print(fila)
                cantidad += 1
            else:
                self.__talleres = np.empty(
                    self.__dimension,
                    dtype=TallerCapacitacion
                )
