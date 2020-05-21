from practica2.Punto3.controllers.manejadorTalleres import ManejadorTalleres
from controllers import manejadorInscripciones
from controllers import manejadorPersona
from models.TallerCapacitacion import TallerCapacitacion
from models.Persona import Persona
import os


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
        os.system("cls")
        print("============================")
        print("Agregar Inscripcion")
        print("Seleccione a usuario: ")
        self.__personas.listarPersonas()
        auxPersona = self.__personas.getPersonaByDni()

        if(type(auxPersona) is Persona):
            print("============================")
            print("Seleccione el id del curso: ")
            self.__talleres.listarTalleres()
            aux = int(input("Ingrese el id del curso"))
            auxTaller = self.__talleres.getTallerById(aux)
            if(type(auxTaller) is TallerCapacitacion):
                self.__inscripciones.agregarInscripcion(auxPersona, auxTaller)
        else:
            print("DNI invalido Cancelando inscripcion...")

    def opcion2(self):
        dni = input('Ingrese DNI: ')
        self.__inscripciones.buscarPersona(dni)

    def opcion3(self):
        pass

    def opcion4(self):
        pass
