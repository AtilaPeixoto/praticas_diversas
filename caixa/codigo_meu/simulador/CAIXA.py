from designer_caixa import aparencia
from menus_caixa import Osistema

a = aparencia()
Osis = Osistema()

class Caixa:
    
    
    def __init__(self):
        a.iniciar()
        Osis.entrada()                         
        a.carregar()
        self.painel_menus()
        
        
    def painel_menus(self):
        while True:  
            a.logotipo()                    
            Osis.saldoConta()                 
            a.linha()
            Osis.menuPrincipal()              
            a.linha()
            
            try:
                if Osis.sair():
                    break
            except:
                self.painel_menus()
                
    
        
inicio = Caixa()
inicio.__init__()        