import eel
import personaD
import personaC

eel.init('web')

@eel.expose
def RegPerr(nombre, apellido, dni, email):
    persona = personaC.personaC()
    persona.variablesM(nombre, apellido, dni, email)
    if (persona.RegistrarPer()):
        eel.AlertaJs("Registro Exitoso")
    else:
        eel.AlertaJs("Error RegPer")




@eel.expose
def ShowPer():
    persona = personaD.PersonaD()
    persona.ShowPer()

@eel.expose
def llenar(x):
    persona = personaD.PersonaD()
    persona.ShowPer1(x)


eel.start('index.htm', block=True)