from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados
from Helado import Helado


def opcion1():
    print("BUENASSSS")
    aux = 1

    while(aux != 100 and aux != 150 and aux != 250 and aux != 500 and aux != 1000 ):
        print("Por favor seleccione un tipo de helado")
        print("100g")
        print("150g")
        print("250g")
        print("500g")
        print("1000g")
        aux = int(input())

    heladoAux = Helado(aux)
    print("hagame el favor de elegir un sabor porfa, 0 para salir de la seleccion")
    sabores.mostrarSabores()

    while(aux != 0 and heladoAux.getCantidadSabores() < 4):
        aux = int(input())
        saborAux = sabores.getSabor(aux)
        if(type(saborAux) is not None):
            heladoAux.agregarSabor(saborAux)
            print(saborAux.getNombre(), " ha sido seleccionado te quedan ", str(4 - heladoAux.getCantidadSabores()), "sabores")
        else:
            print("Sabor invalido")

    helados.ventaHelado(heladoAux)


def opcion2():
    pass


def opcion0():
    print("Hasta la proximaaaaa *dubstep de fondo*")


switcher = {0: opcion0, 1: opcion1, 2: opcion2}


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
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0
        helados.mostrarHelados()
