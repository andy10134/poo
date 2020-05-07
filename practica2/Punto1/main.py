def opcion0():
    print("Hasta la proximaaaaa *dubstep de fondo*")

def opcion2():


def opcion1():


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


#Implemente un programa principal que permita:
#
#a. Cargar los datos de los libros en una instancia de la clase ManejaLibros.
# Para esto debe considerar que la biblioteca ha provisto un archivo libros.csv con los datos de los libros. 
# Este archivo presenta la siguiente estructura lógica: en una línea están los datos del libro y a continuación, 
#una línea por cada capítulo con sus respectivos datos. Esto se repite para cada libro. A continuación se da un ejemplo.

#b.     A través de un menú de opciones cumplir con las siguientes funcionalidades:
#1. Ingresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y
# cantidad total de páginas de un libro.
#2.   Dada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el
# título de alguno de sus capítulos.