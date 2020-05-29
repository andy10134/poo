import os
from manejadorEmpleado import ManejadorEmpleado


class Menu:

    __switcher = None

    def __init__(self):
        os.system("cls")
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
        os.system("cls")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        cant = int(input('Ingrese cantidad de empleados: '))
        self.__empleados = ManejadorEmpleado(cant)
        self.__empleados.mostrar()

    def opcion2(self):
        aux = str(input("Ingrese el DNI del trabajador:"))
        aux = self.__empleados.buscarDni(aux)
        if(aux != -1):
            print("ola")
        else:
            print("DNI invalido...")

    def opcion3(self):
        pass

    def opcion4(self):
        pass

    def salir(self):
        print('Salir')
