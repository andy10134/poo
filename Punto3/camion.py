class camion:
    
    def __init__(self, idcamion=None, nombre=None, patente=None, marca= None, tara= None):
        self.__id       = idcamion
        self.__nombre   = nombre
        self.__patente  = patente
        self.__marca    = marca
        self.__tara     = tara
    

    def getID(self):
        return self.__id

    def getTara(self):
        return self.__tara