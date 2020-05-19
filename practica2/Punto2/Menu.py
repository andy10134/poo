from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados
from Helados import Helado


class Menu:

    __switcher = None
    __helados = None
    __sabores = None

    def __init__(self, helados, sabores):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.salir
        }
        self.__helados = ManejaHelados()
        self.__sabores = ManejaSabores()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("BUENASSSS")
        aux = 1
        listaSabores = [100, 150, 250, 500, 1000]

        while(aux > 0 and aux < 6):
            print("Por favor seleccione un tipo de helado")
            print("1 - 100g")
            print("2 - 150g")
            print("3 - 250g")
            print("4 - 500g")
            print("5 - 1000g")
            aux = int(input())
            if(aux > 0 and aux < 6):
                aux = listaSabores[aux-1]
            else:
                print("Dato no valido")

        heladoAux = Helado(aux)
        s = "hagame el favor de elegir un sabor porfa,"
        s += " 0 para salir de la seleccion"
        print(s)
        self.__sabores.mostrarSabores()

        while(aux != 0 and heladoAux.getCantidadSabores() < 4):
            aux = int(input())
            if(aux > 0 and aux <= self.__sabores.getCantidad()):
                saborAux = self.__sabores.getSabor(aux)
                heladoAux.agregarSabor(saborAux)
                s = saborAux.getNombre() + " ha sido seleccionado te quedan "
                s += str(4 - heladoAux.getCantidadSabores()) + " sabores"
                print(s)
            else:
                print("Sabor invalido")

        self.__sabores.setVenta(
            heladoAux.getSabores(),
            heladoAux.getCantidadSabores(),
            heladoAux.getGramos()
            )
        self.__helados.ventaHelado(heladoAux)
        print("venta realizada")

    def opcion2(self):
        print("Los helados mas vendidos son: ")
        lista = self.__sabores.topVentas()
        for sabor in enumerate(lista):
            if(sabor[1][1] > 0):
                print("========================================")
                saborAux = self.__sabores.getSabor(sabor[1][0])
                print(
                    saborAux.getNombre(),
                    "\nDescripcion : ", saborAux.getDescripcion(),
                    "\nNumero: ", saborAux.getNumero(),
                    '\nPedido: ', sabor[1][1], " veces"
                )
                print("=========================================")

    def opcion3(self):
        numero = int(input("Ingrese el numero a buscar: "))

        if(numero > 0 and numero <= len(self.__sabores.getSabores())):
            print(
                "Se han vendido",
                self.__sabores.gramosVendidos(numero),
                "gramos"
            )
        else:
            print("numero invalido")

    def opcion4(self):
        aux = 1
        listaSabores = [100, 150, 250, 500, 1000]
        while(aux > 0 and aux < 6):
            print("Por favor seleccione un tipo de helado")
            print("1 - 100g")
            print("2 - 150g")
            print("3 - 250g")
            print("4 - 500g")
            print("5 - 1000g")
            aux = int(input())
            if(aux < 0 and aux > 6):
                print("Dato no valido, ingrese otra vez")
            else:
                aux = listaSabores[aux-1]
        self.__helados.buscarTipoHelado(aux)
