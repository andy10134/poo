
class Alumno:

    cantidadMaximaDeInasistencias = 20
    cantidadTotalDeClases = 100

    def __init__(self, nombre, anio, division, cantidadDeInasistencias):
        self.__nombre = nombre
        self.__division = division
        self.__anio = anio
        self.__cantidadDeInasistencias = cantidadDeInasistencias
    
    def getanio(self):
        return self.__anio
    
    def getdivision(self):
        return self.__division
    
    def getnombre(self):
        return self.__nombre
    
    def getinasistencias(self):
        return self.__cantidadDeInasistencias
    
    def porcentajei(self):
        porc =(self.__cantidadDeInasistencias*100)/self.cantidadMaximaDeInasistencias
        return porc

    @classmethod
    def getNombreCantidadMaximaDeInasistencias(cls):
        return cls.cantidadMaximaDeInasistencias
    
    @classmethod
    def getNombreCantidadTotalDeClases(cls):
        return cls.cantidadTotalDeClases

    @classmethod
    def setNombreCantidadMaximaDeInasistencias(cls, cantidadDeInasistencias):
        cls.cantidadMaximaDeInasistencias = cantidadDeInasistencias
 