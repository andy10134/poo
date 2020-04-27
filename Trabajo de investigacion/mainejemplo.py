from ejemplo import Persona

if __name__ == '__main__':
    lista= []
    nombre= input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    lista.append(Persona(nombre, dni))
    lista2= []
    lista2.append(Persona(nombre, dni))
    lista2.append(Persona(nombre, dni))
    lista.extend(lista2)
    lista.insert(2, Persona('Mario', '21345627'))
