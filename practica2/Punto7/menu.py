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
    
    def ingresarDatos(self):
        print('-----Ingrese datos del agente-----')
        tipo = input('Ingrese tipo de agente(docente, investigador, personal de ayuda o docente investigador): ')
        tipo = tipo.lower()
        if(tipo == "docente" or tipo == "investigador" or tipo == "personal de ayuda" or tipo == "docente investigador"):
            nombre = str(input('Ingrese nombre: '))
            apellido = str(input('Ingrese apellido: '))
            cuil = str(input('Ingrese cuil: '))
            sueldo = float(input('Ingrese sueldo: '))
            antiguedad = int(input('Ingrese antiguedad: '))
            if(tipo == 'docente'):
                carrera = str(input('Ingrese carrera: '))
                cargo = str(input('Ingrese cargo: '))
                catedra = str(input('Ingrese catedra: '))
                datos = [cuil, nombre, apellido, sueldo, antiguedad, carrera, cargo, catedra]
                return datos
            elif(tipo == 'investigador'):
                area = str(input('Ingrese area: '))
                tipo = str(input('Ingrese tipo de investigación: '))
                datos = [cuil, nombre, apellido, sueldo, antiguedad, area, tipo]
                return datos
            elif(tipo == 'personal de ayuda'):
                categoria = int(input('Ingrese categoría(del 1 al 22)'))
                datos = [cuil, nombre, apellido, sueldo, antiguedad, categoria]
            else:
                pass
        else:
            print('Tipo de agente invalido')
            return None

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
        posicion = int(input('Ingrese posicion: '))
        elemento = self.__lista.mostrarElemento(posicion-1)

        if(elemento is not None):
            print("Posicion {}: ".format(posicion))
            print(elemento.__class__.__name__)
        else:
            print("Indice no valido")

# "4-Ingresar por teclado el nombre de una carrera y generar un" 
# "listado ordenado por nombre con todos los datos de los agentes"
# " que se desempeñan como docentes investigadores.")
    def opcion4(self):
        carrera = str(input("Ingrese el nombre de la carrera: "))
        docentesInvesticadores = self.__lista.listarDocentesInvestigadores()
        for docente in docentesInvesticadores:
            print(docente)

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
