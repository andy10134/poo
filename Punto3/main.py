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
        camiones.append(Ca.Camion(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()
        

if __name__ == "__main__":
    camiones    = []
    cosecha     = Co.Cosecha()
    punto1(camiones)
    #punto2(cosecha)
    #buscarcamion(lista, camiones)