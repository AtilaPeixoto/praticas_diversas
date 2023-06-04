from tkinter import *
from tkinter import ttk
import random



perguntas1 = [['Qual é a capital do Brasil?', 'Brasília',  ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']],
                ['Qual é o maior animal terrestre?', 'Elefante', ['Elefante', 'Girafa', 'Leão', 'Hipopótamo']]
    ]

class Jogo(Frame):
    def __init__(self, janela):
        super().__init__()
        self['bd'] = 2
        self['relief'] = 'solid'
        
        self.inicio = ttk.Button(self, text='START', command=self.start)
        self.inicio.grid()
        
        frame_borda = Frame(self, height=100, width=200)
        self.lbl_pergunta = ttk.Label(frame_borda, text='')
        
        frame_borda.grid(padx=50, pady=25, ipady=10, ipadx=5)
        self.lbl_pergunta.grid(row=0)
        frame_borda.grid_propagate(0)
        
        self.lista_btn = []    
        for i in range(1, 5):
            btn_respostas = ttk.Button(frame_borda, text='respostas', width=30, command=lambda index=i: self.verificar(index))
            self.lista_btn.append(btn_respostas)
            btn_respostas.grid(row=i)
            
            
            
            
    def verificar(self, index):
        print(index, self.indice)
        if index == self.indice:
            self.msg = 'Parabens'
            print('parabens')
        else:
            self.msg = 'Errado. Desejo mais sorte'
            print('errado')
      
       
        
            
    def start(self):
        self.sorteio = random.choice(perguntas1)
        self.lbl_pergunta.config(text=self.sorteio[0])
        self.certa = self.sorteio[1]
        self.opcoes = self.sorteio[2]
        print(self.opcoes)
        random.shuffle(self.opcoes)
        self.indice = self.opcoes.index(self.certa) +1
        for i in range(4):
            self.lista_btn[i].config(text=self.opcoes[i] )
      
 
            
    def zerar(self):
        for i in range(4):
            self.lista_btn[i].config(text='vazio')
            
