import zope.interface


class IGerente (zope.interface.Interface):

    def modificarBasicoEPlanta(self, dni, nuevoBasico):

        pass

    def modificarViaticoEExterno(self, dni, nuevoViatico):

        pass

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        pass
