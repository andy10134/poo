import csv
from claseAlumno import Alumno

class ManejadorAlumno:
    __Alumnos=[]

    def __init__(self):
        self.__Alumnos = []
        archivo  = open('./integrador/ALUMNOS.csv')
        reader   = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if(bandera):
                self.__Alumnos.append(Alumno(fila[0], int(fila[1]), fila[2], fila[3], fila[4]))
            else:
                bandera = True
        archivo.close()

    def agregar(self, unAlumno):
        self.__Alumnos.append(unAlumno)

    def buscar_Alumno_porRegistro(self, numeroregistro):
        for alumno in self.__Alumnos :    
            if(alumno.get_registro() == numeroregistro):
                return alumno

        print('No existe el alumno con el registro ', numeroregistro)
        return None

    def buscar_alumno_porNombre(self,nombre):
        i = 0

        for alumno in self.__Alumnos :    
            if(alumno.get_nombre() == nombre):
                return i
            else:
                i +=1

        print('No existe el alumno con nombre ', nombre)

    def listar(self):
        for alumno in self.__Alumnos :
            alumno.mostrar()
