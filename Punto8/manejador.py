import csv
from conjunto import 

class ManejadorC:
    def __init__(self):
        self.__lista = []
        archivo  = open('./Punto8/conjunto1.csv')
        reader   = csv.reader(archivo, delimiter=',')
        for fila in reader:
            print('hola')
        archivo.close()
