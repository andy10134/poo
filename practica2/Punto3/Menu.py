from ManejadorTalleres import ManejadorTalleres
from ManejadorPersona import ManejadorPersona
from ManejadorInscripciones import ManejadorInscripciones
import os


class Menu:

    __switcher = None
    __talleres = None
    __personas = None
    __inscripciones = None

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
        print("Seleccione el id del curso: ")
        self.__talleres.listarTalleres()
        aux = int(input("Ingrese el id del curso"))
        auxTaller = self.__talleres.getTallerById(aux)
                

    def opcion2(self):
        pass

    def opcion3(self):
        dni = input('Ingrese DNI: ')
        self.__inscripciones.buscarPersona(dni)
        
    def opcion4(self):
        pass
