from ManejadorTalleres import ManejadorTalleres
from ManejadorInscripciones import ManejadorInscripciones
from ManejadorPersona import ManejadorPersona
from TallerCapacitacion import TallerCapacitacion
from Persona import Persona
import os


class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            0: self.salir
        }
        self.__talleres = ManejadorTalleres()
        self.__personas = ManejadorPersona()
        self.__inscripciones = ManejadorInscripciones()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')
# 2.Inscribir una persona en un taller: Se registra la inscripción
# (con el atributo pago en False) y la cantidad de vacantes del taller debe
# ser actualizada.

    def opcion1(self):
        os.system("clear")
        print("============================")
        print("Agregar Inscripcion")
        print("Seleccione a usuario: ")
        self.__personas.listarPersonas()
        aux = str(input("Ingrese el Dni de la persona: "))
        auxPersona = self.__personas.getPersonaByDni(aux)

        if(type(auxPersona) is Persona):
            os.system("clear")
            print(auxPersona)
            print("\n")
            print("============================")
            print("Seleccione el id del curso: ")
            self.__talleres.listarTalleres()
            aux = int(input("Ingrese el id del curso: "))
            auxTaller = self.__talleres.getTallerById(aux)
            if(type(auxTaller) is TallerCapacitacion):
                self.__inscripciones.agregarInscripcion(auxPersona, auxTaller)
        else:
            print("DNI no encontrado Cancelando inscripcion...")

    def opcion2(self):
        dni = input('Ingrese DNI: ')
        self.__inscripciones.buscarPersona(dni)

    def opcion3(self):
        id = int(input('Ingrese ID: '))
        self.__inscripciones.buscarTaller(id)

    def opcion4(self):
        dni = input('Ingrese DNI: ')
        self.__inscripciones.cambiarPago(dni)

    def opcion5(self):
        pass
