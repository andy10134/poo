from modelos.empleado import Empleado
from datetime import date


class EmpleadoTercero(Empleado):

    __fechaInicio = None
    __fechaFinalizacion = None

    def __init__(self, dni, nombre, direccion,
                 telefono, fecha_inicio, fecha_fin):
        aux = fecha_inicio.split('/')
        mes = int(aux[0])
        dia = int(aux[1])
        año = int(aux[2])
        self.__fechaInicio = date(año, mes, dia)
        aux = fecha_fin.split('/')
        mes = int(aux[0])
        dia = int(aux[1])
        año = int(aux[2])
        self.__fechaFinalizacion = date(año, mes, dia)
        super().__init__(dni, nombre, direccion, telefono)

    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinalizacion

    def __str__(self):
        return (
            ("{} \nFecha Inicio: {} \nFecha Fin: {}").format(
                super().__str__(),
                self.getFechaInicio(),
                self.getFechaFinal()
                )
        )
