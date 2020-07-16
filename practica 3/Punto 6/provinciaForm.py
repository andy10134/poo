import tkinter as tk
from tkinter import messagebox
from provincia import Provincia

class ProvinciaForm(tk.LabelFrame):

    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensación Térmica", "Humedad")
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10,
        **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de un Provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (provincia.getNombre(), provincia.getCapital(),
        provincia.getHabitantes(), provincia.getDepartamentos())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo Provincia
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia
        
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewProvincia(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = ProvinciaForm(self)
        self.form.fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos")
        self.btn_add = tk.Button(self, text="Confirmar",
        command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
        
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class StateProvinciaForm(ProvinciaForm):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)