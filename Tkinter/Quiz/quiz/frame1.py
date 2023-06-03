from tkinter import *
from tkinter import ttk
import random



perguntas = [['Qual é a capital do Brasil?', 'Brasília', ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte']],
                ['Qual é o maior animal terrestre?', 'Elefante', ['Girafa', 'Leão', 'Hipopótamo']]
    ]

class Jogo(Frame):
    def __init__(self, janela):
        super().__init__()
        self['bd'] = 2
        self['relief'] = 'solid'
        
        self.inicio = ttk.Button(self, text='START', command=self.start)
        self.inicio.grid()
        
        frame_borda = Frame(self)
        self.pergunta = ttk.Label(frame_borda, text='Pergunta')
        
        frame_borda.grid(padx=50, pady=25, ipady=10, ipadx=5)
        self.pergunta.grid(row=0)
        
        self.lista_btn = []    
        for i in range(1, 5):
            btn_respostas = ttk.Button(frame_borda, text='respostas', command=lambda index=i: self.verificar(index))
            self.lista_btn.append(btn_respostas)
            btn_respostas.grid(row=i)
            
            
            
            
    def verificar(self, index):
        self.indice = 1
        if self.indice == index:
            self.msg = 'Parabens'
        else:
            self.msg = 'Errado. Desejo mais sorte'
        for i in range(4):
            self.lista_btn[i].config(text='vazio')
       
        
            
    def start(self):
        sorteio = random.choice(perguntas)
        self.pergunta = sorteio[0]
        self.certa = sorteio[1]
        self.opcoes = sorteio[2]
        self.opcoes.insert(random.randint(0, 2), self.certa)
        for i in range(4):
            self.lista_btn[i].config(text=self.opcoes[i])
            
 
            
