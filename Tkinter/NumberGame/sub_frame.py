from tkinter import *
from random import randint
from sub_frame2 import *


class Jogando(Frame):
    def __init__(self, x, contador):
        super().__init__()
        self.contador = contador 
        self['bd'] = 2
        self['relief'] = 'solid'
        
        borda_frame = Frame(self)
        
        self.numero_jogador = StringVar()   
        self.falar = StringVar()
        self.n_bot = 0
        self.lista_maior_menor = ['Muito baixo, tente um maior',
                                  'Muito Alto, tente um menor.',
                                  'Acertou!!!',
                                  'Isso não é um numero.\nDigite um numero!',
                                  ]
        
        lbl = Label(borda_frame, text='Escolha um número! \nTente a sua sorte!!!')
        self.campo_numero = Entry(borda_frame, textvariable=self.numero_jogador)
        self.btn = Button(borda_frame, text='Jogar', command=self.executar)
        lbl_resposta = Label(borda_frame, textvariable=self.falar, width=25)
        
        lbl.grid()
        self.campo_numero.grid()
        self.campo_numero.bind('<Return>', lambda event:self.executar())
        self.btn.grid()
        lbl_resposta.grid()
        self.campo_numero.focus()
        borda_frame.grid(padx=100, pady=30)
        
        
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
        
