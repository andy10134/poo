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
        
    
    def agregarCapitulo(self, capitulo):
        self.__capitulos.append(Capitulo(capitulo[0], capitulo[1]))

    def getId(self):
        return int(self.__idLibro)
    
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getEditorial(self):
        return self.__editorial

    def getIsbn(self):
        return self.__isbn
    
    def getCantidadC(self):
        return int(self.__cantidadCapitulos)


    def listarCapitulos(self):
        for capitulo in self.__capitulos:
            print(' -{}'.format(capitulo.getTitulo()))
    
    def calcularTotalPaginas(self):
        total= 0
        for capitulo in self.__capitulos:
            total+= capitulo.getCantidadPaginas()
        return total

    def buscarEnCapitulo(self, palabra):
        bandera= True
        i=0
        while(bandera and i < self.getCantidadC()):
            titulo= self.__capitulos[i].getTitulo()
            if(titulo.find(palabra) > -1):
                bandera= False
                print('Título: {}'.format(self.getTitulo()), 'Autor: {}'.format(self.getAutor()))
            i+= 1
        return bandera