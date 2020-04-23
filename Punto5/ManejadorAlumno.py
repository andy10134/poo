import csv
import Alumno as A

class ManejadorAlumno:
    def __init__(self):
        self.__lista= carga()
        
    
    def carga(self):
        archivo  = open('./Punto5/alumnos.csv')
        reader   = csv.reader(archivo, delimiter=',')
        alumnos  = []
        for fila in reader

