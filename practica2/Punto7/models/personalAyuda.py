from models.persona import Persona


class PersonalAyuda(Persona):
    __categoria = ''


    def __init__(self, cuil, nombre, apellido, sueldo, antiguedad, categoria):
        super().__init__(cuil, nombre, apellido, sueldo, antiguedad)
        self.__categoria = categoria

    def getCategoria(self):
        return self.__categoria
    
    def __str__(self):
        return((
            '{} \nCategoria: {}'.format(
                super().__str__(),
                self.getCategoria()
                )
            ))
    
    def calcularSueldo(self):
        sueldo = super().getSueldoBasico() + super().getSueldoBasico()*super().getAntiguedad()/100
        if(1 <= self.getCategoria() and self.getCategoria() <= 10):
             sueldo += super().getSueldoBasico()*10/100
        elif(11 <= self.getCategoria() and self.getCategoria() <= 20):
            sueldo += super().getSueldoBasico()*20/100
        else:
            sueldo += super().getSueldoBasico()*30/100
        return sueldo
