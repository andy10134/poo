from manejadorlibro import ManejadorLibro
from libro import Libro
import csv

def carga(manejadorLibro):
    archivo  = open('./practica2/Punto1/libros.csv')
    reader   = csv.reader(archivo, delimiter=',')
    i = 0
    for fila in reader:
        print(len(fila))
        if(len(fila) > 2):
            manejadorLibro.agregarlibro(fila)
            i+=1
            print("i dentro del if: ", i)
        else:
            print("i dentro del else: ", i)
            aux = manejadorLibro.getLibro(i-1)
            aux.agregarCapitulo(fila)
    archivo.close()


def opcion0():
    print("Adios")

def opcion2():
    palabra= input('Ingrese palabra a buscar: ')
    manejadorLibro.buscarPalabra(palabra)

def opcion1():
    idlibro=int(input('Ingrese id del libro: '))
    manejadorLibro.buscarLibro(idlibro)

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
    manejadorLibro = ManejadorLibro()
    
    carga(manejadorLibro)

    while not bandera:
        print("")
        print("0 Salir")
        print("1 Ingresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y cantidad total de páginas de un libro")
        print("2 Dada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el título de alguno de sus capítulos")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0 
