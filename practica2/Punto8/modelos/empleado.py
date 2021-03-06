import abc


class Empleado():

    __dni = 0
    __nombre = None
    __direccion = None
    __telefono = 0

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    @abc.abstractclassmethod
    def calcularSueldo(self):
        pass

    def mostrar(self):
        print("Nombre: {}".format(self.__nombre))
        print("Telefono: {}".format(self.__telefono))

    def __str__(self):
        return ((
            'DNI: {} \nNombre: {} \nDireccion: {} \nTelefono: {}').format(
            self.getDni(), self.getNombre(), self.getDireccion(),
            self.getTelefono()
            )
        )