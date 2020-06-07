import os
import numpy
from manejadorEmpleado import ManejadorEmpleado
from modelos.empleadoContratado import EmpleadoContratado
from interfaces.igerente import IGerente
from interfaces.itesorero import ITesorero


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
            6: self.opcion6,
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

    def opcion6(self):
        usuario=input('Usuario (Tesorero/Gerente): ')
        clave=input('Clave:')
        if(usuario.lower() == 'Tesorero'.lower() and clave =='uTesoreso/ag@74ck'):
            self.tesorero(ITesorero(self.__empleados))
        elif(usuario.lower() == 'Gerente'.lower() and clave == 'uGerente/ufC77#!1'):
            self.gerente(IGerente(self.__empleados))
        else:
            print("Nombre y/o contraseña invalidas")

    def tesorero(self, manejaTesorero):
        print(IGerente.providedBy(manejaTesorero))
        dni = input('Ingrese dni del empleado: ')
        manejaTesorero.gastosSueldoPorEmpleado(dni)

    def gerente(self, manejaGerente):
        print("\n")

    def salir(self):
        print('Salir')
