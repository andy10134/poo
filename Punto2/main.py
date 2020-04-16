import ViajeroFrecuente as V

def punto1():
    archivo=    open('./Punto2/archivopasajeros.csv') 
    reader=     csv.reader(archivo, delimiter=';')
    lista= []
    for fila in reader:
        lista.append(V.ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()
    print(lista)



if __name__ == "__main__":
    punto1()