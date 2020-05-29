from empleado import Empleado
from empleadoPlanta import EmpleadoPlanta
from empleadosExternos import EmpleadosExternos
from empleadoContratado import EmpleadoContratado
import numpy as np
import csv


class ManejadorEmpleado:

    __cantidad = 0
    __dimension = 0

    def __init__(self, cantidad):
        self.__dimension = cantidad
        self.__arreglo = np.empty(self.__dimension, dtype=Empleado)
        self.agregarEmpleadoPlanta()
        self.agregarEmpleadoContratado()
        self.agregarEmpleadoExterno()

    def agregarEmpleadoPlanta(self):
        archivo = open('./planta.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            self.__arreglo[self.__cantidad] = EmpleadoPlanta(
                fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]
            )
            self.__cantidad += 1
        archivo.close()

    def agregarEmpleadoContratado(self):
        archivo = open('./contratados.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            self.__arreglo[self.__cantidad] = EmpleadoContratado(
                fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]
            )
            self.__cantidad += 1
        archivo.close()

    def agregarEmpleadoExterno(self):
        archivo = open('./externos.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            self.__arreglo[self.__cantidad] = EmpleadosExternos(
                fila[0], fila[1], fila[2], fila[3], fila[4],
                fila[5], fila[6], fila[7], fila[8], fila[9]
            )
            self.__cantidad += 1
        archivo.close()
