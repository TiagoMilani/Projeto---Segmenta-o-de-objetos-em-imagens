from os import close
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import preto
import sys
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Test")
        self.minsize(640,40)
        #self.wm_iconbitmap('icon.ico')
      



        self.labelFrame = ttk.LabelFrame(self,text = "abrir")
        self.labelFrame.grid(column = 0,row = 1,pady = 20)

        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text ="Arquivo", command = self.fileDialog)
        self.button.grid(column = 1,row = 1)
        

    def fileDialog(self):
        global caminho
        caminho = filedialog.askopenfilename()
        root.quit()

    def showimage(self):
        preto.teste(caminho)   
        

if __name__=='__main__':
    root = Root()
    root.mainloop()
    root.showimage()
    
    
    