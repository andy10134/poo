from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    salir = False
    print("Trabajadores App")
    while not salir:
        print("=====================================")
        print("0 Salir")
        print("1- Cargar empleados")
        print(
            "2- Registrar horas: Ingresar el DNI de un empleado y la cantidad",
            " de horas trabajadas hoy e incrementar la cantidad de las horas",
            " trabajadas del empleado."
        )
        print(
            "3- Total de tarea: Dada una tarea mostrar el monto",
            " a pagar para ella. Solo se consideran las tareas que",
            " no han finalizado."
        )
        print(
            "4- Ayuda: La empresa dará una ayuda solidaria",
            " a los empleados cuyo sueldo sea inferior a $25000;",
            " listar nombre, dirección y DNI de los empleados que",
            " les corresponde la ayuda"
        )
        print(
            "5- Calcular sueldo: Mostrar nombre, teléfono y sueldo",
            " a cobrar de todos los empleados."
        )
        opcion = int(input("Ingrese una opción: "))
        menu.opcion(opcion)
        salir = int(opcion) == 0
