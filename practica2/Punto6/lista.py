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
        pass

    def mostrarElemento(self, posicion):
        if(posicion <= self.__tope):
            print(self.__vehiculos[posicion])
        else:
            raise Exception('Posición no valida, ingrese un valor menor a {}'.format(self.__tope))       

    def mostrar(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            vehiculos = [vehiculo.toJSON() for vehiculo in self.__vehiculos]
        )
        return d
