from tkinter import Tk, Frame, ttk
from tkinter import *
import pickle

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
                                 'Portugues',
                                 'Historia',
                                 'Geografia',
                                 'Conhecimentos Gerais',
                                 'Biologia',
                                 'Quimica',
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
        self.lbl_genero.grid()
        self.genero.grid()
        self.enviar.grid()
        
        
    def salvar(self):
        self.coletar(self) 
        self.tipificar(self)  
        
        
    def coletar(self, *x):
        self.questao = []
        self.questao_opcoes = []
        self.questao.append(self.pergunta.get())
        self.questao.append(self.certa.get())
        self.questao_opcoes.append(self.opcao1.get())
        self.questao_opcoes.append(self.opcao2.get())
        self.questao_opcoes.append(self.opcao3.get())
        self.questao_opcoes.append(self.certa.get())
        self.questao.append(self.questao_opcoes[:])
        self.materia = self.genero.get()
       
        
    def tipificar(self, *x):
        if self.materia == 'Matematica':
            self.escrever(self, nome='Matematica')
        if self.materia == 'Portugues':
            self.escrever(self, nome='Portugues')
        if self.materia == 'Historia':
            self.escrever(self, nome='Historia')
        if self.materia == 'Quimica':
            self.escrever(self, nome='Quimica')
        if self.materia == 'Biologia':
           self.escrever(self, nome='Biologia')
        if self.materia == 'Geografia':
            self.escrever(self, nome='Geografia')
        if self.materia == 'Gerais':
            self.escrever(self, nome='Gerais')
            
    
    def escrever(self, *x, nome=''):
        try:
            with open('perguntas/'+ nome +'.txt', 'a') as f:
                f.writelines(f'{str(self.questao)} \n')
        except:     
            with open('perguntas/'+ nome + '.txt', 'x') as f:
                f.writelines(f'{str(self.questao)} \n')
    
   
        

a = Questoes()
a.grid()

a.mainloop()