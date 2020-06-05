from models.docente import Docente
from models.investigador import Investigador


class DocenteInvestigador(Docente, Investigador):

    __importeExtra = 0
    __categoria = ''

    def __init__(self, cuil, nombre, apellido, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, importeExtra, categoria):
        super().__init__(cuil, nombre, apellido, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
        self.__importeExtra = importeExtra
        self.__categoria = categoria
    
    def getImporte(self):
        return self.__importeExtra

    def __str__(self):
        return (
            'Importe Extra: {}'.format(
                self.__importeExtra
            )
        )
    
    def calcularSueldo(self):
        sueldo = Docente.calcularSueldo() + self.__importeExtra
        return sueldo

    def __gt__(self, docente):
        return self.getNombre() > docente.getNombre() 