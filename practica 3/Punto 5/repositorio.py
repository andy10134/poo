from paciente import Paciente
from manejadorPaciente import ManejadorPaciente
from objectEncoder import ObjectEncoder

class RespositorioPacientes:
    __conn=None
    __manejador=None

    def __init__(self, conn):
        self.__conn=conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    
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
    
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador)