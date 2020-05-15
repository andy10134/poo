# Cargar los datos de los sabores en una instancia de la clase ManejaSabores.
# Estos datos se encuentran en el archivo sabores.csv.
from Sabor import Sabor
import numpy as np
import csv
import operator


class ManejaSabores:
    # Arreglo
    __cantidad = 0
    __dimension = 5
    __incremento = 1

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__sabores = np.empty(self.__dimension, dtype=Sabor)
        self.__saboresPedidos = {}
        self.__gramosPedidos = {}
        i = 1

        archivo = open('./practica2/Punto2/sabores.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(self.__cantidad == self.__dimension):    # verifica la cantidad
                # de elementos y la dimension
                self.__dimension += self.__incremento   # en caso de que sea
                # igual se
                self.__sabores.resize(self.__dimension)  # aumenta el largo
                # del arreglo
            self.__sabores[self.__cantidad] = Sabor(fila[0], fila[1], i)
            self.__saboresPedidos[i] = 0
            self.__gramosPedidos[i] = 0
            self.__cantidad += 1
            i += 1
        archivo.close()

    def mostrarSabores(self):
        for i in range(self.__dimension):
            if(type(self.__sabores[i]) is Sabor):
                print("=================")
                print(self.__sabores[i])

    def setVenta(self, sabores, cantidad, tipo):
        for sabor in sabores:
            if(type(sabor) is Sabor):
                numeroSabor = sabor.getNumero()
                self.__saboresPedidos[numeroSabor] += 1
                self.__gramosPedidos[numeroSabor] += tipo/cantidad

    def topVentas(self):  # devuelve el top de sabores vendidos
        saboresPedidos_sort = sorted(self.__saboresPedidos.items(),
                                     key=operator.itemgetter(1), reverse=True)
        return saboresPedidos_sort[0:5]

    def gramosVendidos(self, numero):
        if(numero > 0 and numero <= self.__cantidad):
            return self.__gramosPedidos[numero]
        else:
            print("numero invalido")
            return None

    def cantidadVendida(self):
        return self.__saboresPedidos

    def getSabores(self):
        return self.__sabores

    def getCantidad(self):
        return self.__cantidad

    def getSabor(self, numero):
        if(numero > 0 and numero <= self.__cantidad and type(numero) is int):
            return self.__sabores[numero - 1]
        else:
            print("Sabor invalido")
            return None
