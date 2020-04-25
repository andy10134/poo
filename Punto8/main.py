import csv
from manejador import ManejadorC

def opcion0():
    print("Adiós")

def opcion1():
    print("Código de la opción 1")

def opcion2():
    print("Código de la opción 2")

def opcion3():
    print("Código de la opción 3")

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
    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Opción 1")
        print("2 Opción 2")
        print("3 Opción 3")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 