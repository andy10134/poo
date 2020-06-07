from zope.interface import implementer
from interface import IInterface
from nodo import Nodo
from models.docenteInvestigador import DocenteInvestigador
from models.personalAyuda import PersonalAyuda
from models.docente import Docente
from models.investigador import Investigador
from models.persona import Persona
from operator import attrgetter


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


    def mostrarElemento(self, posicion):
        self.__indice = 0
        anterior = self.__comienzo
        sig = anterior.getSiguiente()
        while(self.__indice != posicion and sig is not None):
            anterior = sig
            sig = anterior.getSiguiente()
            self.__indice += 1
        if(self.__indice == posicion):
            return anterior.getDato()
        else:
            raise Exception(
                'Posición no valida, ingrese un valor menor a {}'.format(
                    self.__tope
                )
            )

    def agregarAgente(self, datos, posicion=None):
        if(len(datos) == 6):
            agente = PersonalAyuda(
                datos[0], datos[1], datos[2], datos[3],
                datos[4], datos[5]
            )
        elif(len(datos) == 7):
            agente = Investigador(
                datos[0], datos[1], datos[2], datos[3],
                datos[4], datos[5], datos[6]
            )
        elif(len(datos) == 8):
            agente = Docente(
                datos[0], datos[1], datos[2], datos[3],
                datos[4], datos[5], datos[6], datos[7]
            )
        else:
            agente = DocenteInvestigador(
                datos[0], datos[1], datos[2], datos[3],
                datos[4], datos[5], datos[6], datos[7],
                datos[8], datos[9], datos[10], datos[11]
            )
        if(posicion is None):
            self.agregarElemento(agente)
        else:
            self.insertarElemento(agente, posicion)

    def listarDocentesInvestigadores(self, dato, filtro):
        p = self.__comienzo
        elemento = DocenteInvestigador
        filtro = 'get' + filtro
        func = getattr(DocenteInvestigador, filtro)
        docentesInnvestigadores = []
        while(p is not None):
            elemento = p.getDato()
            if(type(elemento) is DocenteInvestigador and func(elemento) == dato):
                docentesInnvestigadores.append(elemento)

            p = p.getSiguiente()

        docentesInnvestigadores.sort() # Se ordenan las dos listas por igual !!

        return docentesInnvestigadores

    def contarAgentes(self, area):
        aux = self.__comienzo
        contI = 0
        contDI = 0
        while(aux is not None):
            elemento = aux.getDato()
            if(type(elemento) is Investigador):
                if(elemento.getArea() == area):
                    contI += 1
            elif(type(elemento) is DocenteInvestigador):
                if(elemento.getArea() == area):
                    contDI += 1
            aux = aux.getSiguiente()
        print('Cantidad de Investigadores que trabajan en el area de {}: {}'.format(area, contI))
        print('Cantidad de Docentes Investigadores que trabajan en el area de {}: {}'.format(area, contDI))

    def generarListado(self):
        aux = self.__comienzo
        listado = []
        while(aux is not None):
            elemento = aux.getDato()
            listado.append(elemento)
            aux = aux.getSiguiente()
        listado.sort()
        #sorted(listado, key=lambda elemento: elemento.getApellido())
        return listado

    def toJSON(self):
        personal = []
        nodo = self.__comienzo
        while(nodo is not None):
            agente = nodo.getDato()
            personal.append(agente.toJSON())
            nodo = nodo.getSiguiente()

        d = dict(
            __class__=self.__class__.__name__,
            personal=personal
        )
        return d
