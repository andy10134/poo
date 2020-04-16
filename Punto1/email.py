from validar import is_valid_email

class Email:
    __idCuenta    = ''
    __dominio     = ''
    __extension   = ''
    __contrasenia = None

    #Constructor de la clase emaicambiarContraseniacambiarContrasenial
    def __init__ (self, idCuenta = '', dominio ='', extension = '', contrasenia = ' '):
        self.__idCuenta    = idCuenta
        self.__dominio     = dominio
        self.__extension   = extension
        self.__contrasenia = contrasenia
    
    #Obtener Dominio del objeto
    def getDominio(self):
        return self.__dominio
    
    #Retornar Email
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + "." + self.__extension
    
    #Obtener Contrasenia
    def __getContrasenia(self):
        return self.__contrasenia  if self.__contrasenia!=None else print("No tiene clave asignada.")
    
    #Modificar Contrasenia
    def __setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
    
    #Cambiar contrasenia
    def cambiarContrasenia(self,contrasenia):
        if( contrasenia == self.__getContrasenia()):
            self.__setContrasenia(input("Ingrese la nueva clave: "))
            print('SE CAMBIO LA CONTRASEÑA')
        else:
            print("Las claves no coinciden.")

    #Crear Cuenta
    def crearCuenta(self, direccion, contrasenia = None):
        if(is_valid_email(direccion)):
            IDcuenta, extension          = direccion.split('@')
            dominio, extension           = extension.split('.',1)
            self.__idCuenta     =IDcuenta
            self.__dominio      =dominio
            self.__extension    =extension
            if ( contrasenia != None ):
                self.__setContrasenia(contrasenia)
            else:
                self.__contrasenia = input('Ingrese password de {} :'.format(self.retornaEmail()))
            print('Email valido')
            return True
        else:
            print("Email invalido")
            return False
