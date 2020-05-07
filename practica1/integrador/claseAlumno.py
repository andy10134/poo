from FechaHora import FechaHora
#fromclaseFechahoraimportFechahora

class Alumno:

    __Nombre=""
    __Registro=0
    __DNI=""
    __Email=""
    __Fecha_nacimiento= FechaHora() 

    def __init__(self, nombre, registro, dni,email,fecha):
        if( type(nombre) is str):
            self.__Nombre = nombre
        else:
            print('Error de tipo de dato en nombre')
        
        if( type(registro) is int):
            self.__Registro = registro
        else:
            print('Error de tipo de dato en Nro de registro')
        
        if( type(dni) is str):
            self.__DNI = dni
        else:
            print('Error de tipo de dato en dni')
        
        if( type(email) is str):
            self.__Email = email
        else:
            print('Error de tipo de dato en email')
        
        if(type(fecha) is str):
            aux = fecha.split('/')
            dia = int(aux[0])
            mes = int(aux[1])
            anio = int(aux[2])

            self.__Fecha_nacimiento = FechaHora(dia, mes , anio)
        else:
            print('Error de tipo de dato en fecha')

    def get_registro(self):
        return self.__Registro

    def get_nombre(self):
        return self.__Nombre

    def get_dni(self):
        return self.__DNI

    def get_email(self):
        return self.__Email

    #se refiere a fecha de nacimiento
    def get_añol(self):
        return self.__Fecha_nacimiento.getAnio()

    def get_dia(self):
        return self.__Fecha_nacimiento.getDia()

    def get_mesl(self):
        return self.__Fecha_nacimiento.getMes()

    def saludo_cumpleaños(self):
        print('Se ha enviado un Saludo de cumpleaños a ', self.get_nombre(), ' de email ', self.get_email(), ' :) ')
        
    def mostrar(self):
        print('Alumno de nombre: ', self.get_nombre())
        print('Nro de registro: ', self.get_registro())
        print('DNI :', self.get_dni())
        print('Email: ', self.get_email())
        self.__Fecha_nacimiento.Mostrar()