from empleado import Empleado
from empleadoPlanta import EmpleadoPlanta
from empleadosExternos import EmpleadosExternos
from empleadoContratado import EmpleadoContratado
import numpy as np


class ManejadorEmpleado:

    __cantidad = 0

    def __init__(self, cantidad):
        self.__cantidad = cantidad
        self.__arreglo = np.empty(self.__cantidad, dtype=Empleado)

    def agregarEmpleado(self, ):
        pass