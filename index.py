
from tkinter import ttk, filedialog, filedialog, Tk       #importa a biblioteca Tkinter
import BeW  # importa o arquivo responsavel pela segmentação

class Root(Tk):
    def __init__(self):                      
        super(Root, self).__init__()
        self.title("Segmentação de imagens")
        self.minsize(600,600)
        self.labelFrame = ttk.LabelFrame(self,text = "Abrir")
        self.labelFrame.grid(column = 0,row = 1,pady = 20)
       

        self.button()
        

    def button(self): # botão grafico
        self.button = ttk.Button(self.labelFrame, text ="Arquivo", command = self.fileDialog)
        self.button.grid(column = 1,row = 1)            
        
   

    def fileDialog(self): # função responsavel por abrir a imagem e retronar o caminho
        global caminho 
        caminho = filedialog.askopenfilename()
        root.quit()

    def showimage(self):
        BeW.imagem(caminho)   #Chama o arquivo BeW e executa a função Imagem
        

    def quit():
        global root #finaliza o programa após após o término da segmentação
        root.destroy()
    
    
if __name__=='__main__':  #construtor da interface
    root = Root()
    root.mainloop()
    root.showimage()
 
    
    
    
