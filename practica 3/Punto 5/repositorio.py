from paciente import Paciente
from manejadorPaciente import ManejadorPaciente
from objectEncoder import ObjectEncoder

class RespositorioPacientes:
    __pac = None
    __manejador = None

    def __init__(self, pac):
        self.__pac = pac
        diccionario = self.__pac.leerJSONArchivo()
        self.__manejador = self.__pac.decodificarDiccionario(diccionario)
    
    def to_values(self, paciente):
        return paciente.getApellido(), paciente.getNombre(), paciente.getEmail(), paciente.getTelefono()
    
    def obtenerListaPacientes(self):
        return self.__manejador.getLista()
    
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    
    def modificarPaciente(self, paciente):
        self.__manejador.actualizarPaciente(paciente)
        return paciente
    
    def borrarPaciente(self, paciente):
        self.__manejador.eliminarPaciente(paciente)
    
    def calcularIMC(self, paciente):
        imc = self.__manejador.calcularIMC(paciente)
        return imc

    def grabarDatos(self):
        self.__pac.guardarJSONArchivo(self.__manejador.toJSON())