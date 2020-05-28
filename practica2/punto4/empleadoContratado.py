from empleadoTerceros import EmpleadoTercero


class Contratado(EmpleadoTercero):

    __cantHoras = 0
    __valorHora = 50

    def __init__(self, dni, nombre, direccion, telefono,
                 fecha_inicio, fecha_fin, cantidad):
        self.__cantHoras = cantidad
        super().__init__(
            dni, nombre, direccion,
            telefono, fecha_inicio, fecha_fin
        )

    def getCantidad(self):
        return self.__cantHoras

    def getValor(self):
        return self.__valorHora

    def __str__(self):
        return ('Cantidad de horas trabajadas: {}'.format(self.getCantidad()))
