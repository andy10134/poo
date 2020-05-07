class Capitulo:

    __titulo = ''
    __cantidadPaginas = 0

    def __init__(self, titulo, cantidadPaginas):
        self.__titulo = titulo
        self.__cantidadPaginas = cantidadPaginas

    def getTitulo(self):
        return self.__titulo
    
    def getCantidadPaginas(self):
        return int(self.__cantidadPaginas)

    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setCantidadPaginas(self, cantidadPaginas):
        self.__cantidadPaginas = cantidadPaginas