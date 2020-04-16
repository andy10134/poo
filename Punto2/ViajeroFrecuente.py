import re

class ViajeroFrecuente:

    def __init__(self, idViajero = "" , DNI=None, nombre=None, apellido=None, millasAcumuladas=None):
        self.__idViajero        = idViajero 
        self.__DNI              = DNI
        self.__nombre           = re.sub("[^a-zA-Z\n\.]", '', nombre)
        self.__apellido         = re.sub("[^a-zA-Z\n\.]", '', apellido)
        self.__millasAcumuladas = float(millasAcumuladas)
    
    def __str__(self):
        cadena = "El id del viajero {0} tiene por nombre {1} {2} con DNI:{3} y millas acumuladas {4}"
        return cadena.format(self.__idViajero, self.__DNI, self.__nombre, self.__apellido, self.__millasAcumuladas)

    def cantidadTotaldeMillas(self):
        return self.__millasAcumuladas

    def acumularMillas(self, millasUltimoViaje):
        if(type(millasUltimoViaje) is float and millasUltimoViaje > 0):
            self.__millasAcumuladas += millasUltimoViaje
        else:
            print("Millas invalidas")            
    
    def canjearMillas(self, millasCanje):
        if(type(millasCanje) is float and millasCanje <= self.__millasAcumuladas):
            self.__millasAcumuladas-= millasCanje
        else:
            print("Error en la operacion")

    def getIdViajero(self):
        return self.__idViajero
