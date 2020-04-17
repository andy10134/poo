
class cosecha:
    def __init__(self, dia=None, idcamion=None, pesocamion=None):
        self.__dia          = dia
        self.__idcamion     = idcamion
        self.__pesoCamion   = pesocamion

    def calcularKilos(self, taracamion):
        kilos= self.__pesoCamion - taracamion
        return kilos
    
    def getIdCamion(self):
        return self.__idcamion