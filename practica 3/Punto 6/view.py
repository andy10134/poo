import tkinter as tk
from tkinter import messagebox
from provinciaForm import ProvinciaForm
from provinciaForm import StateProvinciaForm
from provinciaForm import NewProvincia
from provincia import Provincia
from provinciaList import ProvinciaList

class ProvinciaView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.resizable(0, 0)
        self.list = ProvinciaList(self, height=15)
        self.form = StateProvinciaForm(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
        self.form.bind_save(ctrl.modificarProvincia)
        self.form.bind_delete(ctrl.borrarProvincia)
    
    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)
    
    def modificarProvincia(self, provincia, index):
        self.list.modificar(provincia, index)
    
    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        #obtiene los valores del formulario y crea un nuevo Provincia
    
    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()
        #Ver estado de Provincia en formulario de Provincia
    
    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)