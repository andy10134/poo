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

    def agregarElemento(self, elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarElemento(self, elemento, indice):
        if(indice >= 0 and indice <= self.__tope):
            if(self.__comienzo is None or indice == 0):
                self.agregarElemento(elemento)
            else:
                nodo = Nodo(elemento)
                anterior = self.__comienzo
                sig = self.__comienzo
                i = 0
                while(i < indice and sig is not None):
                    anterior = sig
                    sig = sig.getSiguiente()
                    i += 1
                anterior.setSiguiente(nodo)
                nodo.setSiguiente(sig)
                self.__tope += 1
        else:
            raise Exception('Indice invalido')

    def agregarPosicion(self, datos, posicion=None):
        if(posicion is None):
            self.agregarElemento(datos)
        else:
            self.insertarElemento(datos, posicion)

    def mostrarElemento(self, posicion):
        self.__indice = 0
        anterior = self.__comienzo
        sig = anterior.getSiguiente()
        while(self.__indice != posicion and sig is not None):
            anterior = sig
            sig = anterior.getSiguiente()
            self.__indice += 1
        if(self.__indice == posicion):
            pass #comentario re loco
        else:
            raise Exception(
                'Posición no valida, ingrese un valor menor a {}'.format(
                    self.__tope
                )
            )

    def toJSON(self):
        personal = []
        nodo = self.__comienzo
        while(nodo is not None):
            auto = nodo.getDato()
            personal.append(auto.toJSON())
            nodo = nodo.getSiguiente()

        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=personal
        )
        return d
