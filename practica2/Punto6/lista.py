from zope.interface import implementer
from interface import IInterface
from nodo import Nodo
from auto import Auto
from autoNuevo import AutoNuevo
from autoUsado import AutoUsado

@implementer(IInterface)

class Lista:
    
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    __vehiculos = []

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

    def agregarElemento(self, elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo 
        self.__actual= nodo
        self.__tope += 1

    def insertarElemento(self, elemento, indice):
        if(indice >= 0 and indice < self.__tope):
            anterior = self.__comienzo
            sig = anterior.getSiguiente() 
            for i in range(indice - 1):
                anterior = anterior.getSiguiente()
                sig = anterior.getSiguiente()
            anterior.setSiguiente(elemento)
            elemento.setSiguiente(sig)
        else:
            if(indice == self.__tope):
                pass
            else:
                raise Exception('Indice invalido')

    #def mostrarElemento(self, posicion):
    #    aux = self.__comienzo
    #    while(aux !=  None and aux.getDato() == elemento):
    #        aux = aux.getsiguiente()
    #    if(aux == None):
            

    def mostrar(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            vehiculos = [vehiculo.toJSON() for vehiculo in self.__vehiculos]
        )
        return d
