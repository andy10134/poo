from auto import Auto
# Además, para los usados se registrará la patente, el año y el kilometraje.


class AutoUsado(Auto):

    __anio = 0
    __kilometraje = 0
    __patente = ""

    def __init__(self, anio, patente, kilometraje, modelo, puertas, color, precio):
        self.__anio = int(anio)
        self.__patente = patente
        self.__kilometraje = kilometraje

        super().__init__(modelo, puertas, color, precio)
    
    def getAnio(self):
        return self.__anio

    def getPatente(self):
        return self.__patente

    def getKilometraje(self):
        return self.__kilometraje

    def calcularAntiguedad(self):
        return (2020 - self.getAnio())

    def calcularPrecio(self):
        precio = super().getPrecioBase() - (super().getPrecioBase() * self.calcularAntiguedad())/100
        if(self.__kilometraje > 100000):
            precio += (super().getPrecioBase()*2)/100
        return precio


    def __str__(self):
        return((
            'Año: {} \nPatente: {} \nKilometraje: {}'.format(self.getAnio(), self.getPatente(), self.getKilometraje())
            ))