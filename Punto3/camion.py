import re

class Camion:
    
    def __init__(self, idcamion=None, patente=None, nombre=None, marca= None, tara= None):
        self.__id       = re.sub("[^0-9\n\.]", '', idcamion)
        self.__nombre   = re.sub("[^a-zA-Z\n\.]", '', nombre)
        self.__patente  = re.sub("[^a-zA-Z0-9\n\.]", '', patente)
        self.__marca    = re.sub("[^a-zA-Z\n\.]", '', marca)
        self.__tara     = re.sub("[^0-9\n\.]", '', tara)
    
    def getPatente(self):
        return self.__patente

    def getNombre(self):
        return self.__nombre

    def getID(self):
        return self.__id

    def getTara(self):
        return self.__tara

    def __str__ (self):
        return (self.getID() + ' ' +  self.getNombre()  +  ' ' +  self.getPatente()  +  ' ' +  self.getTara())