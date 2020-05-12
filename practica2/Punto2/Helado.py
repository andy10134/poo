from Sabor import Sabor
import numpy as np

class Helado:
    cantidadSabores = 4
    __gramos = 0
    
    #Arreglo
    __cantidad= 0
    __dimension= 4

    def __init__(self, gramos):
        self.__gramos = gramos
        self.__sabores = np.empty(self.__dimension, dtype = Sabor)

    def getGramos(self):
        return self.__gramos
    
    def setGramos(self, gramos):
        self.__gramos = gramos