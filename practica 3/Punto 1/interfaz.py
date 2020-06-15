import tkinter as tk
import tkinter.ttk as ttk


class App(ttk.Frame):

    def __init__(self, master=None, **kw):
        ttk.Frame.__init__(self, master, **kw)
        self.__peso = tk.StringVar()
        self.__altura = tk.StringVar()
        self.__imc = tk.StringVar()
        self.__imcEstado = tk.StringVar()

        canvas_2 = tk.Canvas(self)
        canvas_2.config(background='#ffffff', cursor='arrow', height='341', width='580')
        canvas_2.grid()
        canvas_2.grid_propagate(0)
        pesoEntry = ttk.Entry(self, textvariable=self.__peso)
        pesoEntry.config(cursor='arrow', font='{roboto} 10 {}', justify='left', takefocus=False)
        _text_ = '''Ej: 50'''
        pesoEntry.delete('0', 'end')
        pesoEntry.insert('0', _text_)
        pesoEntry.place(anchor='nw', bordermode='ignore', relheight='0.1', relwidth='0.70', relx='0.2', rely='0.25', x='0', y='0')
        alturaEntry = ttk.Entry(self, textvariable=self.__altura)
        alturaEntry.config(font='{roboto} 10 {}', takefocus=False)
        _text_ = '''Ej: 120'''
        alturaEntry.delete('0', 'end')
        alturaEntry.insert('0', _text_)
        alturaEntry.place(anchor='nw', bordermode='inside', relheight='0.1', relwidth='0.70', relx='0.2', rely='0.45', x='0', y='0')
        pesoLabel = ttk.Label(self)
        pesoLabel.config(background='#ffffff', compound='top', cursor='arrow', font='{Roboto} 9 {}')
        pesoLabel.config(justify='left', text='Peso :')
        pesoLabel.place(anchor='nw', relx='0.09', rely='0.255', x='0', y='0')
        alturaLabel = ttk.Label(self)
        alturaLabel.config(anchor='w', background='#ffffff', font='{roboto} 9 {}', takefocus=True)
        alturaLabel.config(text='Altura :')
        alturaLabel.place(anchor='nw', relx='0.09', rely='0.455', x='0', y='0')
        tituloFrame = ttk.Frame(self)
        tituloLabel = ttk.Label(tituloFrame)
        tituloLabel.config(cursor='arrow', font='{roboto} 12 {bold}', takefocus=False, text='Calculadora de IMC')
        tituloLabel.place(anchor='nw', relx='0.36', rely='0.30', x='0', y='0')
        tituloFrame.config(cursor='arrow', height='200', width='200')
        tituloFrame.place(anchor='nw', relheight='0.2', relwidth='1.0', rely='0', x='0', y='0')
        pesobtn = ttk.Button(self)
        pesobtn.config(state='disabled', text='Kg')
        pesobtn.place(anchor='nw', relheight='0.1', relwidth='0.1', relx='0.8', rely='0.25', x='0', y='0')
        cmbtn = ttk.Button(self)
        cmbtn.config(state='disabled', text='cm')
        cmbtn.place(anchor='nw', relheight='0.1', relwidth='0.1', relx='0.8', rely='0.45', x='0', y='0')
        self.__alertFrame = tk.Frame(self)
        self.__icmLabel = tk.Label(self.__alertFrame)
        self.__icmLabel.config(background='#E0F0D9', cursor='arrow', font='TkDefaultFont', foreground='#39773a')
        self.__icmLabel.config(text='Tu IMC (indice de masa corporal) es :')
        self.__icmLabel.place(anchor='nw', relx='0.05', rely='0.10', x='0', y='0')
        self.__estadoImc = tk.Label(self.__alertFrame, textvariable=self.__imcEstado)
        self.__estadoImc.config(background='#e0f0d9', font='{Arial} 20 {}', foreground='#39773a', relief='flat')
        self.__estadoImc.config(text='Peso Normal')
        self.__estadoImc.place(anchor='nw', relwidth='1.0', rely='0.35', x='0', y='0')
        self.__icmValLabel = tk.Label(self.__alertFrame, textvariable=self.__imc)
        self.__icmValLabel.config(background='#e0f0d9', font='{roboto} 10 {bold}', foreground='#39773a', text='icmValLabel')
        self.__icmValLabel.place(anchor='nw', relx='0.67', rely='0.10', x='0', y='0')
        self.__alertFrame.config(background='#e0f0d9', height='200', width='200')
        self.__alertFrame.place(anchor='nw', relheight='0.23', relwidth='0.7', relx='0.15', rely='0.74', x='0', y='0')
        calcular = tk.Button(self, command=self.calcularImc)
        calcular.config(activebackground='#5cb95c', activeforeground='#fff', background='#5cb95c', borderwidth='0')
        calcular.config(compound='top', disabledforeground='#fff', foreground='#fff', text='Calcular')
        calcular.place(anchor='nw', relheight='0.10', relwidth='0.35', relx='0.1', rely='0.605', x='0', y='0')
        limpiar = tk.Button(self, command=self.limpiar)
        limpiar.config(activebackground='#5cb95c', activeforeground='#fff', background='#5cb95c', borderwidth='0')
        limpiar.config(foreground='#fff', text='Limpiar')
        limpiar.place(anchor='nw', relheight='0.10', relwidth='0.35', relx='0.55', rely='0.605', x='0', y='0')
        self.setAlertColor()

    def setAlertColor(self,  color='#fff', font='#fff'):
        self.__alertFrame.config(background=color)
        self.__icmLabel.config(background=color, foreground=font)
        self.__icmValLabel.config(background=color, foreground=font)
        self.__estadoImc.config(background=color, foreground=font)

    def limpiar(self):
        self.setAlertColor()
        self.__peso.set('')
        self.__altura.set('')

    def calcularImc(self):
        peso = float(self.__peso.get())
        altura = float(self.__altura.get())
        altura = altura**2
        altura = altura/10000
        imc = peso/(altura)
        imc = round(imc, 2)

        if(imc <= 18.5):
            self.__imcEstado.set("Peso inferior al normal")
            self.__imc.set(str(imc) + ' Kg/m2')
            self.setAlertColor('#e2e3e5', '#383d41')
        elif(imc <= 24.9):
            self.__imcEstado.set("Peso normal")
            self.__imc.set(str(imc) + ' Kg/m2')
            self.setAlertColor('#d4edda', '#155724')
        elif(imc < 29.9):
            self.__imcEstado.set("Peso superior al normal")
            self.__imc.set(str(imc) + ' Kg/m2')
            self.setAlertColor('#fff3cd', '#856404')
        else:
            self.__imcEstado.set("Obesidad")
            self.__imc.set(str(imc) + ' Kg/m2')
            self.setAlertColor('#f8d7da', '#721c24')


if __name__ == '__main__':
    root = tk.Tk()
    widget = App(root)
    root.geometry('580x341')
    root.title('Calculadora de IMC')
    root.resizable(0,0)
    root.config()
    widget.pack(expand=False, fill='both')
    root.mainloop()
