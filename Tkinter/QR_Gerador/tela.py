import tkinter as tk
from frame1 import Gerador


janela = tk.Tk()
janela.title('QRcode Gerador')

janela.iconbitmap(r'img\\a2.ico')


    
g = Gerador(janela)
g.grid()



janela.mainloop()