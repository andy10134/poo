import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, ttk, font
from datetime import datetime
import requests

class Aplicacion():
    __ventana = None

    def __init__(self):
        self.__ventana = tk.Tk()
        self.__ventana.geometry('390x330')
        self.__ventana.resizable(0, 0)
        self.mainframe = ttk.Frame(self.__ventana, padding=(5, 5, 12, 5), borderwidth=2)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.fuente = font.Font(weight='bold')
        ttk.Label(self.mainframe, text='Moneda', font= self.fuente).grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(self.mainframe, text='Compra', font= self.fuente).grid(column=3, row=1, sticky=(N, W, E, S))
        ttk.Label(self.mainframe, text='Venta', font= self.fuente).grid(column=4, row=1, sticky=(N, W, E, S))
        self.boton = ttk.Button(self.mainframe, text='Actualizar', command=self.actualizar)
        self.label = ttk.Label(self.mainframe, text='')
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.actualizar()
        self.__ventana.mainloop()
    
    def actualizar(self, *args):
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        x = r.json()
        lista = []
        i = 2
        for cotizacion in x:
            if(cotizacion['casa']['nombre'].find('Dolar') != -1):
                if(cotizacion['casa']['compra'].find(',') != -1 and cotizacion['casa']['venta'].find(',') != -1):
                    lista.append(cotizacion)
        for cotizacion in lista:
            ttk.Label(self.mainframe, text=cotizacion['casa']['nombre']).grid(column=1, row=i, sticky=(N, W, E, S))
            ttk.Label(self.mainframe, text=cotizacion['casa']['compra']).grid(column=3, row=i, sticky=(N, W, E, S))
            ttk.Label(self.mainframe, text=cotizacion['casa']['venta']).grid(column=4, row=i, sticky=(N, W, E, S))
            i += 1
        x= datetime.now()
        self.label.config(text='Actualizado '+str(x))
        self.label.grid(column=2, row=i, columnspan=3 , sticky=(N, W, E, S))
        self.boton.grid(column=1, row=i, sticky=(N, W, E, S))