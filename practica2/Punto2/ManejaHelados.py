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
            if(self.__cantidad == self.__dimension):
                self.__dimension += self.__incremento
                self.__helados.resize(self.__dimension)
            self.__helados[self.__cantidad] = helado
            self.__cantidad += 1
        else:
            print("Helado Invalido")

    def getHelado(self):
        return self.__helados[self.__cantidad - 1]

    def getCantidad(self):
        return self.__cantidad

    def CantidadVecesPedido(self):
        pass

    def mostrarHelados(self):
        for i in range(self.__dimension):
            if(type(self.__helados[i]) is Helado):
                print("=================")
                print(self.__helados[i])

    def buscarTipoHelado(self, tipo):
        listaSabores = []
        for i in range(self.__dimension):
            if(type(self.__helados[i]) is Helado):
                if(self.__helados[i].getGramos == tipo):
                    sabores = self.__helados[i].getSabores()
                    for j in range(self.__helados[i].getCantidadSabores()):
                        if(listaSabores.index(sabores[j]) == -1):
                            print(sabores[j])
                            listaSabores.append(sabores[j])
        print('SABORES VENDIDOS: ')
        for sabor in listaSabores:
            print('-' + sabor)
