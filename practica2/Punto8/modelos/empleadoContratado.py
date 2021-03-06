from modelos.empleadosTerceros import EmpleadoTercero


class EmpleadoContratado(EmpleadoTercero):

    __cantHoras = 0
    valorHora = 50

    def __init__(self, dni, nombre, direccion, telefono,
                 fecha_inicio, fecha_fin, cantidad):
        self.__cantHoras = int(cantidad)
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

    @classmethod
    def setValor(cls, valor):
        cls.valorHora = valor

    def agregarHoras(self, horas):
        if(horas > 0):
            self.__cantHoras += horas
        else:
            print("Hora invalida...")

    def __str__(self):
        return ((
            '{} \nCantidad de horas trabajadas: {}'
            ).format(
                super().__str__(),
                self.getCantidad()
            )
        )
