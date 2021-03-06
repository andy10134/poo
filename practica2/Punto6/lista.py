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
            self.insertarElemento(vehiculo, posicion)

    def mostrarElemento(self, posicion):
        self.__indice = 0
        anterior = self.__comienzo
        sig = anterior.getSiguiente()
        while(self.__indice != posicion and sig is not None):
            anterior = sig
            sig = anterior.getSiguiente()
            self.__indice += 1
        if(self.__indice == posicion):
            if(type(anterior.getDato()) is AutoUsado):
                print(
                    'El vehiculo que se encuentra en la',
                    ' posicion {} es del tipo Usado'.format(posicion+1))
            else:
                print(
                    'El vehiculo que se encuentra en la',
                    ' posicion {} es del tipo Nuevo'.format(posicion+1))
        else:
            raise Exception(
                'Posición no valida, ingrese un valor menor a {}'.format(
                    self.__tope
                )
            )

    def busquedaPatente(self, patente):
        aux = self.__comienzo
        elem = self.__comienzo.getDato()
        bandera = False
        while(aux is not None and not bandera):
            elem = aux.getDato()
            if(type(elem) is AutoUsado and elem.getPatente() == patente):
                bandera = True
            else:
                aux = aux.getSiguiente()
        if(bandera):
            return elem
        else:
            return None

    def vehiculoEconomico(self):
        aux = self.__comienzo
        elemento = self.__comienzo.getDato()
        min = 100000000000000000
        auxAuto = None
        while(aux is not None):
            if(elemento.calcularPrecio() < min):
                min = elemento.calcularPrecio()
                auxAuto = elemento
            aux = aux.getSiguiente()
            if(aux is not None):
                elemento = aux.getDato()
        print(auxAuto)
        print('Importe de venta: {}'.format(auxAuto.calcularPrecio()))

    def toJSON(self):
        vehiculos = []
        nodo = self.__comienzo
        while(nodo is not None):
            auto = nodo.getDato()
            vehiculos.append(auto.toJSON())
            nodo = nodo.getSiguiente()

        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=vehiculos
        )
        return d
