from tkinter import Tk, Frame, ttk
from tkinter import *



class Questoes(Frame):
    def __init__(self, *x):
        super().__init__()
        
        self.lbl_pergunta = ttk.Label(self, text='Adicione a pergunta:')
        self.lbl_resposta = ttk.Label(self, text='Adicione a resposta correta:')
        self.lbl_opcoes = ttk.Label(self, text='Adicione as opções:')
        self.lbl_genero = ttk.Label(self, text='Adicione a matéria da pergunta:')
        
        self.pergunta = ttk.Entry(self, text='')    
        self.certa = ttk.Entry(self, text='')    
        self.opcao1 = ttk.Entry(self, text='')    
        self.opcao2 = ttk.Entry(self, text='')    
        self.opcao3 = ttk.Entry(self, text='')    
        self.genero = ttk.Combobox(self)
        self.genero['values'] = ('Matematica',
                                 'Português',
                                 'Historia',
                                 'Geografia',
                                 'Conhecimentos Gerais',
                                 'Biologia',
                                 'Química',
                                 )
        self.enviar = ttk.Button(self, text='Salvar', command=self.salvar)
        
        self.lbl_pergunta.grid()
        self.pergunta.grid()
        self.lbl_resposta.grid()
        self.certa.grid()
        self.lbl_opcoes.grid()
        self.opcao1.grid()
        self.opcao2.grid()
        self.opcao3.grid()
        self.enviar.grid()
        self.lbl_genero.grid()
        self.genero.grid()
        
        
    def salvar(self):
        pergunta = self.pergunta.get()
        resposta = self.certa.get()
        opcao1 = self.opcao1.get()
        opcao2 = self.opcao2.get()
        opcao3 = self.opcao3.get() 
        with open('perguntas.txt', 'a') as f:
                banco_perguntas = f.write(f'{pergunta}; {resposta}; {opcao1}; {opcao2}; {opcao3} \n')
                
                
   
        
                
a = Questoes()
a.grid()

a.mainloop()