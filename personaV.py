from tkinter import messagebox as popup,Tk, Label,Entry, Button, StringVar,\
    IntVar
import personaD
import personaC
from mock.mock import self

class personaV():

    def iniciarComponentes(self):
        ventana = Tk()
        ventana.title('Persona')
        ventana.geometry("600x300")

        nombre = StringVar()
        apellido = StringVar()
        dni = IntVar()

        lblNomPer= Label(ventana, text='Nombres').pack()
        inptNomPer = Entry(ventana,textvariable=nombre,width=50)
        inptNomPer.pack()
                    
        lblApePer= Label(ventana, text='Apellidos').pack()
        inptApePer=Entry(ventana,textvariable=apellido,width=50)
        inptApePer.pack()

        lblDniPer = Label(ventana,text='DNI').pack()
        inptDniPer= Entry(ventana,textvariable=dni,width=50)
        inptDniPer.pack()

        def btnRegPer():
            persona = personaC.personaC()
            persona.variablesM(inptNomPer.get(), inptApePer.get(),inptDniPer.get())
            if (persona.RegistrarPer()):
                inptNomPer.delete(0, 'end')
                inptApePer.delete(0, 'end')
                inptDniPer.delete(0, 'end')
                popup.showinfo("Info", "Registro Correcto!")
            else:
                popup.showerror("Error!", "Algo salió mal")

        def btnShowPer():
            persona = personaD.PersonaD()
            persona.ShowPer()

        btnRegPer= Button(ventana,text='Registrar',command=btnRegPer).pack()
        btnShowPer= Button(ventana,text='Mostrar',command=btnShowPer).pack()

        ventana.mainloop()

#gg_Kody Simpson

personaV.iniciarComponentes(self)
