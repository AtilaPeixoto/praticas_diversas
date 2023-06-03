from tkinter import *
from frame1 import *

janela = Tk()
janela.title('Quiz ')
janela.geometry('500x500')



jogo = Jogo(janela)

jogo.place(relx=0.2, rely=0.2)



janela.mainloop()