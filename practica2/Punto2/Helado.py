from Sabor import Sabor
import numpy as np

class Helado:
    __gramos = 0
    
    #Arreglo
    __cantidad= 0
    __dimension= 4

    def __init__(self, gramos):
        self.__gramos = gramos
        self.__sabores = np.empty(self.__dimension, dtype = Sabor)

    def getGramos(self):
        return self.__gramos
    
    def agregarSabor(self,sabor):
        if(type(sabor) is Sabor):
            if(self.__cantidad <= self.__dimension):
                self.__sabores[self.__cantidad] = sabor
            else:
                print("No se pueden tener mas sabores :c")
        else:
            print("Sabor Invalido")

    def setGramos(self, gramos):
        self.__gramos = gramos