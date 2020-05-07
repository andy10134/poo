import csv
from ManejadorAlumno import ManejadorAlumno

def opcion0():
    print("Adiós")

def opcion2():
    inasistencias = int(input("Ingrese la nueva cantidad maxima de inasistencias: "))
    x.cambiarInasistencias(inasistencias)


def opcion1():
    anio        = int(input("Ingrese año: "))
    division    = int(input("Ingrese division: "))
    x.punto2(anio, division)

switcher = {
    0: opcion0, 
    1: opcion1, 
    2: opcion2 
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == "__main__":
    bandera = False
    x = ManejadorAlumno()

    while not bandera:
        print("")
        print("0 Salir")
        print("1 Liste nombre y porcentaje de inasistencias de los alumnos")
        print("2 Modificar la cantidad máxima de inasistencias permitidas.")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0 
