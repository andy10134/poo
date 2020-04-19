import camion as Ca
import cosecha as Co
import csv

def buscarcamion(camiones, idBuscar):
    for camion in camiones:
        if(camion.getID() == idBuscar):
            tara =int(camion.getTara())
            return tara


def punto2(cosecha, camiones):
    archivo= open('./Punto3/dias.csv')
    reader= csv.reader(archivo, delimiter=';')
    lista= cosecha.getlista()
    for fila in reader:
        tara= buscarcamion(camiones,fila[0])
        lista[int(fila[0])-1][int(fila[1])-1]= int(fila[2])-tara
    print(lista)

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
    punto2(cosecha, camiones)