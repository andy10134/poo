from empleadosTerceros import EmpleadoTercero


class EmpleadosExternos(EmpleadoTercero):

    __obra = 0
    __seguro_vida = 0
    __viaticos = 0
    __trabajo = ""

    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio,
                 fecha_fin, obra, seguro_vida, viaticos, trabajo):
        self.__obra = obra
        self.__seguro_vida = seguro_vida
        self.__viaticos = viaticos
        self.__trabajo = trabajo
        super().__init__(dni, nombre, direccion, telefono, fecha_inicio, fecha_fin)