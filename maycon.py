from os import close        #nada
from tkinter import *     #janela grafica
from tkinter import ttk    
from tkinter import filedialog  #procura imagens
import BeW                    # oque comunica com o outro codigo
import sys                  # tirar depois
class Root(Tk):
    def __init__(self):                      
        super(Root, self).__init__()
        self.title("Segmentação")
        self.minsize(600,600)
        self.labelFrame = ttk.LabelFrame(self,text = "abrir")
        self.labelFrame.grid(column = 0,row = 1,pady = 20)
       

        self.button()
        
        
        

    def button(self):                           # botão grafico
        self.button = ttk.Button(self.labelFrame, text ="Arquivo", command = self.fileDialog)
        self.button.grid(column = 1,row = 1)            
        
   

    def fileDialog(self):
        global caminho                         # metodo de procura de imagem
        caminho = filedialog.askopenfilename()
        root.quit()

    def showimage(self):
        BeW.teste(caminho)   #atenção
        

    def quit():
        global root         #finaliza sem bugar
        root.destroy()
    
    
if __name__=='__main__':           #loop da janela grafica
    root = Root()
    root.mainloop()
    root.showimage()
 
    
    
    
