from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    salir = False
    print("App Centro de Cómputos UNSJ")
    while not salir:
        print("=====================================")
        print("0 Salir")
        print("1-Insertar a agentes a la colección.")
        print("2-Agregar agentes a la colección.")
        print(
            "3-Dada una posición de la Lista: Mostrar por pantalla qué tipo"
            " de agente se encuentra almacenado en dicha posición.")
        print(
            "4-Ingresar por teclado el nombre de una carrera y generar un" 
            "listado ordenado por nombre con todos los datos de los agentes"
            " que se desempeñan como docentes investigadores.")
        print(
            "5-Dada un área de investigación, contar la cantidad de agentes"
            " que son docente investigador, y la cantidad de investigadores"
            " que trabajen en ese área.")
        print(
            "6-Recorrer la colección y generar un listado que muestre nombre"
            " y apellido, tipo de Agente y sueldo de todos los agentes,"
            " ordenado por apellido.")
        print(
            "7-Dada una categoría de investigación (I, II, III, IV o V),"
            " listar apellido, nombre e importe extra, por docencia e investigación"
            " de todos los docentes investigadores que poseen esa categoría")
        print(
            "8-Almacenar los datos de todos los agentes en el archivo “personal.json”.")
        opcion = int(input("Ingrese una opción: "))
        menu.opcion(opcion)
        salir = int(opcion) == 0