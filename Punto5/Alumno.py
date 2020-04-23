
class Alumno:

    cantidadMaximaDeInasistencias = 20
    cantidadTotalDeClases = 100

    def __init__(self, nombre, division, anio, cantidadDeInasistencias):
        self.__nombre = nombre
        self.__division = division
        self.__anio = anio
        self.__cantidadDeInasistencias = cantidadDeInasistencias

    @classmethod
    def getNombreCantidadMaximaDeInasistencias(cls):
        return cls.cantidadMaximaDeInasistencias
    
    @classmethod
    def getNombreCantidadTotalDeClases(cls):
        return cls.cantidadTotalDeClases

    @classmethod
    def setNombreCantidadMaximaDeInasistencias(cls, cantidadDeInasistencias):
        cls.cantidadMaximaDeInasistencias = cantidadDeInasistencias
 