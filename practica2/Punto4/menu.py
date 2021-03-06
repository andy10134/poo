import os
import numpy
from manejadorEmpleado import ManejadorEmpleado
from empleadoContratado import EmpleadoContratado


class Menu:

    __switcher = None

    def __init__(self):
        os.system("cls")
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            0: self.salir
        }
        self.__empleados = None

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        os.system("cls")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        cant = int(input('Ingrese cantidad de empleados: '))
        self.__empleados = ManejadorEmpleado(cant)

    def opcion2(self):
        aux = str(input("Ingrese el DNI del trabajador:"))
        self.__empleados.agregarHoras(aux)

    def opcion3(self):
        tarea = input('Ingrese tarea: ')
        self.__empleados.buscarTarea(tarea)

    def opcion4(self):
        self.__empleados.ayuda()

    def opcion5(self):
        self.__empleados.mostrarEmpleados()

    def salir(self):
        print('Salir')
