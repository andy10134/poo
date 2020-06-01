from zope.interface import implementer
from interface import IInterface
from nodo import Nodo

@implementer(IInterface)

class Lista:
    
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self.__indice == self.__tope):
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo 
        self.__actual= nodo
        self.__tope += 1

    def insertarElemento(self, elemento, indice):
        pass

    #def mostrarElemento(self, posicion):
    #    aux = self.__comienzo
    #    while(aux !=  None and aux.getDato() == elemento):
    #        aux = aux.getsiguiente()
    #    if(aux == None):
            

    #def mostrar(self):
    #    aux = self.__comienzo
    #    while(aux !=  None):
    #        print(aux.getDato())
    #        aux = aux.getsiguiente()