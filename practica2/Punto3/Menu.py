from ManejadorTalleres import ManejadorTalleres
from ManejadorPersona import ManejadorPersona
from ManejadorInscripciones import ManejadorInscripciones


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
            5: self.salir
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

    def opcion1(self):
        pass

    def opcion2(self):
        pass

    def opcion3(self):
        pass

    def opcion4(self):
        pass
