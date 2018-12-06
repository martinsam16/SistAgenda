from six.moves import tkinter as tk

class UI(tk.Frame):

    def __init__(self,parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
    
    def variables(self):
        self.nombre=""
    
    def init_ui(self):
        #Aqui iran mis widgets
        self.parent.title("Titulo")

        etiqueta = tk.Label(self.parent, text="Demo")
        etiqueta.pack()
        self.apellido=""

        def btngg():
            self.nombre= inpNom.get()
        
        def btnjj():
            print(self.nombre)
            

        inpNom= tk.Entry(self.parent,textvariable=self.apellido)
        inpNom.pack()

        btnRegPer= tk.Button(self.parent,text='Registrar',command=btngg)
        btnRegPer.pack()

        btnot= tk.Button(self.parent,text="Prueba",command=btnjj)
        btnot.pack()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("300x100")
    APP = UI(parent=ROOT)
    APP.mainloop()