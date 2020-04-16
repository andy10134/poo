class ViajeroFrecuente:

    def __init__(self, idViajero = "" , DNI=None, nombre=None, apellido=None, millasAcumuladas=None):
        self.__idViajero        = idViajero 
        self.__DNI              = DNI
        self.__nombre           = nombre
        self.__apellido         = apellido
        self.__millasAcumuladas = millasAcumuladas

    def cantidadTotaldeMillas(self):
        return self.__millasAcumuladas

    def acumularMillas(self, millasUltimoViaje):
        if(type(millasUltimoViaje) is int){
            
        }
    
    def canjearMillas(self, millasCanje):