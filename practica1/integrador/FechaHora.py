class FechaHora:

    def __init__(self, dia=1, mes=1, anio=2020, hora=0, minutos=0, segundos=0):
        if(anio > 999):
            self.__anio = anio
        else:
            print("Dato invalido año")
            self.__anio = 2020
            
        if(mes <= 12 and mes > 0):
            self.__mes = mes
        else:
            print("Dato invalido mes")
            self.__mes = 1

        if(self.finMes() >= dia):
            self.__dia = dia
        else:
            print("Dato invalido dia")
            self.__dia = 1

        

        if(hora <= 24 and hora >= 0):
            self.__hora = hora
        else:
            print("Dato invalido hora")
            self.__hora = 0

        if(minutos <= 60 and minutos >= 0):
            self.__minutos = minutos
        else:
            print("Dato invalido minutos")
            self.__minutos = 0

        if(segundos <= 60 and segundos >= 0):
            self.__segundos = segundos
        else:
            print("Dato invalido segundos")
            self.__segundos = 0

    def PonerEnHora(self, hora, minutos=0, segundos=0):
        if (hora <= 24 and hora > 0):
            self.__hora = hora
        else:
            print("Hora invalida")

        if (minutos >= 0 and minutos <= 60):
            self.__minutos = minutos
        else:
            print("Minutos invalidos")

        if (segundos >= 0 and segundos <= 60):
            self.__segundos = segundos
        else:
            print("Segundos invalidos")

    def Mostrar(self):
        print(self.__dia, "/", self.__mes, "/", self.__anio)

    def AdelantarHora(self, horas=0, minutos=0):
        self.__hora += horas
        self.__minutos += minutos

        if((self.__minutos > 60) or (self.__minutos == 60 and self.__segundos > 0)):
            self.__minutos = 0
            self.__hora += 1

        if(self.__hora > 24):
            dias = self.__hora//24
            self.setFecha(dias)
        return self

    def setFecha(self, dia=0):
        self.__dia += dia
        if(self.__dia > self.finMes()):
            self.__dia = 1
            self.__mes += 1
            if(self.__mes > 12):
                print("Feliz año nuevo ;)")
                self.__mes = 1
                self.__anio += 1

    def bisiesto(self):
        if(self.__anio % 4 == 0 and self.__anio % 100 != 0 or self.__anio % 400 == 0):
            return 29
        else:
            return 28

    def finMes(self, bandera = False, mes = 0):
        if(bandera):    
            if( mes == 2):
                return self.bisiesto()
            else:
                if( mes > 8):
                    if( mes % 2 == 0):
                        return 30
                    else:
                        return 31
                else:
                    if( mes % 2 != 0):
                        return 30
                    else:
                        return 31
        else:
            if(self.getMes() == 2):
                return self.bisiesto()
            else:
                if(self.getMes() < 8):
                    if(self.getMes() % 2 == 0):
                        return 30
                    else:
                        return 31
                else:
                    if(self.getMes() % 2 != 0):
                        return 30
                    else:
                        return 31

    def getHora(self):
        return self.__hora

    def getMes(self):
        return self.__mes

    def getDia(self):
        return self.__dia

    def getAnio(self):
        return self.__anio

    def getMinutos(self):
        return self.__minutos
    
    def getSegundos(self):
        return self.__segundos

    def setHora(self, hora):
        self.__hora = hora

    def setMinutos(self, minutos):
        self.__minutos = minutos
    
    def __add__(self, otraHora):
        if(type(otraHora) is int):
            nuevaHora = FechaHora(self.getDia(),self.getMes(),self.getAnio(),self.getHora(),self.getMinutos(),self.getSegundos())
            nuevaHora.AdelantarHora(otraHora)
            return nuevaHora
        else:
            hora = self.getHora() + otraHora.getHora()
            minutos = self.getMinutos() + otraHora.getMinutos()
            segundos = self.getSegundos() + otraHora.getSegundos()
            mes = self.getMes()
            dia = self.getDia()
            anio = self.getAnio()
            
            if( segundos > 60 ):
                segundos = 0
                minutos += 1
            if((minutos > 60) or (minutos == 60 and segundos > 0)):
                minutos = 0
                hora += 1
            if(hora > 24):
                dias = hora//24
                dia += dias
                hora -= 24
                if( dia > self.finMes()):
                    dia = 1
                    mes += 1
                    if(mes > 12):
                        print("Feliz año nuevo ;)")
                        mes = 1
                        anio += 1            
            return FechaHora(dia, mes, anio, hora, minutos, segundos)

    def __sub__(self, otraHora):
        dia = self.getDia()
        mes = self.getMes()
        anio = self.getAnio()
        minutos = self.getMinutos()
        segundos = self.getSegundos()
        hora = self.getHora()
        
        if(type(otraHora) is int): 
            hora -= otraHora
        else:
            hora -= otraHora.getHora()
            minutos -= otraHora.getMinutos()
            segundos -= otraHora.getSegundos()

            if( segundos < 0 ):
                segundos -= 60
                minutos -= 1
            if((minutos < 0)):
                minutos -= 60
                hora -= 1
        if(hora < 0):
            hora += 24
            dia -= 1
            if( dia <= 0):
                mes -= 1
                dia = self.finMes(True, mes)
                if(mes <= 0):
                    print("-Tuve una terrible pesadilla. Soñé que viajaba atrás en el tiempo. Era terrible. -Marty.")
                    mes = 12
                    anio -= 1            
        return FechaHora(dia,mes,anio,hora,minutos, segundos)

    def __gt__(self, otraHora):

        if(type(otraHora) is int):
            return self.getHora() > otraHora
        else:
            if(self.getAnio() >= otraHora.getAnio() and self.getMes() >= otraHora.getMes() and self.getDia() >= otraHora.getDia()):
                if(self.getHora() > otraHora.getHora()):
                    return True
                else:
                    return False
            else:
                return True
