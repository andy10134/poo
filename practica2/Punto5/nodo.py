class Nodo():
    __profesor = None
    __siguiente = None
    def __init__(self, profesor):
        self.__profesor = profesor
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getsiguiente(self):
        return self.__siguiente