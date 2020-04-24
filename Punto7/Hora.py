class Hora:
    
    def __init__(self, hora=0, minutos=0, segundos=0):

        if(hora <= 24 and hora >= 0):
            self.__hora = hora
        else:
            print("Dato invalido hora")

        if(minutos <= 60 and minutos >= 0):
            self.__minutos = minutos
        else:
            print("Dato invalido minutos")

        if(segundos <= 60 and segundos >= 0):
            self.__segundos = segundos
        else:
            print("Dato invalido segundos")
    
    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__minutos
    
    def getSegundos(self):
        return self.__segundos

    def Mostrar(self):
        print("la hora es : ", self.__hora, ":", self.__minutos, ":", self.__segundos, ".")
