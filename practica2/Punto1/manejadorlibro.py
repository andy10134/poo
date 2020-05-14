import numpy as np
from libro import Libro
class ManejadorLibro:
    __cantidad= 0
    __dimension= 0
    __incremento= 3

    def __init__(self, cantidad= 5):
        self.__dimension= cantidad
        self.__arreglo= np.empty(self.__dimension, dtype= Libro)

    def agregarlibro(self, libro):
        if(self.__cantidad== self.__dimension):
            self.__dimension+= self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]= Libro(libro[0], libro[1], libro[2], libro[3], libro[4], libro[5])
        self.__cantidad+= 1
        

    def getArreglo(self):
        return self.__arreglo

    def getLibro(self, indice):
        return self.__arreglo[indice]

    def mostrarArreglo(self):
        print(self.__arreglo)
    
    def buscarLibro(self, id):
        i= 0
        bandera= True
        while(bandera and i != self.__cantidad):
            if(id == self.__arreglo[i].getId()):
                bandera=False
            else:
                i+=1
        if(bandera == False):
            print('Título: {}'.format(self.__arreglo[i].getTitulo()))
            print('Capitulos: ')
            self.__arreglo[i].listarCapitulos()
            print('Total Páginas: {}'.format(self.__arreglo[i].calcularTotalPaginas()))
        else:
            print('No se encontro libro con ese id, vuelva a intentarlo')
        
    def buscarPalabra(self, palabra):
        bandera= True
        for i in range(self.__cantidad):
            titulo= self.__arreglo[i].getTitulo()
            if(titulo.find(palabra)> -1):
                bandera= False
                print('Título: {}'.format(self.__arreglo[i].getTitulo()), '   Autor:{}'.format(self.__arreglo[i].getAutor()))
            else:
                bandera2= self.__arreglo[i].buscarEnCapitulo(palabra) 
        if(bandera and bandera2):
            print('no se encontro la palabra')
