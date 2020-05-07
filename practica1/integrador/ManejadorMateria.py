import csv
from claseMateria import Materia
class ManejadorMateria:

    __Materias=[]

    def __init__(self):
        self.__Materias = []
        archivo  = open('./MATERIAS.csv')
        bandera = True #Aparentemente la primera fila lleva los nombre de los campos
        reader   = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if(bandera):
                bandera = False
            else:    
                self.__Materias.append(Materia(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
        archivo.close()

    def agregarMateria(self, unaMateria):
        self.__Materias.append(unaMateria)

    def buscar_Materia_porCodigo(self, codigomateria):
        i = 0
        for materia in self.__Materias :    
            if(materia.get_cod_materia() == codigomateria):
                return i
            else:
                i +=1
        print('No se encontro materia con el codigo ', codigomateria )

    def buscar_Materia_porNombre(self,nombre):
        i = 0
        for materia in self.__Materias :    
            if(materia.get_nombre_materia() == nombre):
                return i
            else:
                i +=1
        print('No se encontro materia con el nombre ', nombre )

    def lista_Materia_con_correlativa(self, registro):
        pass

    def alumno_adeuda_correlativa(self,nombre):
        pass

    def busca_alumno(self,numero):
        i = 0
        for materia in self.__Materias :    
            if(materia.get_registro() == numero):
                return i
            else:
                i +=1
        print('No se encontro materia con el nombre ', nombre )        

    def listar(self):
        for materia in self.__Materias :
            materia.mostrar()