
class Alumno:

    cantidadMaximaDeInasistencias = 10
    cantidadTotalDeClases = 100

    def __init__(self, nombre, anio, division, cantidadDeInasistencias):
        self.__nombre = nombre
        self.__division = int(division)
        self.__anio = int(anio)
        self.__cantidadDeInasistencias = int(cantidadDeInasistencias)
    
    def getAnio(self):
        return self.__anio
    
    def getDivision(self):
        return self.__division
    
    def getNombre(self):
        return self.__nombre
    
    def getInasistencias(self):
        return self.__cantidadDeInasistencias
    
    def porcentajei(self):
        porc =(self.__cantidadDeInasistencias*100)/self.getCantidadTotalDeClases()
        return porc
    
    def __str__(self):
        return (self.getNombre() + ' ' +  self.getAnio()  +  ' ' +  self.getDivision()  +  ' ' +  self.getInasistencias())

    @classmethod
    def getCantidadMaximaDeInasistencias(cls):
        return cls.cantidadMaximaDeInasistencias
    
    @classmethod
    def getCantidadTotalDeClases(cls):
        return cls.cantidadTotalDeClases

    @classmethod
    def setCantidadMaximaDeInasistencias(cls, cantidadDeInasistencias):
        cls.cantidadMaximaDeInasistencias = cantidadDeInasistencias
 