
class Cosecha:
    def __init__(self):
        self.__lista  = []
        i   =0
        for i in range(20):
            self.__lista.append([])
            j   =0
            for j in range(45):
                self.__lista[i].append(None)
    
    def getlista(self):
        return self.__lista

