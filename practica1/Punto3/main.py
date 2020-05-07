import camion as Ca
import cosecha as Co
import csv

def test():
    print("TEST")
    archivo  = open('./Punto3/test.csv')
    reader   = csv.reader(archivo, delimiter=';')
    camiones = []
    for fila in reader:
        camiones.append(Ca.Camion(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()
    print(camiones[0])
    print(camiones[1])
    print(camiones[2])
    print("TEST FINALIZADO")    


def buscarcamion(camiones, idBuscar):
    for camion in camiones:
        if(camion.getID() == idBuscar):
            tara =int(camion.getTara())
            return tara


def punto2(cosecha, camiones):
    archivo  = open('./Punto3/dias.csv')
    reader   = csv.reader(archivo, delimiter=',')
    lista    = cosecha.getlista()
    for fila in reader:
        tara = buscarcamion(camiones,fila[0])
        lista[int(fila[0])-1][int(fila[1])-1]= int(fila[2])-tara

def punto1(camiones):
    archivo= open('./Punto3/MOCK_DATA.csv')
    reader= csv.reader(archivo, delimiter=';')
    for fila in reader:
        camiones.append(Ca.Camion(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()
        

def opcion0():
    print("Adiós")

def opcion1():
    total=0
    idcamion= int(input('ingrese id del camion: '))
    if idcamion in range(1,4):
        lista= cosecha.getlista()
        for i in range(10):
            total += lista[idcamion-1][i]
        print('CANTIDAD TOTAL DE KILOS DESCARGADOS DEL CAMION {}: {}'.format(idcamion, total))
    else:
        print('El id ingresado no existe')


def opcion2():
    
    dia =  int(input("Ingrese el numero del dia:"))
    if ( dia > 0 and dia <=45 ):
        dia -= 1
        cosecha_del_dia = cosecha.getDiaCosecha(dia)

        a = "Patente"
        b = "Conductor"
        c = "Cantidad de Kilos"   

        print(a.rjust(33, ' '), b.rjust(33, ' '), c.rjust(33, ' '))
        for i in range(len(cosecha_del_dia)):
            print(camiones[i].getPatente().rjust(33, ' '), camiones[i].getNombre().rjust(33, ' '), str(cosecha_del_dia[i]).rjust(33, ' '))
    else : print("Dia invalido")


switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == "__main__":
    test()
    camiones    = []
    cosecha     = Co.Cosecha()
    punto1(camiones)
    punto2(cosecha, camiones)
    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Mostrar cantidad total de kilos descargados de un camion")
        print("2 Mostrar listado de dia")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 
    
