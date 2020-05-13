# C.    Definir una clase ManejaHelados que registre y gestione a través de una
#       lista los helados vendidos.
import numpy as np

from Helado import Helado


class ManejaHelados:
    # Arreglo
    __dimension = 1
    __cantidad = 0
    __incremento = 1

    def __init__(self):
        self.__helados = np.empty(self.__dimension, dtype=Helado)

    def ventaHelado(self, helado):
        if (type(helado) is Helado):
            self.__helados[self.__cantidad] = helado
            self.__cantidad += 1
        else:
            print("Helado Invalido")
