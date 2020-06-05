import os
from objectEncoder import ObjectEncoder
from lista import Lista


class Menu:

    __switcher = None

    def __init__(self, jsonF, lista):
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
        self.__jsonF = jsonF
        self.__lista = lista

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        os.system("cls")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        pass
    #    datos = self.ingresarDatos()
    #    if(type(datos) is not None):
    #        posicion = int(input("Ingrese la posición en la "
    #                             "cual quiere insertar el vehiculo: "))
    #        self.__lista.agregarVehiculo(datos, posicion)

    def opcion2(self):
        pass
    #    datos = self.ingresarDatos()
    #    if(type(datos) is not None):
    #        self.__lista.agregarVehiculo(datos)

    def opcion3(self):
        pass
    #    posicion = int(input('Ingrese posicion: '))
    #    self.__lista.mostrarElemento(posicion-1)

    def opcion4(self):
        pass

    def opcion5(self):
        pass

    def opcion6(self):
        pass

    def opcion7(self):
        pass

    def opcion8(self):
        d = self.__lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, './models/personal.json')

    def salir(self):
        print('Salir')
