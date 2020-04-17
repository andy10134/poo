import camion as Ca
import cosecha as Co

def buscarcamion(lista, camiones):
    for cosecha in lista:
        idBuscar= cosecha.getIdcamion()
        for camion in camiones:
            if(camion.getID() == idBuscar):
                tara =camion.getTara()
                cosecha.calcularKilos(tara)

        

        

if __name__ == "__main__":
    #camiones = []
    # lista = []
    #for i in range(20):
    #    lista.append([])
    #    for j in range(45):
    #        lista[i].append(None)
    #buscarcamion(lista, camiones)