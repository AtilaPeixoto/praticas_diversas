import tkinter as tk
from tkinter import ttk, Frame, StringVar
from qr_gerador import Code

G = Code()


class Gerador(Frame):
    def __init__(self, *x):
        super().__init__()
        self.item = StringVar()
        self.nomeItem = StringVar()
        
        img = tk.PhotoImage(file='img/a.png')
        marca = ttk.Label(self, image=img)
        marca.image = img
        
        self.instrucao1 = ttk.Label(self, text='Escreva algo ou cole um link')
        self.instrucao2 = ttk.Label(self, text='Escreva o nome do arquivo')
        self.entrada1 = ttk.Entry(self, textvariable=self.item)
        self.entrada2 = ttk.Entry(self, textvariable=self.nomeItem)
        self.executar = ttk.Button(self, text='Gerar QRcode', command=lambda:recolher_itens(self.item, self.nomeItem))
        self.instrucao1.grid(row=0, column=0, padx=10, pady=10)
        self.instrucao2.grid(row=1, column=0, padx=10, pady=10)
        self.entrada1.grid(row=0, column=1, padx=10, pady=10)
        self.entrada2.grid(row=1, column=1, padx=10, pady=10)
        self.executar.grid(row=2, column=0, padx=10, pady=10)
        marca.grid(row=2, column=1, padx=10, pady=10)
        
        
        def recolher_itens(item, nomeItem):
            self.item.set(self.entrada1.get())
            self.nomeItem.set(self.entrada2.get())
            G.gerar(self.item, self.nomeItem)
        