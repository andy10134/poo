from TallerCapacitacion import TallerCapacitacion
import numpy as np
import csv


class ManejadorTalleres:
    __cantidad = 0
    __dimension = 1
    __incremeto = 1

    def __init__(self, cantidad=5):
        archivo = open('./punto3/csv/Talleres.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if(len(fila) == 1):
                self.__dimension = int(fila[0])
                self.__talleres = np.empty(
                    self.__dimension,
                    dtype=TallerCapacitacion
                )
            else:
                self.__talleres[self.__cantidad] = TallerCapacitacion(
                    int(fila[0]), fila[1], int(fila[2]), float(fila[3])
                )
                self.__cantidad += 1

    def listarTalleres(self):
        for taller in self.__talleres:
            if(type(taller) is TallerCapacitacion):
                if(taller.getVacantes() > 0):
                    print("=====================")
                    print("Id Taller: ", str(taller.getId()))
                    print("Taller: ", taller.getNombre())
        print('++++++++++++++++++++++')

    def buscarTaller(self, id):
        bandera = True
        i = 0
        while(bandera and i < self.__cantidad):
            taller = self.__talleres[i]
            if(type(taller) is TallerCapacitacion):
                if(taller.getId() == id):
                    bandera = False
                    taller.mostrarInscripciones()
                else:
                    i += 1

    def getTallerById(self, idTaller):
        i = 0
        while(self.__talleres[i].getId() != idTaller):
            i += 1

        if(i <= self.__dimension):
            return self.__talleres[i]
        else:
            return None
