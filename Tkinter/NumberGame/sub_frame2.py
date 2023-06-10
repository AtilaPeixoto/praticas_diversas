from tkinter import *
from sub_frame import *

class Contador(Frame):
    def __init__(self, master=None, *x):
        super().__init__(master=master, *x)
        self.lista = []
        
        self.cont = IntVar()
        lbl_contador = Label(self, text='Número de Tentativas: ')
        lbl_valor = Label(self, textvariable=self.cont)
        
        self.contvitorias = IntVar()
        lbl_contadorVic = Label(self, text='Número de Vitórias: ')
        lbl_valorV = Label(self, textvariable=self.contvitorias)
        
        lbl_lista_jogados = Label(self, text='Até agóra você jogou: ')
        self.lbl_jogados = Label(self, text='')
        
        lbl_contadorVic.grid(row=0, column=0)
        lbl_valorV.grid(row=0, column=1, columnspan=2)
        lbl_contador.grid(row=0, column=4)
        lbl_valor.grid(row=0, column=5, columnspan=2)
        lbl_lista_jogados.grid(row=1, column=0)
        self.lbl_jogados.grid(row=1, column=1, columnspan=4)
        
        
        
    def contar(self):
        self.cont.set(self.cont.get() +1)
      
        
    def contar_vitorias(self):
         self.contvitorias.set(self.contvitorias.get() +1 )
        
    
    def listar_jogados(self, n):
        self.lista.append(n)
        return self.lbl_jogados.config(text=self.lista)
    
    
