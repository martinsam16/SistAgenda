from tkinter import *
import personaD

ventana = Tk()
ventana.title('Persona')

nombre = "1"
apellido="2"
dni="3"

lblNomPer= Label(ventana, text='Nombres').grid(row=1, column=1)
inptNomPer = Entry(ventana,textvariable=nombre,width=50)
inptNomPer.grid(row=1, column=2)

lblApePer= Label(ventana, text='Apellidos').grid(row=2,column=1)
inptApePer=Entry(ventana,textvariable=apellido,width=50)
inptApePer.grid(row=2,column=2)

lblDniPer = Label(ventana,text='DNI').grid(row=3,column=1)
inptDniPer= Entry(ventana,textvariable=dni,width=50)
inptDniPer.grid(row=3,column=2)

def btnRegPer():
    persona = personaD.PersonaD(inptNomPer.get(), inptApePer.get(), inptDniPer.get())
    persona.RegPer()

btnRegPer= Button(ventana,text='Registrar',command=btnRegPer,width=20).grid(row=4,column=1)

ventana.mainloop()