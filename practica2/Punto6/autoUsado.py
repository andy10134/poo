from auto import Auto


class AutoUsado(Auto):

    __anio = 0
    __kilometraje = 0
    __patente = ""
    __marca = ""

    def __init__(self, modelo, puertas, color, precio,
                 anio, patente, kilometraje, marca):
        self.__anio = int(anio)
        self.__patente = patente
        self.__kilometraje = kilometraje
        self.__marca = marca

        super().__init__(modelo, puertas, color, precio)

    def getAnio(self):
        return self.__anio

    def getPatente(self):
        return self.__patente

    def getKilometraje(self):
        return self.__kilometraje

    def getMarca(self):
        return self.__marca

    def calcularAntiguedad(self):
        return (2020 - self.getAnio())

    def calcularPrecio(self):
        precio = super().getPrecioBase() - (
            super().getPrecioBase() * self.calcularAntiguedad())/100
        if(self.__kilometraje > 100000):
            precio -= (super().getPrecioBase()*2)/100
        return precio

    def __str__(self):
        return((
            '{} \nAño: {} \nPatente: {} \nKilometraje: {} \nMarca: {}'.format(
                super().__str__(),
                self.getAnio(),
                self.getPatente(),
                self.getKilometraje(),
                self.getMarca())
            ))

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        modelo=super().getModelo(),
                        cantPuertas=super().getCantidadPuertas(),
                        color=super().getColor(),
                        precioBase=super().getPrecioBase(),
                        anio=self.__anio,
                        patente=self.__patente,
                        kilometraje=self.__kilometraje,
                        marca=self.__marca
                    )
        )
        return d