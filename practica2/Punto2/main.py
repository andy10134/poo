from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados


def opcion0():
    pass


def opcion2():
    pass


def opcion1():
    pass


switcher = {0: opcion0, 1: opcion1, 2: opcion2}


def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()


if __name__ == "__main__":
    bandera = False
    sabores = ManejaSabores()
    helados = ManejaHelados()

    while not bandera:
        print("")
        print("0 Salir")
        print("1.Registrar un helado vendido (instancia de la clase helado).")
        print("2.Mostrar el nombre de los 5 sabores de helado más pedidos.")
        print("3.Estimar el total de gramos vendidos.")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion) == 0
