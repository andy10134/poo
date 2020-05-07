from Capitulo import Capitulo

class Libro: 
    __idLibro            = 0
    __titulo             = ""
    __autor              = ""
    __editorial          = ""
    __isbn               = 0
    __cantidadCapitulos  = 0
    __capitulos          = []

    def __init__(self, idLibro, titulo, autor, editorial, isbn, capitulos):
        self.__idLibro= idLibro
        self.__titulo= titulo
        self.__autor= autor
        self.__editorial= editorial
        self.__isbn = isbn
        self.__cantidadCapitulos= capitulos
        
    
    def agregarcapitulo(self, capitulo):
        self.__capitulos.append(Capitulo(capitulo[0], capitulo[1]))