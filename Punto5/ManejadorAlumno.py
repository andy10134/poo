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
    
    def punto2(self, anio, division):
        print("Alumno           Porcentaje")
        for Alumno in self.__listaAlumnos :
            if(Alumno.getAnio() == anio):
                if(Alumno.getDivision() == division):
                    if(Alumno.getInasistencias() > self.obtenerMaximo()):
                        print("{}           {}%".format(Alumno.getNombre(), Alumno.porcentaje()))