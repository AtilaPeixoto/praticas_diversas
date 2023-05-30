import qrcode


class Code():    
    def nomear(self, nomeItem):
        return nomeItem.get() +'.png'
        

    def gerar(self, item, nomeItem):
        img = qrcode.make(item.get()) 
        type(img)  
        img.save(self.nomear(nomeItem))
        
        
