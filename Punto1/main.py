import csv
import email as E

def test():
    archivo     = open('C:/Users/User/Desktop/GIT/poo/Punto1/testemail.csv')
    reader      = csv.reader(archivo, delimiter = ';')
    for fila in reader:
        emailtest= E.Email()
        flag=emailtest.crearCuenta(fila[0],fila[1])
        if(flag==True):
            emailtest.cambiarContrasenia(fila[1])

def punto4(lista):
    archivo     = open('/home/andy/Escritorio/git/poo/Punto1/direccionesgmail.csv')
    reader      = csv.reader(archivo, delimiter = ';')
    auxiliar    = E.Email()
    i           = 0

    for fila in reader :

        if (auxiliar.crearCuenta(fila[0],fila[1])):
            lista.append(E.Email())
            lista[i].crearCuenta(fila[0],fila[1])
            i+=1
        else:
            print("Email invalido")

    archivo.close()
    dominio     = input("Ingrese el dominio a buscar:")

    i           = 0

    for email in lista :
        
        if(email.getDominio() == dominio):
            i+=1

    print("Se han encontrado {} emails con el dominio {}".format( i, dominio))
    
if __name__ == "__main__":
    
    test()
    print('--------------------------------------------')
    print('Ingrese los siguientes datos:')
    nombre      = input('nombre: ')
    direccion   = input('direccion email: ')
    email       = E.Email()
    email.crearCuenta(direccion)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, direccion))
    email.cambiarContrasenia(input("Ingrese su clave para comenzar con el cambio de pass: "))
    print('--------------------------------------------')
    otroemail   = E.Email()
    otroemail.crearCuenta('informatica.fcefn@gmail.com')
    print('FELICIDADES SE EJECUTO EL PUNTO3')

    listaEmails = []
    #punto4(listaEmails)
