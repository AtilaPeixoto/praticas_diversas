from random import randint
import PySimpleGUI as sg
from time import sleep

class genio:
 
    def __init__(self):
            self.mm = 1
            self.mx = 9
            self.cont = 0 
            self.maior = f'Maior... Foi baixo.\n    Tente mais alto!'
            self.menor = f'Menor...Foi alto.\n  Tente mais baixo!'
            
            
    def tela(self):
        layout = [
            [sg.Text('Escolha um numero', text_color='#fffafa', background_color='#000000')],
            [sg.Input(size=(3, 2), key='ValorChute', do_not_clear=False)],
            [sg.Button('Acerte!', size=(17, 2), button_color='#9400d3', mouseover_colors='#000000'), sg.Button('Não, foi o suficiente.', size=(17, 2), button_color='#9400d3', mouseover_colors='#ff0000')],
            [sg.Output(size=(40, 10))]
        ]       
        self.janela = sg.Window('Adivinhe o numero', layout=layout, background_color='#000000')
        self.evento, self.valores = self.janela.Read()        
        
        
    def aleatorio(self):
        self.ale = randint(self.mm, self.mx)
        self.inicio()
    
    
    def inicio(self):
        self.tela()        
        while True:               
            self.evento, self.valores = self.janela.Read() 
            if self.evento == sg.WIN_CLOSED or self.evento == 'Não, foi o suficiente.':
                break             
            if self.evento == 'Acerte!':
                self.isnumero()
           
           
    def isnumero(self):
        try:
            self.pergunta = self.valores['ValorChute']               
            if self.pergunta.isnumeric():
                self.cont += 1
                self.numero = int(self.pergunta)
                print(f'{self.numero}...')
                self.acertar()
            else:
                print('Isso não foi um numero... \n Digite um numero!')    
        except:
            self.inicio()
            
                        
    def acertar(self):
        if self.numero > self.ale:
            print(self.menor)                           
        elif self.numero < self.ale:
            print(self.maior)                            
        else:
            self.vencedor()       
                
                
    def vencedor(self): 
        vic = [
            [sg.Text('PARABENS VOCE ACERTOU!!!', background_color='#000000', text_color='#fffafa')],
            [sg.Text('Jogar Novamente?!', background_color='#000000')],
            [sg.Text(f'Foram um total de:{self.cont} tentativas', background_color='#000000')]
        ]
        self.mais = sg.Window('Parabens', layout=vic, background_color='#000000')
        while True:
            self.event, self.valor = self.mais.Read()        
            if self.valor == sg.WIN_CLOSED:
                break
                    
jogo = genio()
jogo.aleatorio()


