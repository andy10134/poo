
class Alumno:

    cantidadMaximaDeInasistencias = 20
    cantidadTotalDeClases = 100

    def __init__(self, nombre, anio, division, cantidadDeInasistencias):
        self.__nombre = nombre
        self.__division = division
        self.__anio = anio
        self.__cantidadDeInasistencias = cantidadDeInasistencias
    
    def getAnio(self):
        return self.__anio
    
    def getDivision(self):
        return self.__division
    
    def getNombre(self):
        return self.__nombre
    
    def getInasistencias(self):
        return self.__cantidadDeInasistencias
    
    def porcentajei(self):
        porc =(self.__cantidadDeInasistencias*100)/self.getCantidadMaximaDeInasistencias()
        return porc

    @classmethod
    def getCantidadMaximaDeInasistencias(cls):
        return cls.cantidadMaximaDeInasistencias
    
    @classmethod
    def getCantidadTotalDeClases(cls):
        return cls.cantidadTotalDeClases

    @classmethod
    def setCantidadMaximaDeInasistencias(cls, cantidadDeInasistencias):
        cls.cantidadMaximaDeInasistencias = cantidadDeInasistencias
 