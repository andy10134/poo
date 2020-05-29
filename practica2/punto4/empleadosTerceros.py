from practica2.punto4.empleado import Empleado
from datetime import date
from empleado import Empleado


class EmpleadoTercero(Empleado):

    __fechaInicio = ""
    __fechaFinalizacion = ""

    def __init__(self, dni, nombre, direccion,
                 telefono, fecha_inicio, fecha_fin):
        aux = fecha_inicio.split('/')
        dia = aux[0]
        mes = aux[1]
        año = aux[2]
        self.__fechaInicio = date(año, mes, dia)
        aux = fecha_fin.split('/')
        dia = aux[0]
        mes = aux[1]
        año = aux[2]
        self.__fechaFinalizacion = date(año, mes, dia)
        super().__init__(dni, nombre, direccion, telefono)

    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinalizacion
