from zope.interface import Interface
from zope.interface import implementer

class Iinterface(Interface):

    def insertarElemento(self, elemento, indice):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self, elemento):
        pass