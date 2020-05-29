from empleadoTerceros import EmpleadoTercero


class Contratado(EmpleadoTercero):

    __cantHoras = 0
    valorHora = 50

    def __init__(self, dni, nombre, direccion, telefono,
                 fecha_inicio, fecha_fin, cantidad):
        self.__cantHoras = cantidad
        super().__init__(
            dni, nombre, direccion,
            telefono, fecha_inicio, fecha_fin
        )

    def calcularSueldo(self):
        sueldo = 0
        sueldo = self.__cantHoras * self.getValor()
        return sueldo

    def getCantidad(self):
        return self.__cantHoras

    @classmethod
    def getValor(cls):
        return cls.valorHora

    def __str__(self):
        return ('Cantidad de horas trabajadas: {}'.format(self.getCantidad()))
