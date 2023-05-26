from  time import sleep
from datetime import date
 


class aparencia:
    
    # def cores(self):
    #     self.cor = {"sublinhado": "\033[4m",
    #     "vermelho": "\033[31m",
    #    "negrito": "\033[1m",
    #    "branco": "\033[7m",
    #    "limpa": "\033[m"
    #    }
    
    
    def linha(self):
        print("="*40)
        
        
    def logotipo(self):
        self.linha()
        print(f"{'BANCO':=^40}")
        self.linha()
    
    
    def carregar(self):
        print('Carregando', end=' ')
        self.pontuar()
        
        
    def pontuar(self): 
        for i in range(0, 3):
            print('.', flush=True, end=' ')
            sleep(2)
        print()

        
    def iniciar(self):
        print()
        self.logotipo()
        print(f"{'INICIANDO':>30}", end='')
        self.pontuar()
        sleep(3)
        print(f" {date.today()}{'INSIRA O CARTAO':>22}")
        sleep(2)
        print()


