import csv
from Alumno import Alumno

class ManejadorAlumno:

    def __init__(self):
        self.__listaAlumnos = []
        archivo  = open('./Punto5/alumnos.csv')
        reader   = csv.reader(archivo, delimiter=',')
        for fila in reader:
            self.__listaAlumnos.append(Alumno(fila[0], fila[1], fila[2], fila[3]))
        archivo.close()

    def cambiarInasistencias(self,inasistencias):
        Alumno.setCantidadMaximaDeInasistencias(inasistencias)
    
    def obtenerMaximo(self):
        return Alumno.getCantidadMaximaDeInasistencias()
    
    def getLista(self):
        return self.__listaAlumnos

    def __str__ (self):
        return (self.getLista())
        

    def punto2(self, anio, division):
        for Alumno in self.__listaAlumnos :
            if(Alumno.getAnio() == anio):
                if(Alumno.getDivision() == division):
                    if(Alumno.getInasistencias() > self.obtenerMaximo()):
                        print(Alumno.getNombre().rjust(33,' '), Alumno.porcentajei())