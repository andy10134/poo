
class Cosecha:
    def __init__(self):
        self.__lista  = []
        i   =0
        for i in range(3):
            self.__lista.append([])
            j   =0
            for j in range(10):
                self.__lista[i].append(None)
    
    def getlista(self):
        return self.__lista
    
    def getDiaCosecha(self, nrodia):
        dias = []
        for i in range(len(self.__lista)) :
            dias.append(self.__lista[i][nrodia])
        return dias