import tkinter as tk
from tkinter import ttk

from frame1 import Gerador


janela = tk.Tk()
janela.title('QRcode Gerador')

janela.iconbitmap(r'img\\a2.ico')

style = ttk.Style()
    
g = Gerador(janela, style)
g.grid()



janela.mainloop()