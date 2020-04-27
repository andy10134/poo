from persona import Persona

if __name__ == '__main__':
    lista= []
    nombre= input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    lista.append(Persona(nombre, dni))
