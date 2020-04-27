class Persona:
    __nombre    = ''
    __dni       = ''

    def __init__(self, nombre= '', dni= '', domicilio= ''):
        self.__nombre       = nombre
        self.__dni          = dni
    
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setDni(self, dni):
        self.__dni = dni

    def __str__(self):
        return "\nNombre: {} DNI: {}".format(self.__nombre, self.__dni)
    
    def __repr__(self):
        return str(self)

    def __del__(self):
        print("Chau {}".format(self.__nombre))
        