import ViajeroFrecuente as V
import csv

def test():
    archivo = open('./Punto2/test.csv') 
    reader  = csv.reader(archivo, delimiter=';')
    lista   = []

    for fila in reader:
        lista.append(V.ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()

def punto1():
    archivo = open('./Punto2/archivopasajeros.csv') 
    reader  = csv.reader(archivo, delimiter=';')
    lista   = []
    for fila in reader:
        lista.append(V.ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()

if __name__ == "__main__":
    punto1()