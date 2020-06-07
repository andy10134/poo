import abc


class Persona:

    __cuil = ""
    __nombre = ""
    __apellido = ""
    __sueldo = 0
    __antiguiedad = 0

    def __init__(self, cuil, nombre, apellido, sueldo, antiguiedad, categoria = 0, area = '', tipo = '', carrera = '', cargo = '', catedra = ''):
        self.__cuil = cuil
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo
        self.__antiguiedad = antiguiedad

    def getCuil(self):
        return self.__cuil

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldoBasico(self):
        return self.__sueldo

    def getAntiguedad(self):
        return self.__antiguiedad

    def __str__(self):
        return((
            'Nombre: {}'
            '\nApellido: {} '
            '\nCuil: {} '
            '\nSueldo: {} '
            '\nAntiguedad: {}'.format(
                self.getNombre(),
                self.getApellido(),
                self.getCuil(),
                self.getSueldoBasico(),
                self.getAntiguedad()
                )
            ))
    
    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            atributos = dict(
                cuil = self.__cuil,
                nombre = self.__nombre,
                apellido = self.__apellido,
                sueldo = self.__sueldo,
                antiguedad = self.__antiguiedad
            )
        )
        return d

    @abc.abstractclassmethod
    def calcularSueldo(self):
        pass