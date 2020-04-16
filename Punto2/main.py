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
        if (viajero.getIdViajero() == idBusqueda):
            return viajero
    return None

if __name__ == "__main__":
    
    lista   = []
    
    punto1(lista)
    Viajero = busqueda(lista, input("Ingrese el id del viajero a buscar: "))

    print(Viajero)
    
    if( Viajero != None ):
        print(Viajero)
        millas = Viajero.cantidadTotaldeMillas()
        aux    = float(input("Ingrese la cantidad de millas a Acumular (", millas,") :"))
        Viajero.acumularMillas(aux)
        aux    = float(input("Ingrese la cantidad de millas a canjear :"))
        Viajero.canjearMillas(aux)

    #test()