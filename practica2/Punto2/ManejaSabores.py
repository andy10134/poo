# Cargar los datos de los sabores en una instancia de la clase ManejaSabores.
# Estos datos se encuentran en el archivo sabores.csv.
from Sabor import Sabor
import numpy as np
import csv


class ManejaSabores:
    # Arreglo
    __cantidad = 0
    __dimension = 5
    __columnas = 3
    __incremento = 1

    def __init__(self, cantidad=5):
        self.__dimension = cantidad
        self.__sabores = np.empty(self.__dimension, dtype=Sabor)
        self.__saboresPedidos = np.empty((self.__dimension, self.__columnas))
        i = 1

        archivo = open('./practica2/Punto2/sabores.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(self.__cantidad == self.__dimension):    # verifica la cantidad de elementos y la dimension
                self.__dimension += self.__incremento    # en caso de que sea igual se 
                self.__sabores.resize(self.__dimension)  # aumenta el largo del arreglo
                self.__saboresPedidos.resize(self.__dimension, self.__columnas)
            self.__sabores[self.__cantidad] = Sabor(fila[0], fila[1], i)
            self.__saboresPedidos[self.__cantidad][0] = 0
            self.__saboresPedidos[self.__cantidad][1] = 0
            self.__saboresPedidos[self.__cantidad][2] = i # es el numero del sabor para invocarlo en el punto 3 y 4
            self.__cantidad += 1
            i += 1
        archivo.close()

    def mostrarSabores(self):
        for i in range(self.__dimension):
            if(type(self.__sabores[i]) is Sabor):
                print("=================")
                print(self.__sabores[i])

    def setVenta(self, sabores, cantidad, tipo):
        for i in range(cantidad):
            self.__saboresPedidos[sabores[i].getNumero()][0] += 1
            self.__saboresPedidos[sabores[i].getNumero()][1] += tipo/cantidad
        np.sort(self.__saboresPedidos, axis=0)

    def topVentas(self): # devuelve el top de sabores vendidos
        lista = []
        for i in len(5):
            aux = self.__saboresPedidos[i][0]
            saborAux = self.getSabor(self.__saboresPedidos[i][2]) # se invoca con parametro del numero del sabor
            lista.append(str(saborAux.getNombre(), " con ", aux, " descripcion ", saborAux.getDescripcion))
        return lista

    def gramosVendidos(self, numero):
        i = 0
        while(self.__saboresPedidos[i][2] != numero):
            i += 1
        return self.__saboresPedidos[i][1]

    def cantidadVendida(self):
        return self.__saboresPedidos

    def getSabores(self):
        return self.__sabores

    def getSabor(self, numero):
        if(numero > 0 and numero <= self.__cantidad and type(numero) is int):
            return self.__sabores[numero - 1]
        else:
            print("Sabor invalido")
            return None
