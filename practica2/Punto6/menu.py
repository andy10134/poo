import os
from objectEncoder import ObjectEncoder
from lista import Lista



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
            7: self.opcion7,
            0: self.salir
        }
        self.__jsonF = ObjectEncoder()
        self.__lista = Lista()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        os.system("cls")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        pass

    def opcion2(self):
        pass

    def opcion3(self):
        pass

    def opcion4(self):
        pass

    def opcion5(self):
        pass

    def opcion6(self):
        pass

    def opcion7(self):
        d = self.__lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, 'vehiculos.json')

    def salir(self):
        print('Salir')
