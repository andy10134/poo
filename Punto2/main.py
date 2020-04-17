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

def imprimir():
    print('________________________')
    print('Bienvenido al Menu')
    print('________________________')
    print()
    print('Opciones:')
    print('1-Consultar cantidad de millas')
    print('2-Acumular millas')
    print('3-Canjear millas')
    print('0. Salir')
    opcion= input('ingresar opcion: ')
    return opcion

def menu(Viajero):
    bandera = True
    while (bandera):
        opcion= int(imprimir())
        print('opcion: {}'.format(opcion))
        if opcion in range(4):
            if opcion == 0:
                print('Adios! Vuelva pronto')
                bandera=False
                pass
            if opcion == 1:
                millas = Viajero.cantidadTotaldeMillas()
                print('cantidad de millas: {}'.format(millas))
                pass
            if opcion == 2:
                aux    = float(input('Ingrese la cantidad de millas a Acumular:'))
                Viajero.acumularMillas(aux)
                pass
            if opcion == 3:
                millas2 = Viajero.cantidadTotaldeMillas()
                aux    = float(input("Ingrese la cantidad de millas a canjear ({}): ".format(millas2)))
                Viajero.canjearMillas(aux)
                pass
        else:
            print('Error, solo de aceptan numeros del 0 al 3')


if __name__ == "__main__":
    lista   = []
    punto1(lista)
    idviajero= input("Ingrese el id del viajero a buscar: ")
    Viajero = busqueda(lista, idviajero)
    if(Viajero != None):
        menu(Viajero)
    else:
        print('viajero no encontrado')
    test()