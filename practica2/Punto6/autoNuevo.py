from auto import Auto

class autoNuevo(Auto):

    __version = ""

    def __init__(self, modelo, puertas, color, precio, version):
        self.__version = version

        super().__init__(modelo, puertas, color, precio)
    
    def getVersion(self):
        return self.__version

    def __str__(self):
        return ("{} \nVersion: {}".format(
            super().__str__(), self.getVersion()
            ))