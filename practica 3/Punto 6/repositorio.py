from provincia import Provincia
from manejadorprovincias import ManejadorProvincias
from objectEncoder import ObjectEncoder

class RespositorioProvincias:
    __pac = None
    __manejador = None

    def __init__(self, pac):
        self.__pac = pac
        diccionario = self.__pac.leerJSONArchivo()
        self.__manejador = self.__pac.decodificarDiccionario(diccionario)
    
    def to_values(self, provincia):
        return provincia.getNombre(), provincia.getCapital(), provincia.getHabitantes(), provincia.getDepartamentos()
    
    def obtenerListaProvincias(self):
        return self.__manejador.getLista()
    
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia

    def grabarDatos(self):
        self.__pac.guardarJSONArchivo(self.__manejador.toJSON())