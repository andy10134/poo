import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, ttk
import requests

class Aplicacion():

    __ventana = None
    __dolar = None
    __pesos = None

    def __init__(self):
        r = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
        x = r.json()
        i = 0
        while(i < len(x) and x[i]['casa']['nombre'] != 'Oficial'):
            i += 1
        if(i < len(x)):
            self.ventadolar = float(x[i]['casa']['venta'].replace(',','.'))
        self.__ventana = tk.Tk()
        self.__ventana.geometry('300x150')
        self.__ventana.resizable(0, 0)
        self.__ventana.title('Conversor de moneda')
        mainframe = ttk.Frame(self.__ventana, padding=(5, 5, 12, 5), relief='sunken', borderwidth=2)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.__dolar = StringVar()
        self.__pesos = StringVar()
        self.__dolar.trace('w', self.calcular)
        self.dolarEntry = ttk.Entry(mainframe, width= 6, textvariable= self.__dolar)
        self.dolarEntry.grid(column=2, row=1, sticky=(N, W))
        ttk.Label(mainframe, textvariable= self.__pesos).grid(column=2, row=2, sticky=(N, W))
        ttk.Label(mainframe, text='Dólares').grid(column=3, row=1, sticky=(N, W))
        ttk.Label(mainframe, text='Es equivalente a').grid(column=1, row=2, sticky=(N, W))
        ttk.Label(mainframe, text='Pesos').grid(column=3, row=2, sticky=(N, W))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=(N, W))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=7, pady=7)
        self.dolarEntry.focus()
        self.__ventana.mainloop()
       
    def calcular(self, *args):
        try:
            if(self.dolarEntry.get() == ""):
                self.__pesos.set("")
            else:
                dolar = float(self.dolarEntry.get())
                pesos = round(dolar / self.ventadolar, 2)
                self.__pesos.set(pesos)
        except ValueError:
            messagebox.showerror(title='Error', message='Ingrese un valor numérico')
            self.__dolar.set = ''
            self.dolarEntry.focus()
                

if __name__ == "__main__":
    app = Aplicacion()