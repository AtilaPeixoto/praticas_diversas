import tkinter as tk
from tkinter import ttk, Frame, StringVar, END
from qr_gerador import Code

G = Code()


class Gerador(Frame):
    def __init__(self, janela, style):
        super().__init__()
        self.item = StringVar()
        self.nomeItem = StringVar()
        self.style = style
        self.style.theme_use('vista')
        
        img = tk.PhotoImage(file='img/a4.png', height=50)
        marca = ttk.Label(self, image=img)
        marca.image = img
        
        self.instrucao1 = ttk.Label(self, text='Escreva algo ou cole um link:', border=1, relief='sunken')
        self.instrucao2 = ttk.Label(self, text='Escreva o nome do arquivo:', border=1, relief='sunken')
        self.entrada1 = ttk.Entry(self, textvariable=self.item)
        self.entrada2 = ttk.Entry(self, textvariable=self.nomeItem)
        self.executar = ttk.Button(self, text='Gerar QRcode', command=lambda:recolher_itens(self.item, self.nomeItem))
        
        self.instrucao1.grid(row=0, column=0, padx=10, pady=10)
        self.instrucao2.grid(row=1, column=0, padx=10, pady=10)
        self.entrada1.grid(row=0, column=1, padx=10, pady=10)
        self.entrada2.grid(row=1, column=1, padx=10, pady=10)
        self.executar.grid(row=2, column=0, padx=10, pady=10)
        marca.grid(row=2, column=1, padx=10, pady=10,)
        

        self.entrada1.insert(0, 'Digite algo aqui...')
        self.entrada1.bind('<FocusIn>', self.on_entry_click)
        self.entrada1.bind('<FocusOut>', self.on_focusout)
                
        def recolher_itens(item, nomeItem):
            self.item.set(self.entrada1.get())
            self.nomeItem.set(self.entrada2.get())
            G.gerar(self.item, self.nomeItem)
        
        
    def on_entry_click(self, event):
        if self.entrada1.get() == 'Digite algo aqui...':
           self.entrada1.delete(0, END)
           self.entrada1.config(font='black 12')

    def on_focusout(self, event):
        if self.entrada1.get() == '':
           self.entrada1.insert(0, 'Digite algo aqui...')
           self.entrada1.config(font='grey 12')
        
  