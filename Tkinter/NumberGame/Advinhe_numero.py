from tkinter import *
from sub_frame import *
from sub_frame2 import *


        
   
janela = Tk()
janela.title('Jogo')
janela.geometry('500x300')



contador = Contador(janela)
contador.grid(row=0, column=0, columnspan=2)



sub_1 = Jogando(janela, contador)
sub_1.grid(row=1, column=0, rowspan=4, columnspan=4, padx=50, pady=50, )

janela.mainloop()
