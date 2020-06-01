from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    salir = False
    print("MiAuto.com")
    while not salir:
        print("=====================================")
        print("0 Salir")
        print("1-Insertar un vehículo en la colección en una posición determinada.")
        print("2-Agregar un vehículo a la colección.")
        print("3-Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
        print("4-Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
        print("5-Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
        print("6-Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print("7-Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
        opcion = int(input("Ingrese una opción: "))
        menu.opcion(opcion)
        salir = int(opcion) == 0
