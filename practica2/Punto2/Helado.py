from Sabor import Sabor


import numpy as np


class Helado:
    __gramos = 0
    # Arreglo
    __cantidad = 0
    __dimension = 4

    def __init__(self, gramos):
        self.__gramos = gramos
        self.__sabores = np.empty(self.__dimension, dtype=Sabor)

    def getGramos(self):
        return self.__gramos

    def agregarSabor(self, sabor):
        if(type(sabor) is Sabor):
            if(self.__cantidad <= self.__dimension):
                self.__sabores[self.__cantidad] = sabor
                self.__cantidad += 1
            else:
                print("No se pueden tener mas sabores :c")
        else:
            print("Sabor Invalido")

    def setGramos(self, gramos):
        self.__gramos = gramos

    def getCantidadSabores(self):
        return self.__cantidad

    def getSabores(self):
        return self.__sabores

    def __str__(self):
        nombres = []
        for i in range(self.__cantidad):
            nombres.append(self.__sabores[i].getNombre())
        return str("Gramos: "  + str(self.getGramos()) + "\nCantidad de sabores: " + str(self.getCantidadSabores()) + "\nSabores: " + str(nombres))

