from auto import Auto


class AutoNuevo(Auto):

    __version = ""
    __marca = 'FIAT'

    def __init__(self, modelo, puertas, color, precio, version):
        self.__version = version

        super().__init__(modelo, puertas, color, precio)

    def getVersion(self):
        return self.__version

    def getMarca(self):
        return self.__marca

    def calcularPrecio(self):
        precio = super().getPrecioBase() + (10*super().getPrecioBase())/100

        if(self.getVersion == "full"):
            precio += (2*super().getPrecioBase())/100

        return precio

    def __str__(self):
        return ("{} \nVersion: {}".format(
            super().__str__(), self.getVersion()
            ))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        modelo=super().getModelo(),
                        cantPuertas=super().getCantidadPuertas(),
                        color=super().getColor(),
                        precioBase=super().getPrecioBase(),
                        version=self.__version
                    )
        )
        return d
