from persona import Persona

class Docente(Persona):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, carrera, cargo, catedra):
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def __str__(self):
        return((
            '{} \nCarrera: {} \nCargo: {} \nCatedra: {}'.format(
                super().__str__(),
                self.getCarrera(),
                self.getCargo(),
                self.getCatedra()
                )
            ))
    
    def calcularSueldo(self):
        sueldo = super().getSueldoBasico() + super().getSueldoBasico()*super().getAntiguedad()/100
        if(self.getCargo() == 'simple'):
            sueldo += super().getSueldoBasico()*10/100
        elif(self.getCargo() == 'semiexclusivo'):
            sueldo += super().getSueldoBasico()*20/100
        else:
            sueldo += super().getSueldoBasico()*50/100
        return sueldo
