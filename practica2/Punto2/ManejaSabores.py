#Cargar los datos de los sabores en una instancia de la clase ManejaSabores.
#Estos datos se encuentran en el archivo sabores.csv.
from Sabor import Sabor
import numpy as np
import csv

class ManejaSabores:
    #Arreglo
    __cantidad= 0
    __dimension= 0
    __incremento= 1


    def __init__(self, cantidad = 5):
        self.__dimension= cantidad
        self.__sabores = np.empty(self.__dimension, dtype = Sabor)
        i=1

        archivo  = open('./practica2/Punto2/sabores.csv')
        reader   = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(self.__cantidad == self.__dimension):    #verifica la cantidad de elementos y la dimension
                self.__dimension+= self.__incremento    #en caso de que sea igual se 
                self.__sabores.resize(self.__dimension) # aumenta el largo del arreglo
            self.__sabores[self.__cantidad]= Sabor(fila[0],fila[1],i)
            self.__cantidad+= 1
            i+=1          
        archivo.close()
        
    def mostrarSabores(self):
        for i in range(self.__dimension):
            if(type(self.__sabores[i]) is Sabor):
                print("=================")
                print(self.__sabores[i])

    def getSabores(self):
        return self.__sabores
