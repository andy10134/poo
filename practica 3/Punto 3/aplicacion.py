import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, ttk, font
import requests

class Aplicacion():
    __ventana = None

    def __init__(self):
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        x = r.json()
        lista = []
        for cotizacion in x:
            if(cotizacion['casa']['nombre'].find('Dolar') != -1):
                if(cotizacion['casa']['compra'].find(',') != -1 and cotizacion['casa']['venta'].find(',') != -1):
                    lista.append(cotizacion)
        self.__ventana = tk.Tk()
        self.__ventana.geometry('320x330')
        self.__ventana.resizable(0, 0)
        self.__ventana.title('Cotizaciones de dólar')
        mainframe = ttk.Frame(self.__ventana, padding=(5, 5, 12, 5), borderwidth=2)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.fuente = font.Font(weight='bold')
        ttk.Label(mainframe, text='Moneda', font= self.fuente).grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text='Compra', font= self.fuente).grid(column=3, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text='Venta', font= self.fuente).grid(column=4, row=1, sticky=(N, W, E, S))
        i = 2
        for cotizacion in lista:
            ttk.Label(mainframe, text=cotizacion['casa']['nombre']).grid(column=1, row=i, sticky=(N, W, E, S))
            ttk.Label(mainframe, text=cotizacion['casa']['compra']).grid(column=3, row=i, sticky=(N, W, E, S))
            ttk.Label(mainframe, text=cotizacion['casa']['venta']).grid(column=4, row=i, sticky=(N, W, E, S))
            i += 1
        ttk.Button(mainframe, text='Actualizar', command=self.__ventana.destroy).grid(column=1, row=i, sticky=(N, W))
        ttk.Label(mainframe, text='Actualizado').grid(column=2, row=i, columnspan=3 , sticky=(N, W, E, S))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.__ventana.mainloop()
    
    def actualizar(self):
        pass