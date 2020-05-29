import os
from practica2.punto4.manejadorEmpleado import ManejadorEmpleado


class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            0: self.salir
        }
        self.__empleados = None

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        os.system("clear")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        cant = int(input('Ingrese cantidad de empleados: '))
        self.__empleados = ManejadorEmpleado(cant)

    def opcion2(self):
        pass

    def opcion3(self):
        tarea = input('Ingrese tarea: ')
        self.__empleados.buscarTarea(tarea)

    def opcion4(self):
        pass

    def salir(self):
        print('Salir')
