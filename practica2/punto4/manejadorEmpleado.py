from practica2.punto4.empleado import Empleado
from practica2.punto4.empleadoPlanta import EmpleadoPlanta
from practica2.punto4.empleadosExternos import EmpleadosExternos
from practica2.punto4.empleadoContratado import EmpleadoContratado
import numpy as np
import csv
from datetime import date


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
    
    def buscarTarea(self, tarea):
        total = 0
        for empleado in self.__arreglo:
            if(type(empleado) is EmpleadosExternos):
                trabajo = empleado.getTrabajo()
                if(trabajo == tarea):
                    fechaActual = date.today()
                    if(empleado.getFechaFinal() > fechaActual):
                        total += empleado.getCostoObra()
        print('Monto total a pagar por la tarea {}: {}'.format(tarea, total))