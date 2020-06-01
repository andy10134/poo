from auto import Auto
# Además, para los usados se registrará la patente, el año y el kilometraje.


class AutoUsado(Auto):

    __anio = 0
    __kilometraje = 0
    __patente = ""

    def __init__(self, anio, patente, kilometraje, modelo, puertas, color, precio):
        self.__anio = anio
        self.__patente = patente
        self.__kilometraje = kilometraje

        super().__init__(modelo, puertas, color, precio)