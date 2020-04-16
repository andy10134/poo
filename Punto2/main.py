import ViajeroFrecuente as V
import csv

def test():
    archivo = open('./Punto2/test.csv') 
    reader  = csv.reader(archivo, delimiter=';')
    lista   = []

    for fila in reader:
        lista.append(V.ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()    

def punto1(lista):
    archivo = open('./Punto2/archivopasajeros.csv') 
    reader  = csv.reader(archivo, delimiter=';')
    
    for fila in reader:
        lista.append(V.ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()

def busqueda(lista,idBusqueda):
    for viajero in lista:
        if (viajero.cantidadTotaldeMillas() == idBusqueda):
            return viajero
    return None

if __name__ == "__main__":
    
    lista   = []
    
    punto1(lista)
    Viajero = busqueda(lista, int(input("Ingrese el id del viajero a buscar: ")))

    if( Viajero != None ):
        print()
    #test()