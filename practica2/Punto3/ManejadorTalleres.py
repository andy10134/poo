import numpy as np
import csv
from TallerCapacitacion import TallerCapacitacion


class ManejadorTalleres:
    __cantidad = 0
    __dimension = 1
    __incremeto = 1

    def __init__(self, cantidad=5):
        archivo = open('./practica2/Punto3/Talleres.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(len(fila) < 1):
                self.__dimension = fila[0]
                self.__talleres = np.empty(
                    self.__dimension,
                    dtype=TallerCapacitacion
                )
            else:
                if(self.__cantidad == self.__dimension):
                    self.__dimension += self.__incremeto
                    self.__talleres.resize(self.__dimension)
                self.__talleres[self.__cantidad] = TallerCapacitacion(
                    fila[0], fila[1], fila[2], fila[3]
                )
                self.__cantidad += 1

    def listarTalleres(self):
        print("=====================")
        for taller in self.__talleres:
            if(type(taller) is TallerCapacitacion):
                print("Id Taller: ", str(taller.getId()))
                print("Taller: ", taller.getNombre())
                print("Vacantes: ", taller.getVacantes())
                print("Inscriptos: ", taller.mostrarInscripciones())
