
class Paciente():

    __nombre = ''
    __apellido = ''
    __telefono = 0
    __peso = 0
    __altura = 0

    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__telefono = self.requerido(telefono, 'Teléfono es un valor requerido')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido
    
    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def setTelefono(self, telefono):
        self.__telefono = telefono
    
    def setAlturo(self, altura):
        self.__altura = altura

    def setPeso(self, peso):
        self.__peso = peso

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                apellido = self.__apellido,
                nombre = self.__nombre,
                telefono = self.__telefono,
                altura = self.__altura,
                peso = self.__peso
            )
        )
        return d
