from tkinter import *
from sub_frame import *

class Contador(Frame):
    def __init__(self, master=None, *x):
        super().__init__(master=master, *x)
        
        self.cont = IntVar()
        lbl_contador = Label(self, text='Numero de Tentativas: ')
        lbl_valor = Label(self, textvariable=self.cont)
        
        self.contvitorias = IntVar()
        lbl_contadorVic = Label(self, text='Numero de Vitorias: ')
        lbl_valorV = Label(self, textvariable=self.contvitorias)
        
        lbl_contadorVic.grid(row=0, column=0)
        lbl_valorV.grid(row=0, column=1, columnspan=2)
        
        lbl_contador.grid(row=0, column=4)
        lbl_valor.grid(row=0, column=5, columnspan=2)
        
        
        
    def contar(self):
        self.cont.set(self.cont.get() +1)
      
        
        
    def contar_vitorias(self):
         self.contvitorias.set(self.contvitorias.get() +1 )
        