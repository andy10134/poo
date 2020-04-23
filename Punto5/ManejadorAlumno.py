import csv
from Alumno import Alumno

class ManejadorAlumno:
    
    def __init__(self):
        pass
        
    def obtenerAlumnos(self):
        archivo  = open('./Punto5/alumnos.csv')
        reader   = csv.reader(archivo, delimiter=',')
        alumnos  = []
        for fila in reader:
            alumnos.append(Alumno(fila[0], fila[1], fila[2], fila[3]))
        archivo.close()
        return alumnos

    def cambiarInasistencias(self,inasistencias):
        Alumno.setNombreCantidadMaximaDeInasistencias(inasistencias)
    
    def obtenermaximo(self):
        maximo = Alumno.getNombreCantidadMaximaDeInasistencias()
        return maximo
  