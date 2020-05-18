from Helados import Helado


class ManejaHelados:

    __helados = None

    def __init__(self):
        self.__helados = []

    def ventaHelado(self, helado):
        if (type(helado) is Helado):
            self.__helados.append(helado)
        else:
            print("Helado Invalido")

    def getCantidad(self):
        return len(self.__helados)

    def mostrarHelados(self):
        for helado in self.__helados:
            print("=================")
            print(self.__helados)

    def buscarTipoHelado(self, tipo):
        listaSabores= []
        for i in range(self.__dimension):
            if(type(self.__helados[i]) is Helado):
                if(self.__helados[i].getGramos() == tipo):   
                    sabores= self.__helados[i].getSabores()
                    for j in range(self.__helados[i].getCantidadSabores()):
                        indice = listaSabores.index(sabores[j].getNombre()) if sabores[j].getNombre() in listaSabores else -1
                        if(indice == -1):
                            listaSabores.append(sabores[j].getNombre())
        print('SABORES VENDIDOS: {}'.format(listaSabores))
