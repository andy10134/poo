from models.docente import Docente
from models.investigador import Investigador


class DocenteInvestigador(Docente, Investigador):

    __importeExtra = 0
    __categoria = ''

    def __init__(self, cuil, nombre, apellido, sueldo, antiguedad, carrera, cargo, catedra, area, tipo, categoria, importeExtra):
        super().__init__(cuil, nombre, apellido, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__importeExtra = importeExtra
        self.__categoria = categoria

    def getImporte(self):
        return self.__importeExtra

    def getCategoria(self):
        return self.__categoria

    def __str__(self):
        return (
            '{}\nImporte Extra: {}\nCategoría: {}'.format(
                super().__str__(), self.__importeExtra, self.__categoria
            )
        )

    def calcularSueldo(self):
        sueldo = Docente.calcularSueldo(self) + self.__importeExtra
        return sueldo

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            atributos=dict(
                cuil=super().getCuil(),
                nombre=super().getNombre(),
                apellido=super().getApellido(),
                sueldo=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                area=super().getArea(),
                tipo=super().getTipo(),
                importeExtra=self.__importeExtra,
                categoria=self.__categoria
            )
        )
        return d
