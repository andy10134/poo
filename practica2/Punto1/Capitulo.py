class Capitulo:

    __titulo = ""
    __cantidadPaginas = ""

    def __init__(self, titulo, cantidadPaginas):
        __titulo = titulo
        __cantidadPaginas = cantidadPaginas

    def getTitulo(self):
        return self.__titulo
    
    def getCantidadPaginas(self):
        return self.__cantidadPaginas

    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setCantidadPaginas(self, cantidadPaginas):
        self.__cantidadPaginas = cantidadPaginas