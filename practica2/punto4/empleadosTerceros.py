from empleado import Empleado


class EmpleadoTercero(Empleado):

    fechaInicio = ""
    fechaFinalizacion = ""

    def __init__(self, dni, nombre, direccion,
                 telefono, fecha_inicio, fecha_fin):
        self.fechaInicio = fecha_inicio
        self.fechaFinalizacion = fecha_fin
        super().__init__(dni, nombre, direccion, telefono)
