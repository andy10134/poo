import os
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
        aux = self.__empleados.buscarDni(aux)
        emplAux = self.__empleados[aux]

        if(aux != -1 and type(emplAux) is EmpleadoContratado):
            horas = int(input("Ingrese la cantidad de horas a agregar: "))
            emplAux.agregarHoras()
        else:
            print("DNI invalido...")

    def opcion3(self):
        tarea = input('Ingrese tarea: ')
        self.__empleados.buscarTarea(tarea)

    def opcion4(self):
        pass

    def opcion5(self):
        self.__empleados.mostrarEmpleados()

    def salir(self):
        print('Salir')
