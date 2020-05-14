from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados
from Helado import Helado


#def opcion1():
#    print("BUENASSSS")
#    aux = 1
#    listaSabores = [100, 150, 250, 500, 1000]
#
#    while(aux > 0 and aux < 6):
#        print("Por favor seleccione un tipo de helado")
#        print("1 - 100g")
#        print("2 - 150g")
#        print("3 - 250g")
#        print("4 - 500g")
#        print("5 - 1000g")
#        aux = int(input())
#        if(aux > 0 and aux < 6):
#            aux = listaSabores[aux-1]
#        else:
#            print("Dato no valido")
#
#    heladoAux = Helado(aux)
#    s = "hagame el favor de elegir un sabor porfa,"
#    s = "0 para salir de la seleccion"
#    print(s)
#    sabores.mostrarSabores()
#
#    while(aux != 0 and heladoAux.getCantidadSabores() < 4):
#        aux = int(input())
#        saborAux = sabores.getSabor(aux)
#        if(type(saborAux) is not None):
#            heladoAux.agregarSabor(saborAux)
#            s = saborAux.getNombre() + " ha sido seleccionado te quedan"
#            s = str(4 - heladoAux.getCantidadSabores()) + "sabores"
#            print(s)
#        else:
#            print("Sabor invalido")
#
#    helados.ventaHelado(heladoAux)
#    print("venta realizada")

def opcion1():
    print("BUENASSSS")
    aux = 1
    listaSabores = [100, 150, 250, 500, 1000]

    while(aux > 0 and aux < 6):
        print("Por favor seleccione un tipo de helado")
        print("1 - 100g")
        print("2 - 150g")
        print("3 - 250g")
        print("4 - 500g")
        print("5 - 1000g")
        aux = int(input())
        if(aux > 0 and aux < 6):
            aux = listaSabores[aux]
        else:
            print("Dato no valido")

    heladoAux = Helado(aux)
    s = "hagame el favor de elegir un sabor porfa,"
    s += " 0 para salir de la seleccion"
    print(s)
    sabores.mostrarSabores()

    while(aux != 0 and heladoAux.getCantidadSabores() < 4):
        aux = int(input())
        saborAux = sabores.getSabor(aux)
        if(type(saborAux) is not None):
            heladoAux.agregarSabor(saborAux)
            s = saborAux.getNombre() + " ha sido seleccionado te quedan"
            s += str(4 - heladoAux.getCantidadSabores()) + "sabores"
            print(s)
        else:
            print("Sabor invalido")

    sabores.setVenta(heladoAux.getSabores(), heladoAux.getCantidadSabores(), heladoAux.getGramos())
    helados.ventaHelado(heladoAux)
    print("venta realizada")


def opcion2():
    print("Los helados mas vendidos son: ")
    lista = sabores.topVentas()
    print(lista)


def opcion4():
    aux = 1
    while(aux > 0 and aux < 6):
        print("Por favor seleccione un tipo de helado")
        print("1 - 100g")
        print("2 - 150g")
        print("3 - 250g")
        print("4 - 500g")
        print("5 - 1000g")
        aux = int(input())
        if(aux < 0 and aux > 6):
            print("Dato no valido, ingrese otra vez")
        else:
            tipo = aux
            aux = -1
    helados.buscarTipoHelado(tipo)


def opcion3():
    numero = int(input("Ingrese el numero a buscar"))

    if(numero > 0 and numero <= len(sabores.getSabores())):
        sabores.getGramos(numero)
    else:
        print("numero invalido")


def opcion0():
    print("Hasta la proximaaaaa *dubstep de fondo*")


switcher = {0: opcion0, 1: opcion1, 2: opcion2, 3: opcion3, 4: opcion4}


def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()


sabores = ManejaSabores()
helados = ManejaHelados()

if __name__ == "__main__":
    bandera = False

    print("Bienvenido al conito")
    while not bandera:
        print("")
        print("0 Salir")
        print("1.Registrar un helado vendido (instancia de la clase helado).")
        print("2.Mostrar el nombre de los 5 sabores de helado más pedidos.")
        print("3.Estimar el total de gramos vendidos.")
        print("4.Ingresar un tipo de helado para mostrar los sabores vendidos en ese tamaño")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0
        helados.mostrarHelados()
