import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, ttk, font
from vista.listapacientes import ListaPacientes


class Aplicacion(tk.Tk):
    
    __ventana = None

    def __init__(self):
        self.geometry('550x450')
        self.resizable(0, 0)
        self.title('Lista de Pacientes')
        self.mainframe = ttk.Frame(self.__ventana, padding=(5, 5, 12, 5), borderwidth=2)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.lista = ListaPacientes(self)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.__ventana.mainloop()



 
 