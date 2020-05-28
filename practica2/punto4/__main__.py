from practica2.punto4.menu import Menu


if __name__ == "__main__":
    menu = Menu()
    salir = False

    print("Talleres App")
    while not salir:
        print("=====================================")
        print("0 Salir")
        opcion = int(input("Ingrese una opción: "))
        menu.opcion(opcion)
        salir = int(opcion) == 0
