from Menu import Menu

if __name__ == "__main__":
    salir = False
    menu = Menu()

    print("Bienvenido al conito")
    while not salir:
        print("")
        print("0 Salir")
        print("1.Registrar un helado vendido (instancia de la clase helado).")
        print("2.Mostrar el nombre de los 5 sabores de helado más pedidos.")
        print("3.Estimar el total de gramos vendidos.")
        print("4.Ingresar un tipo de helado para mostrar los " +
              " sabores vendidos en ese tamaño")
        opcion = int(input("Ingrese una opción: "))
        menu.opcion(opcion)
        salir = int(opcion) == 0
