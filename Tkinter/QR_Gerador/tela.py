from tkinter import Tk
from frame1 import Gerador


window = Tk()
window.title('QRcode Gerador')
# window.geometry('200x200')


            
    
g = Gerador(window)
g.grid()



window.mainloop()