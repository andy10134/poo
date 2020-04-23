class FechaHora:

    # Sobrecarga de operadores
    #
    # Dada la clase FechaHora, del ejercicio 4, presente un menú de opciones que permita lo siguiente:
    #
    # 1- Sumar hora, para ello sobrecargue el operador binario suma (+).
    #
    # 2- Restar hora, para ello sobrecargue el operador binario resta (-).
    #
    # 3- Distinguir entre dos horas cuál es mayor, para ello sobrecargue el operador relacional mayor (>).
    #
    # definimos los atributos en el constructor por que la documentacion o al menos varios libros recomiendan
    # que aquellos atributos definidos fuera del constructor sean variables de clase

    def __init__(self, dia=1, mes=1, anio=2020, hora=0, minutos=0, segundos=0):
        if(mes <= 12 and mes > 0):
            self.__mes = mes
        else:
            print("Dato invalido")

        if(self.finMes() >= dia):
            self.__dia = dia
        else:
            print("Dato invalido")

        if(anio > 999):
            self.__anio = anio
        else:
            print("Dato invalido")

        if(hora <= 24 and hora >= 0):
            self.__hora = hora
        else:
            print("Dato invalido")

        if(minutos <= 60 and minutos >= 0):
            self.__minutos = minutos
        else:
            print("Dato invalido")

        if(segundos <= 60 and segundos >= 0):
            self.__segundos = segundos
        else:
            print("Dato invalido")

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
        print("El dia es ", self.__dia, "/", self.__mes, "/", self.__anio,
              " y la hora es : ", self.__hora, ":", self.__minutos, ":", self.__segundos, ".")

    def AdelantarHora(self, horas=0, minutos=0):
        self.__hora += horas
        self.__minutos += minutos

        if((self.__minutos > 60) or (self.__minutos == 60 and self.__segundos > 0)):
            self.__minutos = 0
            self.__hora += 1

        if(self.__hora > 24):
            dias = self.__hora//24
            self.setFecha(dias)
    
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

    def finMes(self):
        if(self.__mes == 2):
            return self.bisiesto()
        else:
            if(self.__mes > 8):
                if(self.__mes % 2 == 0):
                    return 30
                else:
                    return 31
            else:
                if(self.__mes % 2 != 0):
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

    def __add__(self,otraHora):
        self.AdelantarHora(otraHora)

    def __sub__(self, otraHora):
        self.__hora -= otraHora #-45

        if(self.__hora < 0):
            if( self.__hora < -24):
                dias = self.__hora//(-24)
                self.__dia -= dias
                self.__hora = self.__hora % (24)
            else:
                self.__dia -= 1
                self.__hora *= -1
            if(self.__dia <= 0):
                self.__dia += self.finMes() 
                self.__mes -= 1
                if(self.__mes == 0):
                    self.__mes = 12
                    self.__anio -= 1

    def __gt__(self, otraHora):
        
        if(type(otraHora) is int ):
            return self.__hora > otraHora
        else:
            if( self.__anio >= otraHora.getAnio() and self.__mes >= otraHora.getMes and self.__dia >= otraHora.getDia):
                if(self.__hora > otraHora.getHora):
                    return True
                else:
                    return False
            else:
                return True
