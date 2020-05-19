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
            print(helado)

    def buscarTipoHelado(self, tipo):
        listaSabores = []
        for helado in self.__helados:
            if(type(helado) is Helado):
                if(helado.getGramos() == tipo):   
                    sabores = helado.getSabores()
                    for j in range(helado.getCantidadSabores()):
                        indice = listaSabores.index(sabores[j].getNombre()) if sabores[j].getNombre() in listaSabores else -1
                        if(indice == -1):
                            listaSabores.append(sabores[j].getNombre())
        print('SABORES VENDIDOS: {}'.format(listaSabores))
