from tkinter import ttk

class Aplicacion():
    __ventana = None
    __peso = None
    __altura = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Calculadora de IMC')

    def calcular(self):
        pass
    #    try:
    #        valor = float(self.__peso)
