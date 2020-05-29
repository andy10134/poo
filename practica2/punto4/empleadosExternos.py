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
        super().__init__(dni, nombre, direccion,
                         telefono, fecha_inicio, fecha_fin)

    def getCostoObra(self):
        return self.__obra

    def getSeguroVida(self):
        return self.__seguro_vida

    def getViaticos(self):
        return self.__viaticos

    def getTrabajo(self):
        return self.__trabajo

    def calcularSueldo(self):
        sueldo = self.__obra - self.__viaticos - self.__seguro_vida
        return sueldo
