from tkinter import ttk
from random import randint
from sub_frame2 import *


class Jogando(Frame):
    def __init__(self, x, contador, style):
        super().__init__()
        self.contador = contador 
        
        self.s = style
        self.tema = self.s.theme_use('clam')
        self.fundo = self.s.lookup('self.tema', 'background')
        
        self['bd'] = 2
        self['relief'] = 'solid'
        self['background'] = self.fundo
        
        borda_frame = Frame(self, height=200, width=300,)
        borda_frame['background'] = self.fundo
        borda_frame.grid_propagate(0)
        
        
        self.numero_jogador = StringVar()   
        self.falar = StringVar()
        self.n_bot = 0
        self.lista_maior_menor = [
                                'Muito baixo, tente um maior.',
                                'Muito Alto, tente um menor.',
                                'Acertou!!!',
                                'Isso não é um numero.\nDigite um numero!',
                                ]
        
        
        lbl = ttk.Label(borda_frame, text='Escolha um número! \nTente a sua sorte!!!')
        self.campo_numero = ttk.Entry(borda_frame, textvariable=self.numero_jogador)
        self.btn = ttk.Button(borda_frame, text='Jogar', command=self.executar)
        lbl_resposta = ttk.Label(borda_frame, textvariable=self.falar, anchor='center', justify='center', width=30)
        
       
        
        lbl.grid(row=1, column=1, padx=70, pady=10)
        self.campo_numero.grid(row=2, column=1, padx=70, pady=10)
        self.campo_numero.bind('<Return>', lambda event:self.executar())
        self.campo_numero.focus()
        
        self.btn.grid(row=3, column=1, pady=10, padx=70)
        lbl_resposta.grid(row=4, column=1, padx=70)
        borda_frame.grid(padx=50, pady=5, ipady=5, ipadx=10)
        
        
    def validacao(self):
        x = self.campo_numero.get()
        try:
            x = int(x)
            return True
        except: 
            return False
        

    
    def executar(self):
        bot = self.sortear()
        if self.validacao(): 
            jogador = self.pegar_numero()
            if jogador > bot:
                self.falar.set(self.lista_maior_menor[1])
            elif jogador < bot:
                self.falar.set(self.lista_maior_menor[0])
            elif jogador == bot:
                self.n_bot = 0
                self.contador.contar_vitorias()
                self.falar.set(self.lista_maior_menor[2])
        else:
            self.falar.set(self.lista_maior_menor[3])
        self.campo_numero.focus()
        
        
        
    def sortear(self):
        if self.n_bot == 0:
            self.n_bot = randint(0, 5)
            return self.n_bot
        else:
            self.n_bot = self.n_bot
            return self.n_bot
        
        
    def pegar_numero(self):
        self.contador.contar()
        return int(self.numero_jogador.get())  
    
  
        
