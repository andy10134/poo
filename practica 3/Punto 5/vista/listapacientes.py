import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox, ttk, font

class ListaPacientes(tk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.lb = tk.Listbox(self, height= 15)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, contacto, index=tk.END):
        pass
        #text = "{}, {}".format(contacto.getApellido(), contacto.getNombre())
        #self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)
