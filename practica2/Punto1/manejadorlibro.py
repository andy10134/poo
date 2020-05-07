import numpy as np
from libro import Libro
class ManejadorLibro:
    __cantidad= 0
    __dimension= 0
    __incremento= 3

    def __init__(self, cantidad= 10):
        self.__dimension= cantidad
        self.__arreglo= np.empty(self.__dimension, dtype= Libro)

    def agregarlibro(self, libro):
        if(self.__cantidad== self.__dimension):
            self.__dimension+= self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]= Libro(libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[6])
        self.__cantidad+= 1
