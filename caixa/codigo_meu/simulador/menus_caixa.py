from designer_caixa import aparencia
from datetime import datetime, date
from time import sleep


data = datetime.now().isoformat(timespec='seconds')
data2 = date.today()
a = aparencia()


class Osistema:
        
    def entrada(self):
        try:
            int(input(f"SENHA: ")) 
        except:
            print(f'Senha Invalida')
            self.entrada()
    
        
    def saldoConta(self):
        try:
            if self.novosaldo > 0:
                self.Novo()
            else:    
                self.saldo = float(3141592.65)
                print(data2)
                print(f"Seu SALDO R$: {self.saldo}") 
        except:
            self.novosaldo = 0
            self.saldoConta()
        
            
    def SisFora(self):
        print(f"{'Função indisponivel.':>27}")
        print(f"{'Sistema Fora de Rede':>34}")
        sleep(3)
        
    
    def menuPrincipal(self):
        self.menu = ['[1] Transferir', '[2] Sacar', '[3] Pagar', '[4] Extrato', '[5] Sair']
        print('Escolha a sua ação;')
        for i in self.menu:
            print(i)
        self.acao()
            
            
    def acao(self):        
        try:
            self.opcao = int(input('Opção:   '))
            if  0 < self.opcao < 6:
                 self.escolha()
            else:
                print('valor invalido')
                self.menuPrincipal()
        except:
              print('Digito Invalido')
              self.menuPrincipal()
            
            
    def escolha(self):
        if self.opcao == 1:
            a.logotipo()           
            self.SisFora()     # sistema fora
            a.linha()
            self.menuPrincipal()           
        elif self.opcao == 2:
            a.logotipo()
            try:
                self.saque = int(input(f"{'Valor do Saque:':>22}"))
                self.infoSaque()
            except:
                print('Valor Invalido')
                self.menuPrincipal()                   
        elif self.opcao == 3:
            a.logotipo()           
            self.SisFora()     # sistema fora
            a.linha()
            self.menuPrincipal()           
        elif self.opcao == 4:
            self.extrato() 
        elif self.opcao == 5:
            self.sair()
        else:
           a.logotipo()
           print(f"{'Opção invalida':>23}")
           a.linha()
            
    
    def extrato(self):
        try:
            if self.saldoa > 0:
                print(f"Transaçções recentes")
                if self.saldob > 0:
                    print(f"{data} {'Saldo anterior:':<16}{self.saldob}")
                print(f"{data} {'Saldo anterior:':<16}{self.saldoa}")
                print(f"{data} {'Saldo atual:':<16}{self.saldo}")
            else:
                print(f'Nao há transaçoes recentes')
                self.saldoConta()
                self.menuPrincipal()
        except:
            self.saldoa = self.saldob = self.saldo
            self.extrato()
            
            
    def infoSaque(self):
        try:
            self.saldob = self.saldoa
            self.saldoa = self.saldo
            self.saldo -= self.saque
            self.novosaldo = self.saldo
            a.linha()
            a.logotipo()
            print(data)
            print(f"Saque de {self.saque}")
            print(f"Novo SALDO: {self.novosaldo}")
            print(f"Saldo anterior R${self.saldoa}")
            a.linha()
            self.notas()
        except:
            self.saldoa = 0
            self.infoSaque()
            
            
    def Novo(self):
        print(data2)
        print(f"Seu SALDO R$: {self.novosaldo}")
        
                
    def notas(self):
        restodiv = self.saque % 200                                
        if self.saque >= 200:
            self.n100 = self.saque // 100
        else:
            self.n100 = 0
        if restodiv >= 50:
            self.n50 = restodiv // 50
            restodiv = restodiv % 50
        else:
            self.n50 = 0
        if restodiv >= 20:
            self.n20 = restodiv // 20
            restodiv = restodiv % 20
        else:
            self.n20 = 0
        if restodiv >= 10:
            self.n10 = restodiv // 10
            restodiv = restodiv % 10
        else:
            self.n10 = 0
        if restodiv >= 5:
            self.n5 = restodiv // 5
        else:
            self.n5 = 0
        self.totnotas()       
        
        
    def totnotas(self):   
        if self.n100 > 0:
            print(f"Total de notas de cem {self.n100}")
        if self.n50 > 0:
            print(f"Total de notas de cinquenta {self.n50}")    
        if self.n20 > 0:
            print(f"Total de notas de vinte {self.n20}")    
        if self.n10 > 0:
            print(f"Total de notas de dez {self.n10}")       
        if self.n5 > 0:
            print(f"Total de notas de cinco {self.n5}")
     
                
    def sair(self):
        a.logotipo()
        print(f"{'Agradecemos sua preferencia.':>34}")  
         
        
        

        
        