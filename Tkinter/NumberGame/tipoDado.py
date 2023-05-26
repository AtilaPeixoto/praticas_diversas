from tkinter import *
from random import randint

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


class Jogando(Frame):
    def __init__(self, x):
        super().__init__()
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
            jogador = self.mostrar_numero_escolhido()
            if jogador > bot:
                self.falar.set(self.lista_maior_menor[1])
            elif jogador < bot:
                self.falar.set(self.lista_maior_menor[0])
            elif jogador == bot:
                self.n_bot = 0
                frame_contador.contvitorias.set(frame_contador.contvitorias.get() +1 )
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
        print(self.n_bot)
        
        
        
    def mostrar_numero_escolhido(self):
        frame_contador.cont.set(frame_contador.cont.get() + 1)
        return int(self.numero_jogador.get())
            
   
janela = Tk()
janela.title('Jogo')
janela.geometry('500x300')



frame_contador = Contador(janela)
frame_contador.grid(row=0, column=0, columnspan=2)



sub_1 = Jogando(janela)
sub_1.grid(row=1, column=0, rowspan=4, columnspan=4, padx=50, pady=50, )

janela.mainloop()
