from tkinter import ttk
from sub_frame import *
from sub_frame2 import *


        
   
janela = Tk()
janela.title('Jogo')
janela.geometry('500x300')

janela.iconbitmap('img/a2.ico')

contador = Contador(janela)
contador.grid(row=0, column=0, columnspan=2)


style = ttk.Style()

sub_1 = Jogando(janela, contador, style)
sub_1.grid(row=1, column=0, rowspan=4, columnspan=4, padx=50, pady=50, )

janela.mainloop()
