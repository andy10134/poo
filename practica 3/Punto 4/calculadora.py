from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox, ttk
from fraccion import Fraccion

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=3, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=4, row=3, sticky=W)
        ttk.Button(mainframe, text='AC', command=self.borrarPanel).grid(column=4, row=4, sticky=W)
        self.__fraccionbtn = ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, "/"))
        self.__fraccionbtn.grid(column=3, row=7, sticky=W)
        self.__panel.set('')
        self.__ventana.resizable(0, 0)
        panelEntry.focus()
        self.__ventana.mainloop()
    
    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            valor=self.__panel.get()
            self.__operadorAux=None
            if(valor.find("/") >= 0):
                valor = valor.split("/")
                self.__primerOperando = Fraccion(*valor)
            else:
                self.__primerOperando=int(valor)
            self.__panel.set(numero)
            self.__fraccionbtn.config(state="normal")

    def borrarPanel(self):
        self.__panel.set('')
        self.__operador.set("AC")
        self.__fraccionbtn.config(state="normal")
        self.__operadorAux = None

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        try:
            if operacion=='+':
                resultado=operando1+operando2
            elif operacion=='-':
                resultado=operando1-operando2
            elif operacion=='*':
                resultado=operando1*operando2
            elif operacion=='%':
                resultado=operando1/operando2
            if(type(resultado) is Fraccion):
                resultado = resultado.simplificar()
            self.__panel.set(str(resultado))
        except ZeroDivisionError:
            messagebox.showerror(title='Error', message='Division entre cero!')
            self.__panel.set = ''

    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            valor = self.__panel.get()
            if(valor.find("/") >= 0):
                valor = valor.split("/")
                self.__segundoOperando = Fraccion(*valor)
            else:
                self.__segundoOperando=int(valor)
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux=None
        if op=='/':
            self.ponerNUMERO(op)
            self.__fraccionbtn.config(state="disabled")
        elif self.__operador.get()=='' or self.__operador.get()=="AC":
            self.__operador.set(op)
            self.__operadorAux=op
        else:
            operacion=self.__operador.get()
            valor = self.__panel.get()
            if(valor.find("/") >= 0):
                valor = valor.split("/")
                self.__segundoOperando = Fraccion(*valor)
            else:
                self.__segundoOperando=int(valor)
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set(op)
            self.__operadorAux=op
