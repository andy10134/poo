import csv

class Conjunto:
    def __init__(self, archivo):
        self.__lista = []
        reader   = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            self.__lista.append(fila[0])
        print(self.__lista)
        
    def get_lista(self):
        return self.__lista

    def __add__(self, otroConjunto):
        union= []
        union.extend(self.__lista)
        for entero in otroConjunto.__lista:
            try:
                i =self.__lista.index(entero)
            except:
                i = -1
            if(i == -1):
                union.append(entero)
        return Conjunto(union)

    def __sub__(self, otroConjunto):
        interseccion= []
        for entero in otroConjunto.__lista:
            try:
                i =self.__lista.index(entero)
            except:
                i = -1
            if(i != -1):
                interseccion.append(entero)
        return Conjunto(interseccion)
    
    def __eq__(self, otroConjunto):
        bandera=True
        if(len(self.__lista) == len(otroConjunto.__lista)):
            i =0
            while(bandera == True and len(otroConjunto.__lista) != i):
                try:
                    indice =self.__lista.index(otroConjunto.__lista[i])
                    bandera= True
                except:
                    bandera= False
                i += 1
            if(bandera == True):
                print("Los conjuntos son iguales :D")
            else:
                print("Los conjuntos son distintos D:")