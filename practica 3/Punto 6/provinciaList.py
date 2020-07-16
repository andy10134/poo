import tkinter as tk
from tkinter import messagebox
from provincia import Provincia

class ProvinciaList(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)