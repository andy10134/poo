from zope.interface import implementer
from interface import IInterface
from nodo import Nodo
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

    def agregarVehiculo(self, datos, posicion=None):
        if(len(datos) > 5):
            vehiculo = AutoUsado(
                datos[0], datos[1], datos[2], datos[3],
                datos[4], datos[5], datos[6], datos[7]
            )
        else:
            vehiculo = AutoNuevo(
                datos[0], datos[1], datos[2], datos[3], datos[4]
            )
        if(posicion is None):
            self.agregarElemento(vehiculo)
        else:
            print("pos {}".format(posicion))
            self.insertarElemento(vehiculo, posicion)

    def mostrarElemento(self, posicion):
        self.__indice = 0
        if(posicion <= self.__tope):
            while(self.__indice != posicion):
                self.__indice += 1
                print(self.__indice)
            print(type(self.__actual.getDato()))
        else:
            raise Exception(
                'Posición no valida, ingrese un valor menor a {}'.format(
                    self.__tope
                )
            )

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self.__vehiculos]
        )
        return d
