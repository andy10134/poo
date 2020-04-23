import csv
import Alumno as A

class ManejadorAlumno:
    def __init__(self):
        self.__lista= self.carga()
        print(self.__lista)
        
    
    def carga(self):
        archivo  = open('./Punto5/alumnos.csv')
        reader   = csv.reader(archivo, delimiter=',')
        alumnos  = []
        for fila in reader:
            alumnos.append=(A.Alumno(fila[0], fila[1], fila[2], fila[3]))
        archivo.close()
        return alumnos


