from tkinter import Tk


class Aplicacion():
    __ventana = None
    __peso = None
    __altura = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.mainloop()


if __name__ == '__main__':
    mi_app = Aplicacion()
