import camion as Ca
import cosecha as Co
import csv

#def buscarcamion(lista, camiones):
#    for cosecha in lista:
#        idBuscar= cosecha.getIdcamion()
#        for camion in camiones:
#            if(camion.getID() == idBuscar):
#                tara =camion.getTara()
#                cosecha.calcularKilos(tara)
def punto1(camiones):
    archivo= open('./Punto3/MOCK_DATA.csv')
    reader= csv.reader(archivo, delimiter=';')
    for fila in reader:
        camiones.append(Ca.Camion())
        
        

if __name__ == "__main__":
    camiones = []
    punto1(camiones)
    #for i in range(20):
    #    lista.append([])
    #    for j in range(45):
    #        lista[i].append(None)
    #buscarcamion(lista, camiones)