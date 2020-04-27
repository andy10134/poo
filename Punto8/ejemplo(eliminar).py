class Persona:
    __nombre    = ''
    __dni       = ''
    __domicilio = ''

    def __init__(self, nombre= '', dni= '', domicilio= ''):
        self.__nombre       = nombre
        self.__dni          = dni
        self.__domicilio    = domicilio
    
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni

    def getDomicilio(self):
        return self.__domicilio
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setDni(self, dni):
        self.__dni = dni
    
    def setDomicilio(self, domicilio):
        self.__domicilio = domicilio
        