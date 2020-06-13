import tkinter as tk
import tkinter.ttk as ttk


class InterfazApp:
    def __init__(self, master=None):
        # build ui
        mainwindows = ttk.Frame(master)
        canvas_2 = tk.Canvas(mainwindows)
        canvas_2.config(background='#ffffff')
        canvas_2.grid()
        canvas_2.grid_propagate(0)
        entry_1 = ttk.Entry(mainwindows)
        entry_1.config(cursor='arrow', font='{roboto} 10 {}', justify='left', takefocus=False)
        _text_ = '''Ej: 50'''
        entry_1.delete('0', 'end')
        entry_1.insert('0', _text_)
        entry_1.place(anchor='nw', bordermode='ignore', relheight='0.1', relwidth='0.70', relx='0.2', rely='0.25', x='0', y='0')
        entry_2 = ttk.Entry(mainwindows)
        entry_2.config(font='{roboto} 10 {}', takefocus=False)
        _text_ = '''Ej: 120'''
        entry_2.delete('0', 'end')
        entry_2.insert('0', _text_)
        entry_2.place(anchor='nw', bordermode='inside', relheight='0.1', relwidth='0.70', relx='0.2', rely='0.45', x='0', y='0')
        label_2 = ttk.Label(mainwindows)
        label_2.config(background='#ffffff', compound='top', cursor='arrow', font='{Roboto} 9 {}')
        label_2.config(justify='left', text='Peso :')
        label_2.place(anchor='nw', relx='0.09', rely='0.255', x='0', y='0')
        label_3 = ttk.Label(mainwindows)
        label_3.config(anchor='w', background='#ffffff', font='{roboto} 9 {}', takefocus=True)
        label_3.config(text='Altura :')
        label_3.place(anchor='nw', relx='0.09', rely='0.455', x='0', y='0')
        frame_2 = ttk.Frame(mainwindows)
        label_4 = ttk.Label(frame_2)
        label_4.config(cursor='arrow', font='{roboto} 12 {bold}', takefocus=False, text='Calculadora de IMC')
        label_4.place(anchor='nw', relx='0.30', rely='0.30', x='0', y='0')
        frame_2.config(cursor='arrow', height='200', width='200')
        frame_2.place(anchor='nw', relheight='0.2', relwidth='1.0', rely='0', x='0', y='0')
        button_7 = ttk.Button(mainwindows)
        button_7.config(state='disabled', text='Kg')
        button_7.place(anchor='nw', relheight='0.1', relwidth='0.1', relx='0.8', rely='0.25', x='0', y='0')
        button_8 = ttk.Button(mainwindows)
        button_8.config(state='disabled', text='cm')
        button_8.place(anchor='nw', relheight='0.1', relwidth='0.1', relx='0.8', rely='0.45', x='0', y='0')
        frame_2_3 = tk.Frame(mainwindows)
        label_1 = tk.Label(frame_2_3)
        label_1.config(background='#E0F0D9', cursor='arrow', font='TkDefaultFont', foreground='#39773a')
        label_1.config(text='Tu IMC (indice de masa corporal) es :')
        label_1.place(anchor='nw', relx='0.05', rely='0.10', x='0', y='0')
        label_2_3 = tk.Label(frame_2_3)
        label_2_3.config(background='#e0f0d9', font='{Arial} 20 {}', foreground='#39773a', text='Peso Normal')
        label_2_3.place(anchor='nw', relwidth='1.0', rely='0.35', x='0', y='0')
        frame_2_3.config(background='#e0f0d9', height='200', width='200')
        frame_2_3.place(anchor='nw', relheight='0.23', relwidth='0.7', relx='0.15', rely='0.74', x='0', y='0')
        calcular = tk.Button(mainwindows)
        calcular.config(activebackground='#5cb95c', activeforeground='#fff', background='#5cb95c', borderwidth='0')
        calcular.config(compound='top', disabledforeground='#fff', foreground='#fff', text='Calcular')
        calcular.place(anchor='nw', relheight='0.10', relwidth='0.35', relx='0.1', rely='0.605', x='0', y='0')
        limpiar = tk.Button(mainwindows)
        limpiar.config(activebackground='#5cb95c', activeforeground='#fff', background='#5cb95c', borderwidth='0')
        limpiar.config(foreground='#fff', text='Limpiar')
        limpiar.place(anchor='nw', relheight='0.10', relwidth='0.35', relx='0.55', rely='0.605', x='0', y='0')
        mainwindows.config(height='200', width='200')
        mainwindows.grid()

        # Main widget
        self.mainwindow = mainwindows


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = InterfazApp(root)
    app.run()
