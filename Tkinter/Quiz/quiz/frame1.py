from tkinter import *
from tkinter import ttk
import random
from perguntas1 import *

# perguntas = [['Qual é a capital do Brasil?', 'Brasília',  ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']],
#                 ['Qual é o maior animal terrestre?', 'Elefante', ['Elefante', 'Girafa', 'Leão', 'Hipopótamo']]
#     ]

class Jogo(Frame):
    def __init__(self, janela):
        super().__init__()
        self['bd'] = 2
        self['relief'] = 'solid'
        
        self.inicio = ttk.Button(self, text='START', command=self.start)
        self.inicio.grid(row=0, pady=10)
        self.lbl_pergunta = ttk.Label(self, text='')
        self.lbl_pergunta.grid(row=1)
        
        self.frame_borda = Frame(self, height=200, width=350)
        self.frame_borda.grid(padx=10, pady=10, ipady=10)
        self.frame_borda.grid_propagate(0)
        self.lbl_resposta = ttk.Label(self.frame_borda, text='')
        self.lbl_resposta.grid(row=5, ipady=20)
        
        self.lista_btn = []    
        for i in range(1, 5):
            btn_respostas = ttk.Button(self.frame_borda, text='', width=30, command=lambda index=i: self.verificar(index))
            self.lista_btn.append(btn_respostas)
            btn_respostas.grid(row=i, padx=80)
            
        
    def start(self):
        self.retirar_cor()
        self.preparar()
        self.atribuir()
        self.armar()
    
    
    def preparar(self):
        self.sorteio = random.choice(perguntas)
        self.lbl_pergunta.config(text=f'{self.sorteio[0]}?')
        self.certa = self.sorteio[1]
        self.opcoes = self.sorteio[2]
        random.shuffle(self.opcoes)
        self.indice = self.opcoes.index(self.certa) +1
        
        
    def atribuir(self):
        for i in range(4):
            self.lista_btn[i].config(text=self.opcoes[i] )
        
            
    def verificar(self, index):
        if index == self.indice:
            self.confirmar_resposta(True)
            self.colorir('green')
            self.desarmar()
        else:
            self.confirmar_resposta(False)
            self.colorir('red')
            self.desarmar()
            
    
    def colorir(self, cor):
            self['bg'] = cor
            self.frame_borda['bg'] = cor
            
    
    def confirmar_resposta(self, x):
        if x:
            self.lbl_resposta.config(text='Uhulll, parabens!!!')
        else:
            self.lbl_resposta.config(text='ahh, errado. Mais sorte da proxima.')
            
            
    def desarmar(self):
        for i in range(4):
            self.lista_btn[i].config(state='disabled')
            
            
    def retirar_cor(self):
        self['bg'] = self.master['bg']
        self.frame_borda['bg'] = self.master['bg']
        
        
    def armar(self):
        for i in range(4):
            self.lista_btn[i].config(state='active')
            
        
            
      
 
            

            
