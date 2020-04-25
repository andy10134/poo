import csv
from conjunto import Conjunto

def opcion0():
    print("Adiós")

def opcion1():
    union= conjunto1 + conjunto2

def opcion2():
    interseccion= conjunto1 - conjunto2

def opcion3():
    conjunto1 == conjunto2

switcher = {
    0: opcion0,
    1: opcion1, 
    2: opcion2, 
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    archivo  = open('./Punto8/conjunto1.csv')
    conjunto1 = Conjunto(archivo)
    archivo.close()
    archivo  = open('./Punto8/conjunto2.csv')
    conjunto2 = Conjunto(archivo)
    archivo.close()
    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Union de conjuntos")
        print("2 Interseccion de conjuntos")
        print("3 Verificar si los conjuntos son iguales")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0 