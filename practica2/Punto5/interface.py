import zope.interface

class IInterface(zope.interface.interface.InterfaceClass):

    def insertarElemento(self, elemento, indice):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self, elemento):
        pass
