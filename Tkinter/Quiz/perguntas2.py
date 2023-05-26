import random


class Start:
    perguntas = [['pergunta', 'resposta', ['alternativa1', 'flternativa2', 'alternativa3']],
                ['pergunta', 'resposta', ['zlternativa1', 'alternativa2', 'alternativa3']]
]

    def preparando(self):
        pergunta_escolhida = random.choice(self.perguntas)
        self.pergunta = pergunta_escolhida[0]
        
        certa = pergunta_escolhida[1]
        
        self.opcoes = pergunta_escolhida[2]
        self.opcoes.append(certa)
        random.shuffle(self.opcoes)
        
        self.indice = self.opcoes.index(certa)
        self.indice += 1
        
        
        self.perguntando(self)
        
        
    def perguntando(self, *args):
        print('='*40)
        print(self.pergunta)
        print('='*40)
        
        for i in range(len(self.opcoes)):
            print(i+1, end=' ')
            
            print(self.opcoes[i])
            print()
            
        
        self.respondendo(self) 
            
            
    def respondendo(self, *args):
        print('='*40)
        self.res = int(input('Resposta:    '))
        print('='*40)
        
        self.verificacao()
       
    
        
    
    def verificacao(self):
        print(self.indice)
        if self.res == self.indice:
            print( 'acerto')
        else:
            print('erro')
        
         
jogo = Start()
jogo.preparando()
