import os
from objectEncoder import ObjectEncoder
from lista import Lista
from auto import Auto
from autoUsado import AutoUsado


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

    def ingresarDatos(self):
        print('-----Ingrese datos del vehiculo-----')
        tipo = input('Ingrese tipo de auto(nuevo o usado): ')
        tipo = tipo.lower()
        if(tipo == "usado" or tipo == "nuevo"):
            modelo = str(input('Ingrese modelo: '))
            cantPuertas = int(input('Ingrese cantidad de puertas: '))
            color = str(input('Ingrese color: '))
            precioBase = float(input('Ingrese precio base: '))
            if(tipo == 'nuevo'):
                version = str(input('Ingrese version: '))
                datos = [modelo, cantPuertas, color, precioBase, version]
                return datos
            elif(tipo == 'usado'):
                marca = str(input('Ingrese marca: '))
                patente = str(input('Ingrese patente: '))
                anio = int(input('Ingrese año: '))
                kilometraje = float(input('Ingrese kilometraje: '))
                datos = [
                    modelo, cantPuertas, color, precioBase,
                    anio, patente, kilometraje, marca]
                return datos
        else:
            print('Tipo de vehiculo invalido')
            return None

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        os.system("cls")
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def opcion1(self):
        datos = self.ingresarDatos()
        if(type(datos) is Auto):
            posicion = int(input("Ingrese la posición en la "
                                 "cual quiere insertar el vehiculo: "))
            self.__lista.agregarVehiculo(datos, posicion)

    def opcion2(self):
        datos = self.ingresarDatos()
        if(type(datos) is Auto):
            self.__lista.agregarVehiculo(datos)

    def opcion3(self):
        posicion = int(input('Ingrese posicion: '))
        self.__lista.mostrarElemento(posicion-1)

    def opcion4(self):
        patente = str(input("Ingrese la patente: "))
        auxAuto = self.__lista.busquedaPatente(patente)

        if(type(auxAuto) is AutoUsado):
            nuevoPrecio = int(input("Ingrese el nuevo precio base: "))
            auxAuto.setPrecioBase(nuevoPrecio)
            print(
                "El nuevo precio del vehiculo es: {}".format(
                    auxAuto.calcularPrecio()))
        else:
            print(
                "No se ha encontrado el "
                "Vehiculo con la patente {}".format(patente))

    def opcion5(self):
        self.__lista.vehiculoEconomico()

    def opcion6(self):
        print("Autos en consesionaria: ")
        for auto in self.__lista:
            print("================{}================".format(type(auto)))
            print((
                "Modelo: {}"
                "\nCantidad de puertas: {}"
                "\nImporte de Venta: {}"
            ).format(
                auto.getModelo(),
                auto.getCantidadPuertas(),
                auto.calcularPrecio()
            ))

    def opcion7(self):
        d = self.__lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, 'vehiculos.json')

    def salir(self):
        print('Salir')
