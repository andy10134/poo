import tkinter as tk
from tkinter import messagebox
from paciente import Paciente

class PacienteForm(tk.LabelFrame):

    fields = ("Nombre", "Apellido", "Teléfono", "Peso", "Altura")
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10,
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

    def mostrarEstadoPacienteEnFormulario(self, paciente):
        # a partir de un Paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (paciente.getNombre(), paciente.getApellido(),
        paciente.getTelefono(), paciente.getPeso(), paciente.getAltura())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearPacienteDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo Paciente
        values = [e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return paciente
        
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewPaciente(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.form = PacienteForm(self)
        self.btn_add = tk.Button(self, text="Confirmar",
        command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()
        
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente


class Imc(tk.Toplevel):
    
    def __init__(self, parent, imc):
        super().__init__(parent)
        self.paciente = None
        self.form = ImcPaciente(self, imc) 
        self.btn_add = tk.Button(self, text="Volver",
        command=self.volver)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    def volver(self):
        self.destroy()
        
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente
    
class ImcPaciente(tk.LabelFrame):

    def __init__(self, master, imc, **kwargs):
        super().__init__(master, padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        print('hola')
        tk.Label(self.frame, text='IMC').grid(row=0, column=0, pady=5)
        entryimc = tk.Entry(self.frame, width=25)
        entryimc.grid(row=0, column=1, pady=5)
        _text_ = imc
        entryimc.delete('0', 'end')
        entryimc.insert('0', _text_)
        tk.Label(self.frame, text='Composicion Corporal').grid(row=1, column=0, pady=5)
        entryCC = tk.Entry(self.frame, width=25)
        entryCC.grid(row=1, column=1, pady=5)
        if(imc <= 18.5):
            text = "Peso inferior al normal"
            entryCC.delete('0', 'end')
            entryCC.insert('0', text)
        elif(imc <= 24.9):
            text = "Peso normal"
            entryCC.delete('0', 'end')
            entryCC.insert('0', text)
        elif(imc < 29.9):
            text = "Peso superior al normal"
            entryCC.delete('0', 'end')
            entryCC.insert('0', text)
        else:
            text = "Obesidad"
            entryCC.delete('0', 'end')
            entryCC.insert('0', text)
        self.frame.pack()

class UpdatePacienteForm(PacienteForm):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_imc = tk.Button(self, text='Ver IMC')
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_imc.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

    def bind_imc(self, callback):
        self.btn_imc.config(command=callback)