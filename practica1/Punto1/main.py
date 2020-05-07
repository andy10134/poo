import csv
import email as E

def test():
    archivo     = open('./Punto1/testemail.csv')
    reader      = csv.reader(archivo, delimiter = ';')
    for fila in reader:
        emailtest= E.Email()
        flag=emailtest.crearCuenta(fila[0],fila[1])
        if(flag==True):
            emailtest.cambiarContrasenia(fila[1])

def punto4(lista):
    archivo     = open('./Punto1/direccionesgmail.csv')
    reader      = csv.reader(archivo, delimiter = ';')
    i           = 0

    for fila in reader :

        lista.append(E.Email())
        lista[i].crearCuenta(fila[0],fila[1])
        i+=1

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
    print('Datos de su email:')
    idemail     = input('ID: ')
    dominio     = input('dominio: ')
    extension   = input('tipo de dominio: ')
    email       = E.Email(idemail, dominio, extension)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, email.retornaEmail()))
    email.cambiarContrasenia(input("Ingrese su clave para comenzar con el cambio de pass: "))
    print('--------------------------------------------')
    otroemail   = E.Email()
    otroemail.crearCuenta('informatica.fcefn@gmail.com')
    print('FELICIDADES SE CREO LA CUENTA (PUNTO 3)')
    print('--------------------------------------------')
    listaEmails = []
    punto4(listaEmails)
